import os

class Config:
    API_ID = int(os.environ.get("API_ID", 12618934))
    API_HASH = os.environ.get("API_HASH", "49aacd0bc2f8924add29fb02e20c8a16")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7955983025:AAECeT09wQ9ptCDnJ42YmKjy7rMSv9k4eiw")
    MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://batman13:batman13@batman.sawvl.mongodb.net/?retryWrites=true&w=majority&appName=batman")
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "TelegramBot")

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100233236188))
    FORCE_SUB = os.environ.get("FORCE_SUB", None)  # Channel username or ID
    ADMINS = list(map(int, os.environ.get("ADMINS", "5032034594").split()))

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
