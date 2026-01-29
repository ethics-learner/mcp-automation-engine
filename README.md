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
