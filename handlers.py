from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Siema!")

@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Twój ID: {msg.from_user.id}")
