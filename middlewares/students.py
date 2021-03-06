from aiogram import types, Dispatcher
from aiogram.dispatcher.middlewares import BaseMiddleware

from loader import storage
from utils.api.students_req import is_student_exists


REDIS_STUDENT_ID_PREFIX = 'students:user_id:'


class GetUser(BaseMiddleware):

    async def on_process_message(self, message: types.Message, data: dict):
        redis = await storage.redis()
        tg_id = message.from_user.id
        db_id = await redis.get(REDIS_STUDENT_ID_PREFIX + str(tg_id))
        if db_id is None:
            db_id = is_student_exists(tg_id)
            await redis.set(REDIS_STUDENT_ID_PREFIX + str(tg_id), db_id)
        else:
            db_id = int(db_id)
        data['student_id'] = db_id
