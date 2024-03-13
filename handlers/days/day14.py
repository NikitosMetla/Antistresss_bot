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

day_router14 = Router()


@day_router14.callback_query(Text(text="confirm|14"), any_state)
@is_now_day(14)
async def start_day14(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    if int(await Users_stat(message.from_user.id).get_user_day()) == int(message.data.split("|")[1]):
        await state.clear()
        await message.message.answer("Очень простые и где-то даже тривиальные вещи, к которым мы зачастую относимся несерьезно. На прошлой неделе ты занимался тем, что обращал "
                                     "внимание на то, что у тебя вызывает напряжение. Посмотри, можешь ли избавиться от этих стресс-факторов или минимизировать их? Не отмахивайся от этого вопроса. "
                                     "Посмотри внимательно. Попробуй быть креативным. Может быть тебе не обязательно встречаться/созваниваться с раздражающим тебя коллегой и можно договориться "
                                     "взаимодействовать в другом формате, например, подробно расписывать что-либо\n"
                                     "Может дойти даже до совсем примитивного: тебя раздражает сломанный ремень на любимом рюкзаке и ты терпишь, потому что не хочешь его менять. "
                                     "Может можно найти в интернет-магазине сломанную деталь и заменить её? Это ведь не займёт много времени\n"
                                     "Выпиши сейчас причины напряжения и то, какие шаги ты предпримешь, чтобы убрать/минимизировать их:")
        await state.set_state(InputMessage.input_answer_state14_1)


@day_router14.message(F.text, InputMessage.input_answer_state14_1)
@is_now_day(14)
async def answer_day14_1(message: types.Message, state: FSMContext, bot: Bot):
    await message.answer_sticker(sticker=sticker_ids[0])
    await message.answer("Отлично! Так их))\n\n"
                         "Следующим пунктом, самым банальным из банальных, но крайне важным, является налаженные питьевой режим и режим питания. "
                         "Убегаешь с утра не позавтракав? Пропускаешь обед или ужин, вместо этого жуя сэндвич по дороге? "
                         "Отмахиваешься от жажды из-за того, что всё время забываешь купить воды с собой в университет? Поставь напоминание. "
                         "Выдели “священное” время на приемы пищи. Еда и вода — наши основные источники энергии. "
                         "В моменте кажется, что и без еды можно продержаться, но закончить с задачей быстрее. Мы не замечаем, как постепенно "
                         "начинаем медленнее соображать, а сил становится всё меньше. Просто в какой-то день раз и сил ни на что нет\n"
                         "Итак, какой маленький шаг ты можешь предпринять уже сегодня, чтобы улучшить питьевой режим или режим питания?")
    await state.set_state(InputMessage.input_answer_state14_2)


@day_router14.message(F.text, InputMessage.input_answer_state14_2)
@is_now_day(14)
async def answer_day14_2(message: types.Message, state: FSMContext, bot: Bot):
    await state.clear()
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Иду делать", callback_data="Start_doing|14"))
    keyboard.row(InlineKeyboardButton(text="Поставил напоминание", callback_data="Start_doing|14"))
    await message.answer("Хорошо) Только пообещай себе, что сделаешь!\n\n"
                         "Кроме того, ты наверняка слышал о важности сна, физических нагрузок и прогулок на свежем воздухе. Налажен ли у тебя режим или день на день не приходится? "
                         "Мы не будем на этом останавливаться, но важно помнить, что тело — фундамент психики и эти аспекты нельзя оставлять в стороне\n\n"
                         "Следующий пункт — организация жизненного пространства. Некоторые люди уделяют много внимания обустройству квартиры и рабочего места, "
                         "некоторые не обращают на это внимания. В любом случае важно позаботиться о пространстве вокруг (да да, мы не существуем в вакууме и оно так или иначе влияет на нас). "
                         "И это не столько про дизайн (хотя никто не станет отрицать, что гирлянды в преддверии новогодних праздников способствуют появлению новогоднего настроения), "
                         "сколько про удобство (и порядок, конечно😄)\n\n"
                         "Кстати, порядок во внешнем пространстве может способствовать становлению порядка во внутреннем пространстве, особенно если это касается инструментов, "
                         "организующих твою работу (календари, планировщики и др.), но это ты, конечно, и без нас знаешь (надеемся😅)\n\n"
                         "Сегодня ты уйдешь из бота с заданием — нужно будет посмотреть свежим взглядом на своё рабочее место и подумать, а всё ли с ним хорошо? "
                         "Не раздражают ли тебя провода, торчащие тут и там? Удобно ли тебе сидеть на стуле или мышцы затекают уже через 20 минут? "
                         "Легко ли доставать необходимые материалы или приходится тянуться через весь стол (и ты никогда не задумывался, что правое плечо иногда ноет именно поэтому)?\n"
                         "Сделай сейчас, если есть такая возможность, или поставь напоминание на удобное время, но сделай обязательно сегодня, потом будет куча других дел и к этой задачке ты уже никогда не вернёшься",
                         reply_markup=keyboard.as_markup())


@day_router14.callback_query(Text(text="Start_doing|14"))
@is_now_day(14)
async def start_day11(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    now = datetime.now()
    target_time = datetime(now.year, now.month, now.day, 21, 30)
    if now >= target_time:
        target_time += timedelta(days=1)
    time_difference = target_time - now
    await asyncio.sleep(time_difference.total_seconds())
    question = await message.message.answer(
        text="Добрый вечер? Ну что там с твоим рабочем местом, что хочешь поменять?")
    await state.set_state(InputMessage.input_answer_state14_4)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router14.message(F.text, InputMessage.input_answer_state14_4)
@is_now_day(14)
async def answer_day14_4(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    await state.clear()
    await message.answer_sticker(sticker=sticker_ids[-2])
    await message.answer("Давай ещё быстренько посмотрим, что у тебя с состоянием")
    await start_LLIC(message, state, bot)
