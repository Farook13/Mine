# config.py

import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
DB_URI = os.getenv("DB_URI")  # MongoDB connection
DB_NAME = os.getenv("DB_NAME", "autofilter")
FORCE_SUB_CHANNEL = int(os.getenv("FORCE_SUB_CHANNEL", 0))
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", 0))
ADMINS = [int(i) for i in os.getenv("ADMINS", "").split()]
PLUGINS = "bot/handlers"
