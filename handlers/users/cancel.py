from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from loader import dp


@dp.message_handler(Command(commands="cancel"), state='*')
async def new_student(message: types.Message, state: FSMContext):
    await message.answer('Вы все отменили')
    await state.reset_state()
