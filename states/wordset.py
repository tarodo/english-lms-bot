from aiogram.dispatcher.filters.state import StatesGroup, State


class WordSetState(StatesGroup):
    Create = State()
    Update = State()
    ChangeName = State()
    AddWord = State()