import json
from tool_discovery import discover_tools

PERMS = json.load(open("config/permissions.json"))

def check_policy(tool_name):
    tools = discover_tools()
    tool = tools.get(tool_name)

    if not tool:
        return False, "Tool not installed or not allowed"

    if tool["risk"] == "high" and not PERMS["allow_high_risk"]:
        return False, "High-risk tools blocked by policy"

    if tool["risk"] == "medium" and PERMS.get("require_confirmation", True):
        return True, "Confirmation required"

    return True, "Allowed"
