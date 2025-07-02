from src.core import bot

def register_help_handlers(bot):
    @bot.message_handler(commands=['help'])
    async def help(message):
        await bot.reply_to(message, "Помоги мне)")