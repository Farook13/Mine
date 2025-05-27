from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("help") & filters.private)
async def help_command(client, message: Message):
    await message.reply_text(
        "**Help Menu**\n\n"
        "/start - Show welcome message\n"
        "Search any movie/file by sending a query\n"
        "/stats - Show bot statistics\n"
        "/broadcast - Broadcast message to all users (admin only)"
    )
