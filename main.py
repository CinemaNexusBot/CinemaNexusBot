from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import logging
import os

# Вставь сюда токен своего бота от @BotFather
BOT_TOKEN = os.getenv("BOT_TOKEN") or "вставь_сюда_токен"

# Включаем логирование (для отладки)
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Хендлер на /start
@dp.message_handler(commands=["start"])
async def start_handler(message: Message):
    await message.answer("👋 Привет! Я CinemaNexusBot. Отправь название фильма, и я помогу тебе его найти!")

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
