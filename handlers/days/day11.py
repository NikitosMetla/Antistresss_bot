import asyncio
from datetime import datetime, timedelta

from aiogram import types, Dispatcher, Router, F, Bot
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state

from db.users_stat import Users_stat
from handlers.user_handlers import start_statement_next_days
from settings import InputMessage
from utils.is_now_day import is_now_day

day_router11 = Router()


@day_router11.callback_query(Text(text="confirm|11"), any_state)
@is_now_day(11)
async def start_day11(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    if int(await Users_stat(message.from_user.id).get_user_day()) == int(message.data.split("|")[1]):
        now = datetime.now()
        target_time = datetime(now.year, now.month, now.day, 20, 29)
        if now >= target_time:
            target_time += timedelta(days=1)
        time_difference = target_time - now
        await asyncio.sleep(time_difference.total_seconds())
        await message.message.answer(
            text="Итак, пройдёмся по вопросам в последний раз. Какие причины стресса удалось сегодня отметить?")
        await state.set_state(InputMessage.input_answer_state11_1)


@day_router11.message(F.text, InputMessage.input_answer_state11_1)
@is_now_day(11)
async def answer_day11_1(message: types.Message, state: FSMContext, bot: Bot):
    await message.answer("Какие мысли приходили?")
    await state.set_state(InputMessage.input_answer_state11_2)


@day_router11.message(F.text, InputMessage.input_answer_state11_2)
@is_now_day(11)
async def answer_day11_2(message: types.Message, state: FSMContext, bot: Bot):
    await message.answer("Что было с телом?")
    await state.set_state(InputMessage.input_answer_state11_3)


@day_router11.message(F.text, InputMessage.input_answer_state11_3)
@is_now_day(11)
async def answer_day11_3(message: types.Message, state: FSMContext, bot: Bot):
    await message.answer("Какие эмоции возникали?")
    await state.set_state(InputMessage.input_answer_state11_4)


@day_router11.message(F.text, InputMessage.input_answer_state11_4)
@is_now_day(11)
async def answer_day11_4(message: types.Message, state: FSMContext, bot: Bot):
    await message.answer("И что ты при этом делал?")
    await state.set_state(InputMessage.input_answer_state11_5)


@day_router11.message(F.text, InputMessage.input_answer_state11_5)
@is_now_day(11)
async def answer_day11_5(message: types.Message, state: FSMContext, bot: Bot):
    await message.answer("Отлично! Завтра будем двигаться дальше😉\n"
                         "Давай ещё посмотрим, что у тебя с рабочим состоянием")
    await state.clear()
    await start_statement_next_days(message, state, bot)
