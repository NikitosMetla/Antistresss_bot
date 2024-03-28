import asyncio
from datetime import datetime, timedelta

from aiogram import types, Router, F, Bot
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.answers import Answers
from db.users_stat import Users_stat
from handlers.user_handlers import start_LLIC
from settings import InputMessage
from utils.is_now_day import is_now_day

day_router6 = Router()

@day_router6.callback_query(Text(text="confirm|6"), any_state)
@is_now_day(6)
async def start_day6(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.edit_reply_markup()
    await state.clear()
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Оки-доки", callback_data="OKI_DOKI|6"))
    await message.message.answer("Сегодня мы усложним задачу: нужно будет замечать и записывать причины напряжения, "
                                 "мысли и (барабанная дробь) ощущения в теле (помнишь, мы говорили про то, что стресс "
                                 "по-разному проявляется на физиологическом уровне?) Вечером уточним, что тебе удалось заметить 😉", reply_markup=keyboard.as_markup())


@day_router6.callback_query(Text(text="OKI_DOKI|6"))
@is_now_day(6)
async def oki_doki_day6(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.edit_reply_markup()
    await message.message.answer("Отлично, договорились)")
    now = datetime.now()
    target_time = datetime(now.year, now.month, now.day, 20, 41)
    if now >= target_time:
        target_time += timedelta(days=1)
    time_difference = target_time - now
    await asyncio.sleep(time_difference.total_seconds())
    question = await message.message.answer("Ну что, как успехи? Что стало источником стресса сегодня?")
    await state.set_state(InputMessage.input_answer_state6_1)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router6.message(F.text, InputMessage.input_answer_state6_1)
@is_now_day(6)
async def answer_day6_1(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("Какие мысли при этом возникали? (Если стрессовых ситуаций было несколько, "
                         "пиши для каждой отдельно, но в одном сообщении)")
    await state.set_state(InputMessage.input_answer_state6_2)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router6.message(F.text, InputMessage.input_answer_state6_2)
@is_now_day(6)
async def answer_day6_2(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("А что было с телом?")
    await state.set_state(InputMessage.input_answer_state6_3)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router6.message(F.text, InputMessage.input_answer_state6_3)
@is_now_day(6)
async def answer_day6_3(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    await message.answer("Хорошая работа 🙂 Так держать!\n\nДавай ещё быстренько посмотрим, что у тебя с состоянием")
    await state.clear()
    user = Users_stat(message.from_user.id)
    await start_LLIC(message, state, bot)
