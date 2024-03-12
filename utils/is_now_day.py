import traceback
from functools import wraps

from aiogram.fsm.context import FSMContext

from aiogram import types, Bot

from db.admins import Admin
from db.users_stat import Users_stat


def is_now_day(day: int):
    def decorator(func):
        @wraps(func)
        async def wrapper(message: types.Message | types.CallbackQuery, state: FSMContext, bot: Bot | None, **kwargs):
            # print("========================= " + func.__name__ + " ============================")
            try:
                if int(await Users_stat(message.from_user.id).get_user_day()) == day:
                    # print('Проверка на подписку пройдена')
                    return await func(message, state, bot, **kwargs)
                elif type(message) == types.Message:
                    await message.answer(f"Дорогой друг, продолжи, пожалуйста, с программы последнего дня")
                else:
                    await message.message.answer(f"Дорогой друг, продолжи, пожалуйста, с программы последнего дня")
            except Exception:
                print(traceback.format_exc())
            # finally:
            #     # print("========================= " + func.__name__ + " ============================")

        return wrapper
    return decorator
