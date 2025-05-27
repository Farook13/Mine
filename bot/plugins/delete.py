from pyrogram import Client, filters
from database.files import delete_file

@Client.on_message(filters.command("delete") & filters.user(Config.ADMINS))
async def delete_command(client, message: Message):
    query = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else None
    if not query:
        return await message.reply_text("Provide a query to delete.")
    count = await delete_file(query)
    await message.reply_text(f"Deleted {count} entries for `{query}`")
