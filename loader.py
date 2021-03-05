from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = RedisStorage2(host=config.REDIS_HOST, port=config.REDIS_PORT, db=config.REDIS_DB,
                        pool_size=config.REDIS_POOL, prefix=config.REDIS_PREFIX)
dp = Dispatcher(bot, storage=storage)
