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

day_router8 = Router()


@day_router8.callback_query(Text(text="confirm|8"), any_state)
@is_now_day(8)
async def start_day8(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    if int(str(await Users_stat(message.from_user.id).get_user_day())) == int(message.data.split("|")[1]):
        now = datetime.now()
        target_time = datetime(now.year, now.month, now.day, 20, 35)
        if now >= target_time:
            target_time += timedelta(days=1)
        time_difference = target_time - now
        await message.message.answer("Вечером вернемся с расспросами😄")
        await asyncio.sleep(time_difference.total_seconds())
        question = await message.message.answer(text="Ну что, как успехи? Что стало причиной стресса сегодня?")
        await state.set_state(InputMessage.input_answer_state8_1)
        await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router8.message(F.text, InputMessage.input_answer_state8_1)
@is_now_day(8)
async def answer_day8_1(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("Какие мысли при этом возникали?")
    await state.set_state(InputMessage.input_answer_state8_2)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router8.message(F.text, InputMessage.input_answer_state8_2)
@is_now_day(8)
async def answer_day8_2(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("А что было с телом?")
    await state.set_state(InputMessage.input_answer_state8_3)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router8.message(F.text, InputMessage.input_answer_state8_3)
@is_now_day(8)
async def answer_day8_3(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("Какие эмоции были?")
    await state.set_state(InputMessage.input_answer_state8_4)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router8.message(F.text, InputMessage.input_answer_state8_4)
@is_now_day(8)
async def answer_day8_4(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("А что ты делал в этой ситуации (или в этих ситуациях, если их было несколько)?")
    await state.set_state(InputMessage.input_answer_state8_5)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router8.message(F.text, InputMessage.input_answer_state8_5)
@is_now_day(8)
async def answer_day8_5(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    await message.answer("Супер! Ты славно потрудился сегодня, рассчитываем, что и отдохнешь не хуже 👐\n\nДавай ещё быстренько посмотрим, что у тебя с состоянием")
    await state.clear()
    await start_LLIC(message, state, bot)
