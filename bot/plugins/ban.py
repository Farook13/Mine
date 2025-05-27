from pyrogram import Client, filters
from pyrogram.types import Message
from database.users import ban_user

@Client.on_message(filters.command("ban") & filters.user(Config.ADMINS))
async def ban_command(client, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a user to ban.")
    user_id = message.reply_to_message.from_user.id
    await ban_user(user_id)
    await message.reply_text(f"Banned {user_id}"
