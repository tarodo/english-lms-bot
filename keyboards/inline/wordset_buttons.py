from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.api.wordset_req import WordSetList, WordSet
from .callback_datas import wordset_callback, wordset_pages


def wordsets_inline(wordset_list: WordSetList, page: int = 1):
    if wordset_list.pages() < page:
        return None
    keyboard = InlineKeyboardMarkup(row_width=wordset_list.page_step)
    one_page, prev_page, next_page = wordset_list.page(page)
    if prev_page > 0:
        keyboard.insert(
            InlineKeyboardButton(
                text='<<<',
                callback_data=wordset_pages.new(prev_page)
            )
        )
    if next_page > 0:
        keyboard.insert(
            InlineKeyboardButton(
                text='>>>',
                callback_data=wordset_pages.new(next_page)
            )
        )

    keyboard.row()
    print(one_page.sets)
    for wset in one_page.sets:
        keyboard.insert(InlineKeyboardButton(
                text=wset.name,
                callback_data=wordset_callback.new(wset.id)))

    return keyboard
