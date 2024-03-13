from aiogram import Router, types, Bot, F
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import BufferedInputFile, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.answers import Answers
from db.users_stat import Users_stat
from handlers.user_handlers import start_LLIC
from settings import start_text, InputMessage
from utils.is_now_day import is_now_day

day_router2 = Router()


@day_router2.callback_query(Text(text="confirm|2"))
@is_now_day(2)
async def start_day1(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    if int(str(await Users_stat(message.from_user.id).get_user_day())) == int(message.data.split("|")[1]):
        text = """Представим, что ты в точке А: спокойно выполняешь рабочие задачки, отвлекаясь на сообщения в мессенджерах или small talks с коллегами — это твой нормальный рабочий режим. И тут тебе прилетает сообщение от руководителя: «Срочно! Надо сделать то-то и то-то, иначе …». У тебя начинает быстрее биться сердце, сознание сужается до одной единственной мысли о прилетевшем поручении, а тревога, кажется, накрывает с головой и ты замираешь в бездействии на некоторое время (секунды, минуты, а может быть даже часы…)
    
Это первая стадия в динамике развития стресса, которая называется alarm reaction, или стадия тревоги. Здесь твоя продуктивность падает, а организм готовится к предстоящему сопротивлению
    
Дальше наступает стадия резистентности (от лат. resistentia — сопротивление) и тут возможны два варианта развития событий: ты либо собираешься и начинаешь работать с удвоенной силой, либо теряешься, начинаешь совершать ненужные действия или вовсе замираешь, ничего не предпринимая. Первый вариант — это эустресс, в этом случае напряжение (стресс) способствует активизации не только физиологических процессов, но и мыслительных процессов, памяти, внимания, повышая уровень твоей продуктивности. Нам обычно кажется, что стресс — это что-то вредное, но в этом случае он тебе помогает, так же как и помогает оперативно выполнить работу накануне дедлайна
    
Однако возможен и второй вариант, когда высокое напряжение приводит к совершению ошибок, лишним действиям или вовсе остановке деятельности. Часто люди, говоря о стрессе, подразумевает именно это состояние. В науке это называют дистрессом, который, если решение не находится, переходит в истощение
    
Затянувшаяся стадия истощения приводит к возникновению психологических и физиологических проблем. Агрессивность, тревога, синдром «выгорания», проблемы со сном, астения, болезни сердечно-сосудистой системы…Список можно продолжать и продолжать, ведь стресс воздействует на весь организм
    
И ты здесь, чтобы не допустить этого, верно?
    
Давай перейдем от теории к практике и посмотрим на динамику развития стресса на твоём примере😉 Вспомни, когда ты последний раз испытывал стресс (=сталкивался со сложной или/и значимой задачей)
    """
        keyboard = InlineKeyboardBuilder()
        keyboard.row(InlineKeyboardButton(text="Угу, вспомнил", callback_data="Remember_1"))
        await state.clear()
        await message.message.answer(text=text, reply_markup=keyboard.as_markup())


@day_router2.callback_query(Text(text="Remember_1"))
@is_now_day(2)
async def start_day1(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    question = await message.message.answer("Что ты испытывал, когда только услышал о проблеме?")
    await state.set_state(InputMessage.input_answer_state2)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router2.message(F.text, InputMessage.input_answer_state2)
@is_now_day(2)
async def answer_start2(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    await state.clear()
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text=" Стресс придал мне сил 💪", callback_data="Remember_1_2"))
    keyboard.row(InlineKeyboardButton(text="Всё пропало…", callback_data="Remember_1_2"))
    await message.answer("А как развивалась история дальше? Ты стал продуктивным или, наоборот, деструктивным?", reply_markup=keyboard.as_markup())


@day_router2.callback_query(Text(text="Remember_1_2"))
@is_now_day(2)
async def start_day1(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Вернулся к рабочему состоянию", callback_data="Remember_1_3"))
    keyboard.row(InlineKeyboardButton(text="Застрял в напряжении", callback_data="Remember_1_3"))
    await message.message.answer("Следом ты вернулся в нормальный рабочий режим или застрял в состоянии напряжения?", reply_markup=keyboard.as_markup())


@day_router2.callback_query(Text(text="Remember_1_3"))
@is_now_day(2)
async def start_day1(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.answer("👌")
    await message.message.answer("Сегодня ты узнала, что стресс — не всегда зло😁 А ещё он включает в себя 3 стадии (тревоги, резистентности и истощения), каждой из которых свойственны свои проявления, и о них мы ещё поговорим, но завтра😉Давай ещё быстренько посмотрим, что у тебя с состоянием")
    await start_LLIC(message, state, bot)


"""agfajskdhlf;sjhgdfsakgjkhjfvdbafjskglkjlkjfhjdbjfkslgkldkjfdnfkslgd"""



