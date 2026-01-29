from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from decision import decide
from policy import check_policy
from executor import run_tool
from auth import check_auth
from logger import log_event
from tool_discovery import discover_tools

HOST = "0.0.0.0"
PORT = 9100

PENDING_CONFIRMATIONS = {}
AVAILABLE_TOOLS = discover_tools()

print("[MCP] Discovered tools:", ", ".join(AVAILABLE_TOOLS.keys()))

class MCPHandler(BaseHTTPRequestHandler):

    def respond(self, payload, code=200):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    def do_GET(self):
        self.respond({
            "status": "alive",
            "available_tools": list(AVAILABLE_TOOLS.keys())
        })

    def do_POST(self):
        try:
            if not check_auth(self.headers):
                log_event("AUTH_FAIL", self.client_address[0])
                self.respond({"status": "unauthorized"}, 401)
                return

            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length)
            data = json.loads(raw.decode())

            log_event("REQUEST", data)

            if "confirm_token" in data:
                token = data["confirm_token"]
                decision_data = PENDING_CONFIRMATIONS.pop(token, None)

                if not decision_data:
                    self.respond({"status": "invalid_token"})
                    return

                output = run_tool(
                    decision_data["tool"],
                    decision_data.get("target")
                )

                log_event("EXECUTED", decision_data["tool"])

                self.respond({
                    "status": "executed",
                    "tool": decision_data["tool"],
                    "output": output[:8000]
                })
                return

            user_input = data.get("input", "")
            decision_data = decide(user_input)
            tool = decision_data.get("tool")

            log_event("DECISION", decision_data)

            if not tool:
                self.respond({"status": "no_action"})
                return

            allowed, reason = check_policy(tool)
            if not allowed:
                log_event("BLOCKED", reason)
                self.respond({"status": "blocked", "reason": reason})
                return

            if reason == "Confirmation required":
                token = str(len(PENDING_CONFIRMATIONS) + 1)
                PENDING_CONFIRMATIONS[token] = decision_data
                log_event("CONFIRM_REQUIRED", decision_data)

                self.respond({
                    "status": "confirmation_required",
                    "token": token
                })
                return

            output = run_tool(tool, decision_data.get("target"))
            log_event("EXECUTED", tool)

            self.respond({
                "status": "executed",
                "tool": tool,
                "output": output[:8000]
            })

        except Exception as e:
            log_event("SERVER_ERROR", str(e))
            self.respond({"status": "server_error", "error": str(e)}, 500)


print(f"[MCP] Tool Automation Server running on {HOST}:{PORT}")
HTTPServer((HOST, PORT), MCPHandler).serve_forever()
