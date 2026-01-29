from tool_discovery import discover_tools
import subprocess

def run_tool(tool_name, target=None):
    tools = discover_tools()
    tool = tools.get(tool_name)

    if not tool:
        return "Tool not available"

    cmd = tool["command"]

    if "{target}" in cmd:
        cmd = cmd.replace("{target}", target or "")

    process = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    stdout, stderr = process.communicate(timeout=180)
    return stdout if stdout else stderr
