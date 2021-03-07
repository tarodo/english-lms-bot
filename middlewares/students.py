from aiogram import types, Dispatcher
from aiogram.dispatcher.middlewares import BaseMiddleware

from loader import storage
from utils.api.students_req import student_id


REDIS_STUDENT_ID_PREFIX = 'students:user_id:'


class GetUser(BaseMiddleware):

    async def add_student_id(self, tg_id: int) -> int:
        redis = await storage.redis()
        db_id = await redis.get(REDIS_STUDENT_ID_PREFIX + str(tg_id))
        if db_id is None:
            db_id = student_id(tg_id)
            await redis.set(REDIS_STUDENT_ID_PREFIX + str(tg_id), db_id)
        else:
            db_id = int(db_id)
        return db_id

    async def on_process_message(self, message: types.Message, data: dict):
        data['student_id'] = await self.add_student_id(message.from_user.id)

    async def on_process_callback_query(self, message: types.Message, data: dict):
        data['student_id'] = await self.add_student_id(message.from_user.id)
