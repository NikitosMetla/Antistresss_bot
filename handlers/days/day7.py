import asyncio
from datetime import datetime, timedelta

from aiogram import types, Dispatcher, Router, F, Bot
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.answers import Answers
from db.users_stat import Users_stat
from settings import InputMessage
from utils.is_now_day import is_now_day

day_router7 = Router()


@day_router7.callback_query(Text(text="confirm|7"), any_state)
@is_now_day(7)
async def start_day7(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.edit_reply_markup()
    await state.clear()
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Ок", callback_data="OK|7"))
    await message.message.answer("Помимо причин напряжения, мыслей и чувств в теле, которые возникают во время стресса, "
                                 "нужно будет подмечать ещё и эмоции. Если тебе будет сложно идентифицировать свои эмоции, "
                                 "можешь воспользоваться списком базовых эмоций, которые выделил американский психолог К.Изард:"
                                 "\n• Интерес\n• Радость\n• Удивление\n• Горе\n• Гнев\n• Отвращение\n• Презрение\n• Страх"
                                 "\n• Стыд\n• Вина\nНе забудь записывать всё в заметки 😉", reply_markup=keyboard.as_markup())


@day_router7.callback_query(Text(text="OK|7"))
@is_now_day(7)
async def ok_day7(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.edit_reply_markup()
    now = datetime.now()
    target_time = datetime(now.year, now.month, now.day, 20, 38)
    if now >= target_time:
        target_time += timedelta(days=1)
    time_difference = target_time - now
    await message.message.answer("Вечером вернемся с расспросами😄")
    await asyncio.sleep(time_difference.total_seconds())
    question = await message.message.answer(text="Ну что, как успехи? Что стало причиной стресса сегодня?")
    await state.set_state(InputMessage.input_answer_state7_1)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router7.message(F.text, InputMessage.input_answer_state7_1)
@is_now_day(7)
async def answer_day7_1(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("Какие мысли при этом возникали?")
    await state.set_state(InputMessage.input_answer_state7_2)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router7.message(F.text, InputMessage.input_answer_state7_2)
@is_now_day(7)
async def answer_day7_2(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("А что было с телом?")
    await state.set_state(InputMessage.input_answer_state7_3)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router7.message(F.text, InputMessage.input_answer_state7_3)
@is_now_day(7)
async def answer_day7_3(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("Какие эмоции возникали?")
    await state.set_state(InputMessage.input_answer_state7_4)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router7.message(F.text, InputMessage.input_answer_state7_4)
@is_now_day(7)
async def answer_day7_4(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    await message.answer("Ух, ничего себе! Вот это рефлексия)) То ли ещё будет 😄")
    await state.clear()
    user = Users_stat(message.from_user.id)
    await user.edit_user_end_day()
