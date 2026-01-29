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
=======
# MCP Tool Automation Engine 🔐⚙️

A **Dockerized, policy-driven security tool automation engine** inspired by
Model Context Protocol (MCP) principles.

This platform converts **natural-language requests** into **controlled,
auditable tool execution** with strong safety boundaries.

> ⚠️ Designed for **authorized labs, learning, and defensive research only**.

---

## 🚀 Key Features

- 🔍 **Tool Auto-Discovery** (runs only if tool exists)
- 🧠 Natural language → structured decisions
- 🛡️ Policy enforcement (risk-aware)
- ✅ Confirmation flow for medium/high-risk tools
- 🔑 API-key authentication
- 📜 Full audit logging
- 📤 Export logs as **JSON / PDF**
- 🐳 Fully Dockerized (Kali Linux based)

---

## 🧰 Supported Tools (Auto-Discovered)

| Tool     | Purpose                  | Risk |
|----------|--------------------------|------|
| nmap     | Network scanning         | Low  |
| whois   | Domain intelligence      | Low  |
| dig     | DNS inspection           | Low  |
| nikto   | Web vulnerability scan  | Medium |

> Tools are discovered dynamically using `which`.
> If a tool is not installed, it cannot be executed.

---

## 🏗️ Architecture Overview

Client (curl / UI / AI)
|
| X-API-Key
v
+-----------------------+
| MCP HTTP Server |
+-----------------------+
|
v
+-----------------------+
| Decision Engine |
+-----------------------+
|
v
+-----------------------+
| Tool Auto-Discovery |
+-----------------------+
|
v
+-----------------------+
| Policy & Risk Gate |
+-----------------------+
|
v
+-----------------------+
| Confirmation Layer |
+-----------------------+
|
v
+-----------------------+
| Tool Executor |
+-----------------------+
|
v
+-----------------------+
| Audit Logger |
+-----------------------+


---

## 🐳 Run with Docker (Recommended)

### Build
```bash
docker build --no-cache -t mcp-tool-automation .

Run
docker run -p 9100:9100 mcp-tool-automation

🔐 Authentication

All requests require an API key.

X-API-Key: change-this-strong-key

Configured in:
config/.env


🙌 Author

Ethics Learner(Lalit Pandit)
Cybersecurity | Automation | Defensive Research
>>>>>>> 9cfbd38c0490b2269153c56a59f1d3d8685c3b5d
