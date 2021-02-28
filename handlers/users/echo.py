from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp


@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f"Эхо без состояния.\n"
                         f"Сообщение:"
                         f"{message.text}")

