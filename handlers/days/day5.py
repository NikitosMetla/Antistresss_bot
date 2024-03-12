import asyncio
from datetime import datetime, timedelta

from aiogram import types, Dispatcher, Router, F, Bot
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.users_stat import Users_stat
from settings import InputMessage, sticker_ids
from utils.is_now_day import is_now_day

day_router5 = Router()


@day_router5.callback_query(Text(text="confirm|5"), any_state)
@is_now_day(5)
async def start_day5(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    if int(await Users_stat(message.from_user.id).get_user_day()) == int(message.data.split("|")[1]):
        await state.clear()
        keyboard = InlineKeyboardBuilder()
        keyboard.row(InlineKeyboardButton(text="Договорились", callback_data="AGREED|5"))
        await message.message.answer("Для этого мы начнём углубляться в практику и следующую неделю посвятим наблюдению 👀 "
                                     "Но подглядывать мы за тобой не можем, поэтому тебе придётся самостоятельно наблюдать за собой"
                                     "Начнём с того, что сегодня в течение дня тебе нужно будет замечать, что у тебя вызывает "
                                     "напряжение (это могут быть какие-то незначительные комментарии коллег, разрядившийся телефон, "
                                     "новое задание по учёбе, в общем всё, что угодно) и ещё какие мысли в этот момент возникают. "
                                     "Заведи себе отдельную заметку в телефоне и записывай туда причины стресса + мысли 🙂 "
                                     "Важно подмечать даже незначительные, казалось бы, ситуации напряжения, так как их эффекты "
                                     "имеют свойство накапливаться и перерастают в хронический стресс (который по своим последствиям "
                                     "оказывается опаснее острого)\n\nВечером уточним, что у тебя получилось 👐 Ок?",
                                     reply_markup=keyboard.as_markup())


@day_router5.callback_query(Text(text="AGREED|5"))
@is_now_day(5)
async def agreed_day5(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    now = datetime.now()
    target_time = datetime(now.year, now.month, now.day, 20, 49)
    if now >= target_time:
        target_time += timedelta(days=1)
    time_difference = target_time - now
    await asyncio.sleep(time_difference.total_seconds())
    await message.message.answer(text="Как успехи? Удалось исследовать триггеры и мысли во время стресса?"
                                      " Что получилось? (Можешь скопировать сюда свою заметку или написать"
                                      " в более обобщенном виде)")
    await state.set_state(InputMessage.input_answer_state5_1)


@day_router5.message(F.text, InputMessage.input_answer_state5_1)
@is_now_day(5)
async def answer_remembered3(message: types.Message, state: FSMContext, bot: Bot):
    await message.answer_sticker(sticker=sticker_ids[1])
    await message.answer("Хорошо! Продолжим завтра)")
    await state.clear()
    user = Users_stat(message.from_user.id)
    await user.edit_user_end_day()
