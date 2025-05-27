from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_buttons(files):
    buttons = []
    for file in files:
        buttons.append([InlineKeyboardButton(f"{file['file_name']} ({file['file_size']})", url=file['file_url'])])
    return InlineKeyboardMarkup(buttons)
