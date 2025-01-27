from aiogram import types

from keyboards.inline import admin_kb
from config import Admin_Id

#admin paneli kamandasi
async def admin_command(message: types.Message):
    if message.from_user.id == Admin_Id:
        await message.answer("Admin panel",reply_markup=admin_kb)
    else:
        await message.answer("Bot admini va dasturchisi: @Nufada")

