async def start_bot(app):
    from bot.handlers import start, help, search, callback, force_sub, indexer
    import bot.plugins
    print("Bot modules loaded successfully.")
