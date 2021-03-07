from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from states import WordSetState
from utils.api.wordset_req import wordset_create, wordsets

from keyboards.inline.wordset_buttons import wordsets_inline
from loader import dp
from aiogram import types


@dp.message_handler(Command("newset"))
async def create_wordset(message: types.Message):
    await message.answer('Введите название нового Сэта слов:')
    await WordSetState.Create.set()


@dp.message_handler(Command("sets"))
async def wordset_show(message: types.Message, student_id: int):
    sets = wordsets(student_id)
    if len(sets.sets) > 0:
        await message.answer(
            text='Вот сколько у вас всего:',
            reply_markup=wordsets_inline(sets)
        )
    else:
        await message.answer('У вас пока нет сетов слов. Чтобы создать, введите /newset')


@dp.message_handler(state=WordSetState.Create)
async def wordsset_set_newname(message: types.Message, student_id: int, state: FSMContext):
    user = message.from_user
    new_name = message.text
    res = wordset_create(new_name, student_id=student_id)
    if res == 201:
        await message.answer(f'Создан новый Сэт: "{new_name}"')
        await state.reset_state()
    else:
        await message.answer(f"{user.full_name}, у нас проблемка №{res}, обратитесь к администратору!")