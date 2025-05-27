from pyrogram import Client, filters
from pyrogram.types import Message
from database.files import add_file

@Client.on_message(filters.document | filters.video | filters.audio)
async def index_files(client, message: Message):
    media = message.document or message.video or message.audio
    await add_file(media, message.caption)
    await message.reply_text("File indexed successfully!")
