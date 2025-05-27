import asyncio
from pyrogram import Client, idle
from config import Config
from bot.handlers import start  # if this auto-loads handlers

Bot = Client(
    "AdvancedFilterBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins={"root": "bot/handlers"}  # or Config.PLUGINS if added
)

async def main():
    await Bot.start()
    print("Bot is running...")
    await idle()
    await Bot.stop()

if __name__ == "__main__":
    asyncio.run(main())