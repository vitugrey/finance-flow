import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("TELEGRAM_API_ID"))
API_HASH = os.getenv("TELEGRAM_API_HASH")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
HISTORY_DIR = "storage/history"

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
