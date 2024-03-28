from aiogram import types, Router, F, Bot
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.answers import Answers
from db.users_stat import Users_stat
from settings import InputMessage
from utils.is_now_day import is_now_day

day_router3 = Router()


@day_router3.callback_query(Text(text="confirm|3"), any_state)
@is_now_day(3)
async def start_again(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.edit_reply_markup()
    await state.clear()
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Угу, вспомнил", callback_data="REMEMBERED|3"))
    await message.message.answer("Казалось бы, вроде вчера всё обсудили, и там всё предельно ясно! Да не всё так просто)) "
                         "Чтобы эффективно бороться со стрессом, важно осознавать, как он проявляется\n"
                         "А проявляется он на трёх уровнях:\n"
                         "•физиологическом\n•психологическом\n•поведенческом\n\n"
                         "С физиологией всё понятно: при остром стрессе (то есть когда ты непосредственно "
                         "находишься в стрессовой ситуации) начинает быстрее биться сердце, может перехватить дыхание, "
                         "пересохнуть горло, напрячься мышцы, могут трястись руки (и ещё много чего происходит внутри "
                         "организма, но это нашему прямому наблюдению не подвластно, поэтому мы это здесь не обсуждаем)\n\n"
                         "В психологическом уровне скрываются 2 подуровня: операциональный и рефлексивный. Первый подуровень "
                         "включает перцептивные и когнитивные процессы. Помнишь, мы вчера говорили о том, что на стадии тревоги "
                         "сознание может зациклиться на одной единственной мысли, а на стадии резистентности функции внимания, "
                         "памяти, мыслительные процессы могут значительно улучшиться?) Операциональный подуровень про это. "
                         "Рефлексивный же про рефлексию :) Но не только. Не только про то, что ты думаешь про ситуацию и "
                         "собственное состояние, но и то, что ты чувствуешь, какая у тебя мотивация…Ещё не запутался? "
                         "Если запутался, не переживай, отработаем всё на практике\n\n"
                         "Третий уровень, поведенческий, охватывает деятельностную сторону процесса. То есть то, что ты делаешь, "
                         "насколько точно и скоро. Это всё про результат\n\n"
                         "Ну а теперь наша любимая рубрика “вспомнить всё”😁\n"
                         "Вспомни, когда ты последний раз испытывал стресс (=сталкивался со сложной или/и значимой задачей), "
                         "может быть это было даже сегодня", reply_markup=keyboard.as_markup())


@day_router3.callback_query(Text(text="REMEMBERED|3"))
@is_now_day(3)
async def remembered(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    question = await message.message.answer("Опиши, что происходило с твоим телом в тот момент")
    await state.set_state(InputMessage.input_answer_state3_1)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router3.message(F.text, InputMessage.input_answer_state3_1)
@is_now_day(3)
async def answer_remembered1(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("Угу, а какие мысли у тебя возникали?")
    await state.set_state(InputMessage.input_answer_state3_2)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router3.message(F.text, InputMessage.input_answer_state3_2)
@is_now_day(3)
async def answer_remembered2(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("А что ты чувствовал? Какая эмоция была? (Заметь, эмоция — не мысль, не твои действия в ситуации, "
                         "это ощущение, которое может быть сложно назвать, но ты всё-таки попробуй)")
    await state.set_state(InputMessage.input_answer_state3_3)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router3.message(F.text, InputMessage.input_answer_state3_3)
@is_now_day(3)
async def answer_remembered3(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("Иии, последнее на сегодня, что ты сделал?")
    await state.set_state(InputMessage.input_answer_state3_4)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router3.message(F.text, InputMessage.input_answer_state3_4)
@is_now_day(3)
async def answer_remembered4(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    await message.answer("Ух, не лёгкую работу ты сегодня проделал! Столько внимания своему состоянию уделил! "
                         "А мы тебе рассказали про разные уровни проявления стресса (физиологический, "
                         "психологический и поведенческий). И каждый из них мы будем использовать, чтобы бороться со стрессом. "
                         "И это дальше в нашей программе! Не переключайтесь😄")
    await state.clear()
    user = Users_stat(message.from_user.id)
    await user.edit_user_end_day()
