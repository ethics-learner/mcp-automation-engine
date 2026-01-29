import json
import shutil

CATALOG_FILE = "config/tool_catalog.json"

def discover_tools():
    """
    Discover which tools from catalog are actually installed
    """
    with open(CATALOG_FILE) as f:
        catalog = json.load(f)

    discovered = {}

    for tool_name, meta in catalog.items():
        binary = meta.get("binary")
        if shutil.which(binary):
            discovered[tool_name] = meta

    return discovered
