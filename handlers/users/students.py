from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from utils.api.students_req import student_registration

from loader import dp


@dp.message_handler(Command(commands="reg"))
async def bot_start(message: types.Message):
    user = message.from_user
    res = student_registration(user.id, first_name=user.first_name, last_name=user.last_name, username=user.username,
                               is_student=True)
    if res == 201:
        await message.answer(f"Вы зареганы, {user.full_name}!")
    elif res == -1:
        await message.answer(f"Вы уже в системе, {user.full_name}!")
    else:
        await message.answer(f"{user.full_name}, у нас проблемка №{res}, обратитесь к администратору!")

