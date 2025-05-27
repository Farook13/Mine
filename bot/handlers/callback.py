from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

@Client.on_callback_query(filters.regex("help"))
async def help_cb(client, callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        "**Help Menu**\n\nSend a movie or file name to search.\nUse /start to restart.",
        reply_markup=callback_query.message.reply_markup
