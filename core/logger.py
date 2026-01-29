from datetime import datetime

LOG_FILE = "logs/audit.log"

def log_event(event_type, details):
    timestamp = datetime.utcnow().isoformat()
    line = f"[{timestamp}] {event_type}: {details}\n"

    with open(LOG_FILE, "a") as f:
        f.write(line)
