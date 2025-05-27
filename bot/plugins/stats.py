from pyrogram import Client, filters
from pyrogram.types import Message
from database.users import get_user_count
from database.files import get_file_count

@Client.on_message(filters.command("stats") & filters.user(Config.ADMINS))
async def stats_handler(client, message: Message):
    user_count = await get_user_count()
    file_count = await get_file_count()
    await message.reply_text(f"**Bot Stats:**\nUsers: {user_count}\nFiles Indexed: {file_count}"
