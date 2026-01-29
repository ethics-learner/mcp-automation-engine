def extract_target(text):
    for part in text.split():
        if "." in part or part.replace(".", "").isdigit():
            return part
    return None

def decide(user_input: str):
    text = user_input.lower()
    target = extract_target(text)

    if "nmap" in text or "scan" in text:
        return {"tool": "nmap", "target": target}

    if "whois" in text:
        return {"tool": "whois", "target": target}

    if "dig" in text or "dns" in text:
        return {"tool": "dig", "target": target}

    if "nikto" in text:
        return {"tool": "nikto", "target": target}

    if "ssh" in text:
        return {"tool": "ssh_logs"}

    if "tor" in text:
        return {"tool": "tor_logs"}

    return {"tool": None}
