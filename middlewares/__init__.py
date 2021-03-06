from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .students import GetUser


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(GetUser())