import os

class Config:
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "your_api_hash")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token")
    MONGO_URI = os.environ.get("MONGO_URI", "your_mongo_uri")
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "TelegramBot")

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001234567890))
    FORCE_SUB = os.environ.get("FORCE_SUB", None)  # Channel username or ID
    ADMINS = list(map(int, os.environ.get("ADMINS", "123456789").split()))

    WELCOME_MESSAGE = os.environ.get("WELCOME_MESSAGE", "Welcome {mention}! Use me to get your files instantly.")
    FILE_CAPTION_TEMPLATE = os.environ.get(
        "FILE_CAPTION_TEMPLATE",
        "<b>📂 Filename:</b> {file_name}\n<b>📦 Size:</b> {file_size}"
    )
    MAX_RESULTS = int(os.environ.get("MAX_RESULTS", 10))
    START_BUTTONS = [
        ["Channel", "https://t.me/YourChannel"],
        ["Support Group", "https://t.me/YourGroup"]
    ]