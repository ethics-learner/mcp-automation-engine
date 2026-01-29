# MCP Tool Automation Engine

A standalone **MCP-style automation engine** that executes real system tools
with **policy enforcement, authentication, and confirmation gates**.

## Features
- Natural language → tool execution
- Policy & permission enforcement
- High-risk confirmation flow
- API key authentication
- Docker-ready

## Run (Local)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 core/mcp_server.py


Example Request:
curl -X POST http://127.0.0.1:9100 \
-H "X-API-Key: change-this-strong-key" \
-H "Content-Type: application/json" \
-d '{"input":"scan scanme.nmap.org"}'



High-Risk Confirmation:
curl -X POST http://127.0.0.1:9100 \
-H "X-API-Key: change-this-strong-key" \
-H "Content-Type: application/json" \
-d '{"confirm_token":"1"}'



Disclaimer:

Use only on systems you own or have permission to test.
