from aiogram import Router, types, Bot, F
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import BufferedInputFile, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.answers import Answers
from db.users_stat import Users_stat
from settings import start_text, InputMessage
from utils.is_now_day import is_now_day

day_router1 = Router()


@day_router1.callback_query(Text(text="confirm|1"))
@is_now_day(1)
async def start_day1(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.edit_reply_markup()
    await state.clear()
    question = await message.message.answer("Для начала разберёмся, что вообще такое стресс. Что ты понимаешь под стрессом?")
    await state.set_state(InputMessage.input_answer_state1)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)
    await message.message.delete()


@day_router1.message(F.text, InputMessage.input_answer_state1)
@is_now_day(1)
async def answer_start1(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_new_user(message.from_user.id)
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("Отличное предположение! Вслед за доктором психологических наук А.Б. Леоновой, мы определяем стресс как состояние повышенной мобилизации психологических и энергетических ресурсов, развивающиеся в ответ на повышение сложности или субъективной значимости деятельности. Другими словами, стресс — это состояние, которое ты испытываешь, сталкиваясь со сложной и важной для тебя задачей. При этом у тебя возникает желание либо решить проблему, либо избавится от неё. И в этом стресс может как помочь, так и помешать. Но это мы обсудим позже\nА теперь вспомни, когда последний раз ты испытывал стресс? Напиши свой отчёт в чате ")
    await state.set_state(InputMessage.input_answer_state1_1)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router1.message(F.text, InputMessage.input_answer_state1_1)
@is_now_day(1)
async def answer_start1(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("Что его вызвало?")
    await state.set_state(InputMessage.input_answer_state1_2)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router1.message(F.text, InputMessage.input_answer_state1_2)
@is_now_day(1)
async def answer_start1(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Да", callback_data="YES|1"))
    keyboard.row(InlineKeyboardButton(text="Нет", callback_data="NO|1"))
    await message.answer(text="Можно ли это назвать сложной и значимой задачей?", reply_markup=keyboard.as_markup())
    await state.clear()


@day_router1.callback_query(Text(text="YES|1"))
@is_now_day(1)
async def start_day1(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.answer("👌")
    await message.message.answer("Здорово, что ты сразу это определил, хотя вывод не всегда может быть очевидным."
                                 " Например, можно испытывать напряжение во время разговора с близким человеком."
                                 " На первый взгляд может показаться, что здесь нет сложной или значимой задачи,"
                                 " но если посмотреть глубже, то станет понятно, что в этой ситуации тебе важно быть"
                                 " услышанным и понятым. И это и является значимой задачей в этом диалоге\n\nСегодня"
                                 " мы разобрались с тем, что же такое стресс и выделили его основные критерии, на основе"
                                 " которых ты попробовал определить, когда ты непосредственно сталкивался со стрессом,"
                                 " а завтра мы расскажем, что стресс — состояние неоднородное, имеющее несколько стадий"
                                 " в своей динамике 📉")
    await Users_stat(message.from_user.id).edit_user_end_day()


@day_router1.callback_query(Text(text="NO|1"))
@is_now_day(1)
async def start_day1(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Да, причина является сложной или/и значимой задачей", callback_data="NO_2|1"))
    keyboard.row(InlineKeyboardButton(text="Всё-таки это не стресс", callback_data="NO_2|1"))
    await message.message.answer("Хм… Здесь может быть 2 варианта: 1 — это не стресс, а что-то другое; 2 — на причину нужно посмотреть под другим углом. Например, можно испытывать напряжение во время разговора с близким человеком. На первый взгляд может показаться, что здесь нет сложной или значимой задачи, но если капнуть глубже, то станет понятно, что в этой ситуации тебе важно быть услышанным и понятым. И это и является значимой задачей в этом диалоге. Давай подумаем, точно ли причину твоего крайнего стресса нельзя назвать сложной или/и значимой задачей?",
                                 reply_markup=keyboard.as_markup())


@day_router1.callback_query(Text(text="NO_2|1"))
@is_now_day(1)
async def start_day1(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.answer("👌Сегодня мы разобрались с тем, что же такое стресс и выделили его основные критерии, на основе которых ты попробовал определить, когда ты непосредственно сталкивался со стрессом, а завтра мы расскажем, что стресс — состояние неоднородное, имеющее несколько стадий в своей динамике 📉")
    user = Users_stat(message.from_user.id)
    await user.edit_user_end_day()
