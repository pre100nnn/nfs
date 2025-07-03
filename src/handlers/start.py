from src.dao.models import AsyncSessionLocal, User


def register_start_handlers(bot):
    @bot.message_handler(commands=['start'])
    async def start(message):
        async with AsyncSessionLocal() as session:
            user = await session.get(User, message.from_user.id)
            if not user:
                user = User(
                    telegram_id=message.from_user.id,
                    username=message.from_user.username,
                    first_name=message.from_user.first_name,
                    last_name=message.from_user.last_name,
                )
                session.add(user)
                await session.commit()
                await bot.reply_to(message, "Welcome, вы зарегестрированы.😎")
            else:
                await bot.reply_to(message, "С возращением 🤗")
