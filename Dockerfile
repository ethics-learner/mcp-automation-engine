FROM kalilinux/kali-rolling

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app

# ---- System tools ----
RUN apt update && apt install -y \
    python3 \
    python3-venv \
    python3-pip \
    nmap \
    nikto \
    whois \
    dnsutils \
    iproute2 \
    net-tools \
    curl \
 && apt clean \
 && rm -rf /var/lib/apt/lists/*

# ---- Python deps ----
COPY requirements.txt .
RUN python3 -m venv venv \
 && . venv/bin/activate \
 && pip install --no-cache-dir -r requirements.txt

# ---- App code ----
COPY core/ core/
COPY config/ config/
COPY logs/ logs/

EXPOSE 9100
CMD ["venv/bin/python", "core/mcp_server.py"]
