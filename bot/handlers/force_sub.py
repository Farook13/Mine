from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config

@Client.on_message(filters.private & ~filters.command(["start", "help"]))
async def check_force_sub(client, message: Message):
    try:
        user = await client.get_chat_member(Config.FORCE_SUB_CHANNEL, message.from_user.id)
        if user.status not in ["member", "administrator", "creator"]:
            raise Exception()
    except:
        await message.reply_text(
            "You need to join the channel before using this bot.",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Join Channel", url=f"https://t.me/{Config.FORCE_SUB_CHANNEL}")]]
            )
        )
        return 
