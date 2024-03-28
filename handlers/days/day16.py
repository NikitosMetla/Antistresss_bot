from aiogram import types, Dispatcher, Router, F, Bot
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

day_router16 = Router()

@day_router16.callback_query(Text(text="confirm|16"), any_state)
@is_now_day(16)
async def start_day16(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.edit_reply_markup()
    await state.clear()
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Да, есть такое😄", callback_data="UnderstandingProblem|16"))
    await message.message.answer(
        "Наверняка ты замечал, что если ты не понимаешь, зачем ты делаешь ту или иную работу/выполняешь задание в университете, процесс становится невероятно тяжелым, затягивается или вовсе откладывается, пока тебе о нём не напомнят.", reply_markup=keyboard.as_markup())


@day_router16.callback_query(Text(text="UnderstandingProblem|16"))
@is_now_day(16)
async def understanding_problem(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    question = await message.message.answer("К сожалению, не всегда на работе или учебе объясняют, какой смысл в той или иной деятельности. Но чтобы тебе самому было легче и интересней справится с той или иной работой, лучше это всё-таки выяснить. Как ты можешь это сделать?")
    await state.set_state(InputMessage.input_answer_state16_1)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router16.message(F.text, InputMessage.input_answer_state16_1)
@is_now_day(16)
async def answer_day16_1(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    await state.clear()
    await message.answer_sticker(sticker=sticker_ids[-6])
    await message.answer(("Действительно, есть несколько общих способов:\n"
                         "• Непосредственно спросить у руководителя, как твоя работа влияет на достижение целей компании/спросить у преподавателя, на развитие каких навыков направлено это задание и как ты сможешь применять их в будущем.\n"
                         "• Обсудить то же самое с коллегами или одногруппниками."
                         "\n• Самостоятельно поразмышлять о том, какой может быть смысл в той или иной работе и на что она влияет."))
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="О да(", callback_data="TaskUnderstandingProblem|16"))
    keyboard.row(InlineKeyboardButton(text="Нет, с этим всё ок", callback_data="NoTaskUnderstandingProblem|16"))
    await message.answer("Есть ли у тебя такое задание на примете, смысл выполнения которых ты не понимаешь?", reply_markup=keyboard.as_markup())


@day_router16.callback_query(Text(text="TaskUnderstandingProblem|16"))
@is_now_day(16)
async def task_understanding_problem(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Спрошу руководителя/преподавателя", callback_data="NoTaskUnderstandingProblem|16"))
    keyboard.row(InlineKeyboardButton(text="Поговорю с коллегами/одногруппниками", callback_data="NoTaskUnderstandingProblem|16"))
    keyboard.row(InlineKeyboardButton(text="Постараюсь самостоятельно найти смысл", callback_data="NoTaskUnderstandingProblem|16"))
    keyboard.row(InlineKeyboardButton(text="Это слишком сложно, не буду с этим возиться", callback_data="NoTaskUnderstandingProblem|16"))
    await message.message.answer("Как ты будешь в этом разбираться?", reply_markup=keyboard.as_markup())


@day_router16.callback_query(Text(text="NoTaskUnderstandingProblem|16"))
@is_now_day(16)
async def answer_day16_3(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Всегда так делаю", callback_data="ALWAYS_DO|16"))
    keyboard.row(InlineKeyboardButton(text="Это моя зона роста", callback_data="ALWAYS_DO|16"))
    await message.message.answer(
        "Хорошо, теперь пойдём дальше)\n"
        "Следующий пункт касается взаимоотношений в коллективе — мало что так нас волнует, как прямой или косвенный контакт с другими людьми."
        " Думаем, не надо объяснять, что социальные связи — одна из основных сторон нашей жизни и она непосредственно влияет на твоё состояние."
        " Налаживание коммуникации — целая 'наука' и здесь у нас нет возможности остановиться на этом подробно, но мы всё же подсветим 1 аспект: предотвращение конфликтов"
        "\n\nНам всем неприятно попадать в конфликты и многие люди стараются их избегать."
        " Тем не менее в конфликтах проявляются противоречия, которые в регулярной коммуникации оказываются скрыты."
        " Вместо того, чтобы умалчивать о возникающих разногласиях, можно предложить человеку обсудить происходящее и выработать стратегию, которая будет устраивать обоих",
        reply_markup=keyboard.as_markup()
    )


@day_router16.callback_query(Text(text="ALWAYS_DO|16"))
@is_now_day(16)
async def answer_day16_4(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.edit_reply_markup()
    await message.message.answer_sticker(sticker=sticker_ids[-5])
    question = await message.message.answer(
        "Ещё один аспект, про который мы поговорим сегодня — мотивация."
        " Мы уже обсудили, что гораздо легче работать, если ты понимаешь смысл того, что ты делаешь, и на что твоя деятельность влияет, а ещё если в коллективе благоприятный климат 👐"
        " Есть ещё один фактор, который мы бы хотели обсудить: обратная связь. Обратная связь от руководства, преподавателей и коллег может быть очень разной и тебе необходимо понять, что тебе важно услышать:"
        " подробный комментарий (что было сделано хорошо, что и как можно было бы улучшить, что сделать по-другому и т.д.), может быть слова поддержки или благодарность за проделанную работу"
        "\n\nКакую обратную связь ты бы хотел получать?"
    )
    await state.set_state(InputMessage.input_answer_state16_5)


@day_router16.message(F.text, InputMessage.input_answer_state16_5)
@is_now_day(16)
async def answer_day16_5(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    await message.answer_sticker(sticker=sticker_ids[-4])
    question = await message.answer(
        "Кроме этого есть ещё множество факторов, влияющих на мотивацию:"
        "\n• твои потребности и ценности (которые могут включать желание самореализации в выбранной сфере деятельности и личностное развитие, стремление к престижной работе, повышению социального статуса, улучшению качества жизни и/или поддержанию достигнутого, ориентацию на безопасность (в том числе финансовую) и многое другое)"
        "\n• ясные достаточно сложные, но достижимые цели"
        "\n• требуемые и имеющиеся ресурсы (материальные и нематериальные)"
        "\n• поощрение выполнения работы (также материальное и нематериальное)"
        "\n\nЧто из этого списка про тебя?"
        "\nЧего в твоей работе или учебе не хватает, чтобы мотивация была выше?"
    )
    await state.set_state(InputMessage.input_answer_state16_6)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router16.message(F.text, InputMessage.input_answer_state16_6)
@is_now_day(16)
async def answer_day16_6(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    question = await message.answer("Как ты можешь поспособствовать появлению этого?")
    await state.set_state(InputMessage.input_answer_state16_7)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router16.message(F.text, InputMessage.input_answer_state16_7)
@is_now_day(16)
async def answer_day16_7(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    await message.answer(
        "Хорошо)\nДавай ещё быстренько посмотрим, что у тебя с состоянием"
    )
    await state.clear()
    await start_LLIC(message, state, bot)
