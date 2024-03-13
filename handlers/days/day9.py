import asyncio
from datetime import datetime, timedelta

from aiogram import types, Dispatcher, Router, F, Bot
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state

from db.answers import Answers
from db.users_stat import Users_stat
from settings import InputMessage
from utils.is_now_day import is_now_day

day_router9 = Router()


@day_router9.callback_query(Text(text="confirm|9"), any_state)
@is_now_day(9)
async def start_day9(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    if int(str(await Users_stat(message.from_user.id).get_user_day())) == int(message.data.split("|")[1]):
        now = datetime.now()
        target_time = datetime(now.year, now.month, now.day, 20, 34)
        if now >= target_time:
            target_time += timedelta(days=1)
        time_difference = target_time - now
        await asyncio.sleep(time_difference.total_seconds())
        question = await message.message.answer(text="Ну что, что заметил сегодня? Что вызывало напряжение?")
        await state.set_state(InputMessage.input_answer_state9_1)
        await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router9.message(F.text, InputMessage.input_answer_state9_1)
@is_now_day(9)
async def answer_day9_1(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("Какие мысли приходили?")
    await state.set_state(InputMessage.input_answer_state9_2)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router9.message(F.text, InputMessage.input_answer_state9_2)
@is_now_day(9)
async def answer_day9_2(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("А что было с телом?")
    await state.set_state(InputMessage.input_answer_state9_3)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router9.message(F.text, InputMessage.input_answer_state9_3)
@is_now_day(9)
async def answer_day9_3(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("Какие эмоции возникали?")
    await state.set_state(InputMessage.input_answer_state9_4)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router9.message(F.text, InputMessage.input_answer_state9_4)
@is_now_day(9)
async def answer_day9_4(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("И что ты при этом делал?")
    await state.set_state(InputMessage.input_answer_state9_5)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router9.message(F.text, InputMessage.input_answer_state9_5)
@is_now_day(9)
async def answer_day9_5(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    await message.answer("Ага, отлично! Будем работать с этим дальше 💪")
    await state.clear()
    user = Users_stat(message.from_user.id)
    await user.edit_user_end_day()
