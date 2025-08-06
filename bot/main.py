import sys
import asyncio
import logging

from aiogram import Bot, Dispatcher
from core.settings import BOT_TOKEN
from aiogram.client.bot import DefaultBotProperties
from bot.handler.private import user_private_router

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

dp.include_router(user_private_router)


async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await dp.start_polling(bot)