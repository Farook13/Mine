from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from config import Config

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client, message: Message):
    buttons = [
        [InlineKeyboardButton("Join Channel", url=f"https://t.me/{Config.FORCE_SUB_CHANNEL}")],
        [InlineKeyboardButton("Group", url="https://t.me/YourGroup")],
        [InlineKeyboardButton("Help", callback_data="help")]
    ]
    await message.reply_photo(
        photo=Config.START_PIC or "https://telegra.ph/file/6c2d8c33f24c7fc83b3d9.jpg",
        caption=f"Hello {message.from_user.mention}, welcome to the fastest AutoFilter bot!",
        reply_markup=InlineKeyboardMarkup(buttons)
    
