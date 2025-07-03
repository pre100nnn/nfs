def register_start_handlers(bot):
    @bot.message_handler(commands=['start'])
    async def start(message):
        await bot.reply_to(message, "Привет! Я бот. 🚀")