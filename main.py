# main.py

import asyncio
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, PLUGINS
from bot.handlers import start  # triggers on startup to load modules

Bot = Client(
    "AdvancedFilterBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": PLUGINS}
)

async def main():
    await Bot.start()
    print("Bot is running...")
    await idle()
    await Bot.stop()

if __name__ == "__main__":
    from pyrogram import idle
    asyncio.run(main())
