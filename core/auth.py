import os
from dotenv import load_dotenv

load_dotenv("config/.env")
API_KEY = os.getenv("API_KEY")

def check_auth(headers):
    return headers.get("X-API-Key") == API_KEY
