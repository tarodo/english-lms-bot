from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from states import WordSetState
from utils.api.wordset_req import wordset_create, wordsets

from keyboards.inline.wordset_buttons import wordsets_inline
from keyboards.inline.callback_datas import wordset_pages
from loader import dp


class MessageGenerator:
    def __init__(self, lang: str = 'ru'):
        self.lang = lang
        self.messages_ru = {
            'create_wordset': 'Введите название нового Сэта слов:',
            'wordset_show:pos': 'Вот сколько у вас всего:\n{}',
            'wordset_show:neg': 'У вас пока нет сетов слов. Чтобы создать, введите /newset',
            'wordset_new_name:pos': 'Создан новый Сэт: "{}"',
            'wordset_new_name:neg': '{}, у нас проблемка №{}, обратитесь к администратору!',
        }
        self.messages = {
            'ru': self.messages_ru
        }

    def create_wordset(self):
        return self.messages[self.lang]['create_wordset']

    def wordset_show_pos(self, *args):
        return self.messages[self.lang]['wordset_show:pos'].format(*args)

    def wordset_show_neg(self):
        return self.messages[self.lang]['wordset_show:neg']

    def wordset_new_name_pos(self, *args):
        return self.messages[self.lang]['wordset_new_name:pos'].format(*args)

    def wordset_new_name_neg(self, *args):
        return self.messages[self.lang]['wordset_new_name:neg'].format(*args)


message_gen = MessageGenerator()


@dp.message_handler(Command("newset"))
async def create_wordset(message: types.Message):
    await message.answer(message_gen.create_wordset())
    await WordSetState.Create.set()


@dp.message_handler(Command("sets"))
async def wordset_show(message: types.Message, student_id: int):
    sets = wordsets(student_id)
    if len(sets.sets) > 0:
        await message.answer(
            text=message_gen.wordset_show_pos(sets.page(1)[0].tg_message()),
            reply_markup=wordsets_inline(sets)
        )
    else:
        await message.answer(message_gen.wordset_show_neg())


@dp.callback_query_handler(wordset_pages.filter())
async def wordset_move_page(call: CallbackQuery, callback_data: dict, student_id: int):
    await call.answer()
    sets = wordsets(student_id)
    new_page = int(callback_data.get('page'))
    await call.message.edit_text(
        text=message_gen.wordset_show_pos(sets.page(new_page)[0].tg_message()),
        reply_markup=wordsets_inline(sets, page=new_page)
    )


@dp.message_handler(state=WordSetState.Create)
async def wordset_new_name(message: types.Message, student_id: int, state: FSMContext):
    user = message.from_user
    new_name = message.text
    res = wordset_create(new_name, student_id=student_id)
    if res == 201:
        await message.answer(message_gen.wordset_new_name_pos(new_name))
        await state.reset_state()
    else:
        await message.answer(message_gen.wordset_new_name_pos(user.full_name, res))
