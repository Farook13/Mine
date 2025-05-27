from pyrogram import Client, filters
from pyrogram.types import Message
from database.files import search_files
from bot.utils import get_buttons

@Client.on_message(filters.text & ~filters.command(["start", "help"]))
async def search_file(client, message: Message):
    results = await search_files(message.text)
    if results:
        buttons = get_buttons(results)
        await message.reply_text(f"Results for: `{message.text}`", reply_markup=buttons)
    else:
        await message.reply_text("No results found."
