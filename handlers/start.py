from aiogram.types import Message
from aiogram import types

from utils import referral
from keyboards.reply import start_kb

async def start_command(message: Message):
    from main import logging
    await message.answer("Hush kelibsiz!",reply_markup=start_kb())
    try:
        args = message.text.split()[1:]
        if args:
            referral.register_user(message.from_user.id, args)
            referral.add_point(args, 1)
        else:
            referral.register_user(message.from_user.id)
    except Exception as e:
        logging.error(f"Start kamandasida xatolik: {e}")


    


