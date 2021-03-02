from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from states import WordSetState
from utils.api.wordset_req import wordset_create

from loader import dp
from aiogram import types


@dp.message_handler(Command("newset"))
async def create_wordset(message: types.Message):
    await message.answer('Введите название нового Сэта слов:')
    await WordSetState.Create.set()


@dp.message_handler(state=WordSetState.Create)
async def wordsset_set_newname(message: types.Message):
    user = message.from_user
    new_name = message.text
    res = wordset_create(new_name)
    if res == 201:
        await message.answer(f'Создан новый Сэт: "{new_name}"')
    else:
        await message.answer(f"{user.full_name}, у нас проблемка №{res}, обратитесь к администратору!")