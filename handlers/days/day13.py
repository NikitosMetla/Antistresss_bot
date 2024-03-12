import asyncio
from datetime import datetime, timedelta

from aiogram import types, Dispatcher, Router, F, Bot
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.users_stat import Users_stat
from settings import InputMessage
from utils.is_now_day import is_now_day

day_router13 = Router()


@day_router13.callback_query(Text(text="confirm|13"), any_state)
@is_now_day(13)
async def start_day13(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    if int(await Users_stat(message.from_user.id).get_user_day()) == int(message.data.split("|")[1]):
        await state.clear()
        await message.message.answer("Возможно, ты заметил какую-то закономерность и, например, на схожие стрессоры реагируешь "
                                     "аналогичной последовательностью действий. Возможно, во всех ситуациях твое поведение разнилось. "
                                     "У каждого из нас свой репертуар стратегий — чем он богаче, тем больше шансов эффективно решить проблему\n\n"
                                     "Давай посмотрим на то, какие стратегии вообще бывают. "
                                     "Американские психологи Р.Лазарус и С.Фолкман выделяют 8 стратегий:\n"
                                     "1. Конфронтация\n2. Дистанцирование\n3. Самоконтроль\n4. Поиск социальной поддержки\n"
                                     "5. Принятие ответственности\n6. Бегство-избегание\n7. Планирование решения проблемы\n"
                                     "8. Положительная переоценка\n\n"
                                     "Мы придерживаемся идеи, что нет эффективных или неэффективных стратегий как таковых. Одна и та же "
                                     "стратегия в разных ситуациях приведёт к разным последствиям. Посмотри на эти стратегии и попробуй соотнести "
                                     "их с теми, которые ты отследил у себя за прошлую неделю. Какие стратегии использовал?")
        await state.set_state(InputMessage.input_answer_state13_1)


@day_router13.message(F.text, InputMessage.input_answer_state13_1)
@is_now_day(13)
async def answer_day13_1(message: types.Message, state: FSMContext, bot: Bot):
    await message.answer("А к каким, как тебе кажется, прибегаешь чаще всего?")
    await state.set_state(InputMessage.input_answer_state13_2)


@day_router13.message(F.text, InputMessage.input_answer_state13_2)
@is_now_day(13)
async def answer_day13_2(message: types.Message, state: FSMContext, bot: Bot):
    await message.answer("А какие, наоборот, не используешь или используешь крайне редко?")
    await state.set_state(InputMessage.input_answer_state13_3)


@day_router13.message(F.text, InputMessage.input_answer_state13_3)
@is_now_day(13)
async def answer_day13_3(message: types.Message, state: FSMContext, bot: Bot):
    await message.answer("Какие стратегии ты бы хотел использовать чаще?")
    await state.set_state(InputMessage.input_answer_state13_4)


@day_router13.message(F.text, InputMessage.input_answer_state13_4)
@is_now_day(13)
async def answer_day13_4(message: types.Message, state: FSMContext, bot: Bot):
    await message.answer("Хорошо!\n"
                         "Можно заметить, что все стратегии направлены на 2 фокуса: на проблему и возникающие в связи с ней эмоции. "
                         "Может показаться, что важны только стратегии, направленные непосредственно на решение проблемы. "
                         "Но! Большое и важное но: в ситуации, когда человек испытывает сильные эмоции, даже если он в состоянии взяться за "
                         "решение проблемы (что бывает далеко не всегда), он, вероятнее всего, будет принимать не совсем адекватные решения. "
                         "Если он в моменте может взять под контроль эмоции и спрятать их поглубже (и так там их и оставить, не прожив их), "
                         "они потом сами всплывут (вероятнее всего в самый неподходящий момент, конечно). "
                         "Поэтому важно работать со стрессом в двух направлениях: и в проблемном, и в эмоциональном поле. Об этом будем говорить дальше) "
                         "Хорошего дня 👐")
    await state.clear()
    user = Users_stat(message.from_user.id)
    await user.edit_user_end_day()
