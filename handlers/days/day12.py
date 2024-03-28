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
from settings import InputMessage, sticker_ids
from utils.is_now_day import is_now_day

day_router12 = Router()


@day_router12.callback_query(Text(text="confirm|12"), any_state)
@is_now_day(12)
async def start_day12(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.edit_reply_markup()
    await state.clear()
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Окей, сделаю", callback_data="OKAY_DO|12"))
    await message.message.answer("Создай где-нибудь табличку, состоящую из 5 колонок — источник стресса, мысли, ощущения в теле, эмоции и поведение во время стрессовой ситуации. Перенеси туда свои наблюдения. Если какие-то причины напряжения повторялись или схожи по своей сути, можешь объединить их в группу. После попробуй проследить похожие паттерны по любому признаку: будь то одна и та же эмоция или одинаковый способ реакции на стресс-фактор. Возможно, в твоей учебной или профессиональной деятельности одна неделя кардинально отличается от другой и, соответственно, данных одной недели будет казаться недостаточно. Как бы то ни было, мы рекомендуем и дальше наблюдать за причинами стресса и их реакциями, а уже завтра мы поделимся, что с ними делать дальше👐", reply_markup=keyboard.as_markup())


@day_router12.callback_query(Text(text="OKAY_DO|12"), any_state)
@is_now_day(12)
async def start_day12(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.edit_reply_markup()
    now = datetime.now()
    target_time = datetime(now.year, now.month, now.day, 21, 0)
    if now >= target_time:
        target_time += timedelta(days=1)
    time_difference = target_time - now
    await message.message.answer("Вечером вернемся с расспросами😄")
    await asyncio.sleep(time_difference.total_seconds())
    question = await message.message.answer("Что удалось заметить?")
    await state.set_state(InputMessage.input_answer_state12_2)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router12.message(F.text, InputMessage.input_answer_state12_2)
@is_now_day(12)
async def answer_day11_5(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    await state.clear()
    await message.answer_sticker(sticker=sticker_ids[-1])
    await start_LLIC(message, state, bot)
    # await message.answer_sticker()


