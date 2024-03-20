import asyncio
from datetime import datetime, timedelta

from aiogram import types, Dispatcher, Router, F, Bot
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.answers import Answers
from db.users_stat import Users_stat
from handlers.user_handlers import start_LLIC
from settings import InputMessage, sticker_ids
from utils.is_now_day import is_now_day

day_router15 = Router()


@day_router15.callback_query(Text(text="confirm|15"), any_state)
@is_now_day(15)
async def start_day15(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.answer("Вечером вернемся с расспросами😄")
    await state.clear()
    question = await message.message.answer("Поговорим о процессуальной стороне твоей деятельности. Задумывался ли ты когда-нибудь о том, как можешь облегчить свою работу? "
                                 "Кажется, что все люди с удовольствием делали бы меньше, но на самом деле большая часть людей выполняет задачи так, как они привыкли это делать, "
                                 "как научились или как кто-то их научил. Мало того, что сформировавшиеся паттерны поведения не всегда бывают эффективными, технологии развиваются так быстро, "
                                 "что буквально каждый день появляются новые инструменты, которые могли бы оптимизировать и твою деятельность. "
                                 "Процесс анализа и коррекции стиля выполнения работы занимает какое-то время, но если это проделать с задачами, отнимающими много времени и сил, это окупится сполна. "
                                 "Какую часть из своей работы ты бы хотел <b>оптимизировать?</b>")
    await state.set_state(InputMessage.input_answer_state15_1)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router15.message(F.text, InputMessage.input_answer_state15_1)
@is_now_day(15)
async def answer_day15_1(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("Как ты мог бы это сделать?")
    await state.set_state(InputMessage.input_answer_state15_2)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router15.message(F.text, InputMessage.input_answer_state15_2)
@is_now_day(15)
async def answer_day15_2(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    keyboard = InlineKeyboardBuilder()
    await state.clear()
    keyboard.row(InlineKeyboardButton(text="Да, думаю, они могут что-то подсказать", callback_data="Discussion|15"))
    keyboard.row(InlineKeyboardButton(text="Нет, сам знаю, что надо делать", callback_data="Discussion|15"))
    await message.answer(
        "Хочешь ли ты обсудить это с коллегами или руководством, чтобы услышать их мнение и, может быть, узнать про альтернативные варианты?", reply_markup=keyboard.as_markup())


@day_router15.callback_query(Text(text="Discussion|15"))
@is_now_day(15)
async def discussion_day15(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Да, так я смогу оптимизировать свою работу", callback_data="Training|15"))
    keyboard.row(InlineKeyboardButton(text="Нет, сам справлюсь", callback_data="Training|15"))
    await message.message.answer("Нужно ли тебе пройти обучение для освоения каких-то инструментов?", reply_markup=keyboard.as_markup())


@day_router15.callback_query(Text(text="Training|15"))
@is_now_day(15)
async def training_day15(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await state.clear()
    await message.message.answer_sticker(sticker=sticker_ids[-7])
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Поставил напоминание", callback_data="Reminder|15"))
    await message.message.answer("Отлично! Допустим, ты оптимизировал процесс выполнения основных задач, что ещё тебе может помочь? "
                                 "<b>Рациональное чередование заданий и форм активной занятости</b>\n"
                                 "Все мы устаем от однообразной работы, кто-то быстрее, кто-то медленнее, после чего выполняем задачи, напрягаясь ещё сильнее. "
                                 "Чтобы этого избежать, необходимо понаблюдать за собой и зафиксировать, в какой момент наступает утомление от определенной деятельности и возникает желание её сменить. "
                                 "Даже внутри одной задачи зачастую можно выделить различные формы активности, а следовательно и периодически их менять. "
                                 "Когда ты станешь понимать, через какой промежуток времени рационально сменять каждую из задач, учитывай этот аспект при составлении графика работы и учебы 😉",
                                 reply_markup=keyboard.as_markup())


@day_router15.callback_query(Text(text="Reminder|15"))
@is_now_day(15)
async def reminder_day15(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Буду балансировать😌", callback_data="Balance|15"))
    await message.message.answer("Хорошо) Последний пункт на сегодня — <b>сбалансированность режимов труда и отдыха</b>. "
                                 "Если время твоей работы и перерывов не фиксировано, проследи, оптимально ли ты распределяешь нагрузку в течение рабочего дня или необходимо где-то добавить перерывы, "
                                 "пораньше заканчивать или в целом в течение недели больше времени отводить на отдых. "
                                 "Не забывай, что отдых необходим для восстановления твоих ресурсов, а работа на износ приводит к истощению 😢 "
                                 "Ведь если ты не будешь заботиться о своем здоровье, то кто будет?", reply_markup=keyboard.as_markup())


@day_router15.callback_query(Text(text="Balance|15"))
@is_now_day(15)
async def balance_day15(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await Users_stat(message.from_user.id).edit_user_end_day()
    await message.message.answer("На сегодня все👐")
