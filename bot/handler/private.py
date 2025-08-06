import os
import django
from aiogram import Router, F, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import CommandStart, Command
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    FSInputFile,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from asgiref.sync import sync_to_async

from ..settings.buttons import *
from datetime import datetime
import logging
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

user_private_router = Router()
dp = user_private_router

@dp.message(CommandStart())
async def StartCommand(message: Message):
    await message.answer(f"<b>Salom, {message.from_user.full_name}")
