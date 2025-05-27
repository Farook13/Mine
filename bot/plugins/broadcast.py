from pyrogram import Client, filters
from pyrogram.types import Message
from database.users import get_all_users

@Client.on_message(filters.command("broadcast") & filters.user(Config.ADMINS))
async def broadcast_msg(client, message: Message):
    users = await get_all_users()
    success = fail = 0
    for user_id in users:
        try:
            await client.send_message(user_id, message.reply_to_message.text)
            success += 1
        except:
            fail += 1
    await message.reply_text(f"Broadcast complete.\nSuccess: {success} | Failed: {fail}"
