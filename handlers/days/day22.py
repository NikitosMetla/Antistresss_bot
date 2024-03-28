from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state
from aiogram.types import InlineKeyboardButton, CallbackQuery
from aiogram import types, Bot, F, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.answers import Answers
from db.feed_back import FEED_BACK
from db.users import Users
from db.users_stat import Users_stat
from handlers.user_handlers import start_LLIC, start_statement_next_days
from settings import InputMessage, sticker_ids
from utils.is_now_day import is_now_day

day_router22 = Router()

@day_router22.callback_query(Text(text="confirm|22"), any_state)
@is_now_day(22)
async def not_sad_day22(message: CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.edit_reply_markup()
    await state.clear()
    await message.message.answer("Давай посмотрим на цель, которую ты поставил вчера. Какие действия нужно предпринять, чтобы достичь её?")
    await state.set_state(InputMessage.input_answer_state22_1)


@day_router22.message(F.text, InputMessage.input_answer_state22_1)
@is_now_day(22)
async def answer_day22_1(message: types.Message, state: FSMContext, bot: Bot):
    question = await message.answer("Ага, теперь давай более конкретно. Какие методы ты выбираешь и когда/как часто каждый из них будешь использовать? Пропиши по пунктам")
    await state.set_state(InputMessage.input_answer_state22_2)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router22.message(F.text, InputMessage.input_answer_state22_2)
@is_now_day(22)
async def answer_day22_2(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("Как ты думаешь, на сколько процентов ты сможешь выполнить этот план?")
    await state.set_state(InputMessage.input_answer_state22_3)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router22.message(F.text, InputMessage.input_answer_state22_3)
@is_now_day(22)
async def answer_day22_3(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("Что ты можешь предпринять, чтобы эти помехи предотвратить или минимизировать их ущерб?")
    await state.set_state(InputMessage.input_answer_state22_4)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router22.message(F.text, InputMessage.input_answer_state22_4)
@is_now_day(22)
async def answer_day22_4(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("Что ещё можно сделать для того, чтобы тебе было легче достичь цели?")
    await state.set_state(InputMessage.input_answer_state22_21)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router22.message(F.text, InputMessage.input_answer_state22_21)
@is_now_day(22)
async def answer_day22_5(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    await state.clear()
    await message.answer("Отлично! Теперь у тебя есть план) Осталось его придерживаться")
    await message.answer_sticker(sticker=sticker_ids[6])
    await message.answer("Вот и подошла наша программа к концу! Давай обсудим результаты)\nЧто изменилось вследствие прохождения программы?")
    await state.set_state(InputMessage.input_answer_state22_6)


@day_router22.message(F.text, InputMessage.input_answer_state22_6)
@is_now_day(22)
async def answer_day22_6(message: types.Message, state: FSMContext, bot: Bot):
    await FEED_BACK().add_new_user(message.from_user.id)
    await FEED_BACK().question1(message.from_user.id, message.text)
    await message.answer("Что изменилось в твоем поведении?")
    await state.set_state(InputMessage.input_answer_state22_7)


@day_router22.message(F.text, InputMessage.input_answer_state22_7)
@is_now_day(22)
async def answer_day22_7(message: types.Message, state: FSMContext, bot: Bot):
    await FEED_BACK().question2(message.from_user.id, message.text)
    await message.answer("Что изменилось в твоем самоощущении, в том числе в стрессовых ситуациях и после них?")
    await state.set_state(InputMessage.input_answer_state22_8)


@day_router22.message(F.text, InputMessage.input_answer_state22_8)
@is_now_day(22)
async def answer_day22_8(message: types.Message, state: FSMContext, bot: Bot):
    await FEED_BACK().question3(message.from_user.id, message.text)
    await message.answer("Какие инструменты, с которыми мы тебя познакомили, ты будешь использовать?")
    await state.set_state(InputMessage.input_answer_state22_9)


@day_router22.message(F.text, InputMessage.input_answer_state22_9)
@is_now_day(22)
async def answer_day22_9(message: types.Message, state: FSMContext, bot: Bot):
    await FEED_BACK().question4(message.from_user.id, message.text)
    keyboard = InlineKeyboardBuilder().row(
        InlineKeyboardButton(text="1", callback_data="progress_rating|1"),
        InlineKeyboardButton(text="2", callback_data="progress_rating|2"),
        InlineKeyboardButton(text="3", callback_data="progress_rating|3"),
        InlineKeyboardButton(text="4", callback_data="progress_rating|4"),
        InlineKeyboardButton(text="5", callback_data="progress_rating|5"),
        InlineKeyboardButton(text="6", callback_data="progress_rating|6"),
        InlineKeyboardButton(text="7", callback_data="progress_rating|7"),
    )
    await message.answer("Как ты оцениваешь свой прогресс в совладании со стрессом по шкале от 1 до 7, где 7 — максимальное значение?", reply_markup=keyboard.as_markup())


@day_router22.callback_query(Text(startswith="progress_rating|"))
@is_now_day(22)
async def progress_rating_day22(message: CallbackQuery, state: FSMContext, bot: Bot):
    rating = int(message.data.split("|")[1])
    await FEED_BACK().question5(message.from_user.id, rating)
    await Users().user_self_progress(self_progress=rating, user_id=message.from_user.id)
    await message.message.answer("Любая обратная связь от тебя✍️")
    await message.message.edit_reply_markup()
    await state.set_state(InputMessage.input_answer_state22_11)


@day_router22.message(F.text, InputMessage.input_answer_state22_11)
@is_now_day(22)
async def answer_day22_11(message: types.Message, state: FSMContext, bot: Bot):
    await state.clear()
    await FEED_BACK().question6(message.from_user.id, message.text)
    await message.answer("Класс! А теперь давай посмотрим, что скажут методики о твоем состоянии👇")
    await start_LLIC(message, state, bot)


@day_router22.message(F.text, InputMessage.input_answer_state22_100)
@is_now_day(22)
async def answer_day22_11(message: types.Message, state: FSMContext, bot: Bot):
    await state.clear()
    await FEED_BACK().question0(message.from_user.id, message.text)
    await start_statement_next_days(message, state, bot)


@day_router22.callback_query(Text(startswith="answer|23"))
@is_now_day(22)
async def progress_rating_day22(message: CallbackQuery, state: FSMContext, bot: Bot):
    await FEED_BACK().question7(message.from_user.id, message.data[9:])
    await message.message.answer("Что ты замечал за этот месяц? ")
    await state.set_state(InputMessage.input_answer_state22_20)


@day_router22.message(F.text, InputMessage.input_answer_state22_20)
@is_now_day(22)
async def answer_day22_11(message: types.Message, state: FSMContext, bot: Bot):
    await FEED_BACK().question8(message.from_user.id, message.text)
    await message.answer("Что изменилось в твоем самоощущении, в том числе в стрессовых ситуациях и после них?")
    await state.set_state(InputMessage.input_answer_state22_12)


@day_router22.message(F.text, InputMessage.input_answer_state22_12)
@is_now_day(22)
async def answer_day22_11(message: types.Message, state: FSMContext, bot: Bot):
    await FEED_BACK().question9(message.from_user.id, message.text)
    await message.answer("Что изменилось в твоем самоощущении, в том числе в стрессовых ситуациях и после них?")
    await state.set_state(InputMessage.input_answer_state22_13)


@day_router22.message(F.text, InputMessage.input_answer_state22_13)
@is_now_day(22)
async def answer_day22_11(message: types.Message, state: FSMContext, bot: Bot):
    await FEED_BACK().question10(message.from_user.id, message.text)
    await message.answer("Какие инструменты, с которыми мы тебя познакомили, ты использовал?")
    await state.set_state(InputMessage.input_answer_state22_14)


@day_router22.message(F.text, InputMessage.input_answer_state22_14)
@is_now_day(22)
async def answer_day22_11(message: types.Message, state: FSMContext, bot: Bot):
    await FEED_BACK().question11(message.from_user.id, message.text)
    await message.answer("Любая обратная связь от тебя✍️")
    await state.set_state(InputMessage.input_answer_state22_15)


@day_router22.message(F.text, InputMessage.input_answer_state22_15)
@is_now_day(22)
async def answer_day22_11(message: types.Message, state: FSMContext, bot: Bot):
    await FEED_BACK().question12(message.from_user.id, message.text)
    await message.answer("Спасибо, что был с нами всё это время ❤️ Хорошего самоощущения и психологического благополучия👐")
    await state.clear()



@day_router22.message(Text(text="/contact_us"))
async def start(message: types.Message, state: FSMContext, bot: Bot):
    await state.set_state(InputMessage.connect_us)
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Отмена", callback_data="cancel_answer"))
    answer = await message.answer("Введите ваше обращение", reply_markup=keyboard.as_markup())
    await state.update_data(message_id=answer.message_id)
