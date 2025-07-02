import asyncio, os
from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv
from src import handlers # handlers

load_dotenv()

bot = AsyncTeleBot(os.getenv("NFS_BOT_TOKEN"))

if __name__ == '__main__':
    print('Бот успешно запущен')
    asyncio.run(bot.polling())