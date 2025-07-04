import asyncio
from src.core import bot
from src.handlers import register_handlers

async def main():
    register_handlers(bot)  # Регистрация всех обработчиков
    await bot.polling(non_stop=True)

if __name__ == "__main__":
    print ('Бот запущен.')
    asyncio.run(main())
