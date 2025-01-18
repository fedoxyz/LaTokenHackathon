import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
IS_DEBUG = os.getenv("DEBUG")
API_HOST = os.getenv("API_HOST")

