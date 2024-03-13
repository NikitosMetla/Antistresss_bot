import asyncio
from datetime import datetime, timedelta

from aiogram import types, Dispatcher, Router, F, Bot
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state

from db.answers import Answers
from db.users_stat import Users_stat
from handlers.user_handlers import start_LLIC
from settings import InputMessage
from utils.is_now_day import is_now_day

day_router10 = Router()


@day_router10.callback_query(Text(text="confirm|10"), any_state)
@is_now_day(10)
async def start_day10(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    if int(await Users_stat(message.from_user.id).get_user_day()) == int(message.data.split("|")[1]):
        now = datetime.now()
        target_time = datetime(now.year, now.month, now.day, 20, 31)
        if now >= target_time:
            target_time += timedelta(days=1)
        time_difference = target_time - now
        await message.message.answer("Вечером вернемся с расспросами😉")
        await asyncio.sleep(time_difference.total_seconds())
        question = await message.message.answer(text="Пройдемся по отработанной схеме? Какие причины стресса удалось выделить?")
        await state.set_state(InputMessage.input_answer_state10_1)
        await state.update_data(question=question.text)


@day_router10.message(F.text, InputMessage.input_answer_state10_1)
@is_now_day(10)
async def answer_day10_1(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("Какие мысли приходили?")
    await state.set_state(InputMessage.input_answer_state10_2)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + question.text)


@day_router10.message(F.text, InputMessage.input_answer_state10_2)
@is_now_day(10)
async def answer_day10_2(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("А что было с телом?")
    await state.set_state(InputMessage.input_answer_state10_3)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + question.text)


@day_router10.message(F.text, InputMessage.input_answer_state10_3)
@is_now_day(10)
async def answer_day10_3(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    await message.answer("Какие эмоции возникали?")
    await state.set_state(InputMessage.input_answer_state10_4)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router10.message(F.text, InputMessage.input_answer_state10_4)
@is_now_day(10)
async def answer_day10_4(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("Что ты при этом делал?")
    await state.set_state(InputMessage.input_answer_state10_5)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router10.message(F.text, InputMessage.input_answer_state10_5)
@is_now_day(10)
async def answer_day10_5(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    await message.answer("Хорошая работа была проделана! Завтра завершающий день недели наблюдения 👀")
    await state.clear()
    await start_LLIC(message, state, bot)
