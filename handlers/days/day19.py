import asyncio
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

day_router19 = Router()

@day_router19.callback_query(Text(text="confirm|19"), any_state)
@is_now_day(19)
async def start_day19(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.edit_reply_markup()
    await state.clear()
    await message.message.answer(
        "Мы с тобой уже много говорили о том, что стресс это — состояние, которое ты испытываешь, сталкиваясь со сложной "
        "или важной для тебя задачей. И в этом утверждении кроется ответ на вопрос, почему в одной и той же ситуации "
        "один человек начнёт паниковать, а другой останется спокоен"
    )
    question = await message.message.answer("Есть идеи?")
    await state.set_state(InputMessage.input_answer_state19_1)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router19.message(F.text, InputMessage.input_answer_state19_1)
@is_now_day(19)
async def answer_day19_1(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    await state.clear()
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Погнали", callback_data="Pognali|19"))
    await message.answer_sticker(sticker=sticker_ids[3])
    await message.answer("Дело в том, что наша психика имеет сложную организацию и мы воспринимаем происходящее не буквально, "
                         "а, скажем так, как после обработки многочисленными фильтрами, созданными на нашем жизненном опыте. "
                         "Это крайне полезный механизм, который помогает ориентироваться в нашем мире, и он же отвечает за "
                         "то, что кто-то воспримет ситуацию как сложную/важную, а кто-то нет, и, как следствие, в одних и тех "
                         "же условиях у кого-то разовьётся стресс, а у кого-то нет. Поэтому внешний фактор сам по себе никогда "
                         "не является истинной причиной стресса (конечно, мы здесь говорим про психологический стресс, "
                         "физиологический стресс же будет возникать при воздействии негативных факторов на организм человека "
                         "(экстремальных температур, сильных физических воздействий, токсинов и т.д.) несмотря на восприятие "
                         "ситуации человеком)\n\n"
                         "В общем, к чему всё это: так как за восприятие ситуации отвечают условные “фильтры”, в некоторых "
                         "случаях их можно перефокусировать при помощи достаточно простых упражнений. Переходим к рефлексивному компоненту?",
                         reply_markup=keyboard.as_markup())


@day_router19.callback_query(Text(text="Pognali|19"))
@is_now_day(19)
async def continue_day19(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Вспомнил", callback_data="REMEMBER|19"))
    await message.message.answer(
        "Итак, чтобы поменять восприятие ситуации как сложной или важной, нужно посмотреть на неё под другим углом:"
        "\n<b>Вариант 1</b>: представить, что ты будешь думать об этой ситуации через 20, 30-50 лет. "
        "Будешь ли ты вообще про неё помнить? Будет ли она казаться тебе настолько важной? "
        "Будешь ли ты удивляться тому, как сильно переживал из-за неё?"
        "\n<b>Вариант 2</b>: представить самый худший вариант развития событий и способ поведения в нём. "
        "Какой может быть самый страшный исход? И что ты тогда будешь с этим делать?"
        "\n<b>Вариант 3</b>: подумать о том, а какие есть положительные стороны у создавшейся ситуации? "
                                 "Чему она может научить? От каких ошибок уберечь в дальнейшем?")
    await message.message.answer(f'Кроме того, когда тебе удасться остановить порочный поток негативных мыслей, хорошо закрепить в сознании положительные, например:\n• я могу справиться\n• я хочу решить эту задачу\n• я готов к действиям\nЗдесь ты программируешь себя на желаемый результат. Есть несколько правил формулировки таких утверждений: это должны быть простые (одно подлежащее и одно сказуемое), короткие (до 6 слов) предложения, содержащие информацию о себе (намерениях, ощущениях или процессах в теле и т.п.) в утвердительной форме (никаких частичек “не” или скрытого отрицания, например, как в слове "безошибочно"). А ещё, ты должен в них верить. Если ты чувствуешь неуверенность в том, что справишься, можешь заменить предложение на "я попробую справиться" и "я сделаю всё возможное для максимального результата". Повтори эти простые формулы несколько раз😉')
    await message.message.answer("Давай попробуем использовать эти инструменты на практике. Вспомни последнюю ситуацию, которая тебя тревожила", reply_markup=keyboard.as_markup())



@day_router19.callback_query(Text(text="REMEMBER|19"))
@is_now_day(19)
async def continue_reflexive_day19(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    question = await message.message.answer("Какой из инструментов тебе бы лучше подошёл в данной ситуации: "
                         "представить, как ты будешь относиться к этой ситуации через пару десятков лет, "
                         "какой может быть самый худший вариант развития событий и что ты будешь делать, "
                         "если он произойдёт, или найти положительные аспекты данного поворота событий?")
    await state.set_state(InputMessage.input_answer_state19_3)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router19.message(F.text, InputMessage.input_answer_state19_3)
@is_now_day(19)
async def answer_day19_3(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("И что бы ты тогда стал думать о ситуации?")
    await state.set_state(InputMessage.input_answer_state19_4)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router19.message(F.text, InputMessage.input_answer_state19_4)
@is_now_day(19)
async def answer_day19_4(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("Какие положительные мысли ты бы хотел закрепить?")
    await state.set_state(InputMessage.input_answer_state19_5)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router19.message(F.text, InputMessage.input_answer_state19_5)
@is_now_day(19)
async def answer_day19_5(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    await state.clear()
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Да", callback_data="YES_ZAKREP|19"))
    keyboard.row(InlineKeyboardButton(text="Нет", callback_data="NO_ZAKREP|19"))
    await message.answer(
        "Твой ответ попадает под критерий простых коротких предложений, содержащих информацию о тебе в утвердительной форме?",
    reply_markup=keyboard.as_markup())


@day_router19.message(F.text, InputMessage.input_answer_state19_7)
@day_router19.callback_query(Text(text="YES_ZAKREP|19"))
@is_now_day(19)
async def continue_reflexive_day19(message: types.CallbackQuery | types.Message, state: FSMContext, bot: Bot):
    if type(message) == types.CallbackQuery:
        question = await message.message.answer("Отлично! Какой из инструментов ты бы хотел использовать завтра в случае возникновения напряжения?")
    else:
        data = await state.get_data()
        question = data.get("question")
        answers = Answers()
        await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
        question = await message.answer(
            "Отлично! Какой из инструментов ты бы хотел использовать завтра в случае возникновения напряжения?")
    await state.set_state(InputMessage.input_answer_state19_6)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router19.callback_query(Text(text="NO_ZAKREP|19"))
@is_now_day(19)
async def continue_reflexive_day19(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    question = await message.message.answer("Давай попробуем ещё раз")
    await state.set_state(InputMessage.input_answer_state19_7)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router19.message(F.text, InputMessage.input_answer_state19_6)
@is_now_day(19)
async def answer_day19_4(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    await message.answer("Одобряем! Увидимся завтра 😉")
    await state.clear()
    await Users_stat(message.from_user.id).edit_user_end_day()


