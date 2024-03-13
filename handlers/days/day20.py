from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.markdown import hitalic

from db.answers import Answers
from handlers.user_handlers import start_LLIC
from settings import InputMessage, sticker_ids
from db.users_stat import Users_stat
from aiogram import types, F, Router, Bot

from utils.is_now_day import is_now_day

day_router20 = Router()


@day_router20.callback_query(Text(text="confirm|20"), any_state)
@is_now_day(20)
async def start_day20(message: CallbackQuery, state: FSMContext, bot: Bot):
    if int(await Users_stat(message.from_user.id).get_user_day()) == int(message.data.split("|")[1]):
        await state.clear()
        await message.message.answer("Управление собственными эмоциями — один из важнейших жизненных навыков, "
                                      "но далеко не все понимают, что он включает в себя не только подавление или сокрытие чувств. "
                                      "Все мы оказываемся в ситуациях, когда нормы и правила диктуют, как мы должны себя вести, "
                                      "и часто они подразумевают сдерживание ярких эмоций, особенно негативных. "
                                      "Однако если не позволять эмоциям выходить наружу, они будут накапливаться и однажды всплывут, "
                                      "или могут проявить себя в виде болезней. Поэтому крайне важно давать эмоциям “время и место”. "
                                      "Возможно не там, где они настигнут. Возможно, вечером дома. Возможно, через пару дней. Что же с ними в итоге делать?")
        await message.message.answer("Первым шагом эмоцию надо заметить. Это бывает не так-то просто. В нас вихрем проносится множество эмоций и в этой смеси бывает сложно что-то распознать. Иногда просто не хочется. Но всё-таки смесь надо разбить по ингредиентам, а ингредиенты назвать (что ты тренировался делать в прошлой части программы)\nПосле того, как ты смог выделить и назвать эмоцию, её надо принять. Не гнать от себя, не думать о том, что ты не должен или не хочешь её чувствовать, а принять. Принять, что она появилась. Принять, что она о чём-то говорит. Не бывает плохих и хороших эмоций. Эмоции — индикаторы отношения к тому, что происходит, и без них, нам было бы очень сложно ориентироваться в мире")
        keyboard = InlineKeyboardBuilder().row(
            InlineKeyboardButton(text="Понял) Буду прислушиваться к себе", callback_data="Understood|20")
        )
        await message.message.answer("Когда у тебя получилось принять эмоцию, проживи её. "
                             "Посмотри внутрь себя и почувствуй, что тебе хочется сделать: "
                             "возможно, тебе захочется поделиться с кем-то и получить поддержку (тут будет здорово, "
                             "если ты сможешь понять, какая именно поддержка тебе нужна и скажешь об этом), "
                             "возможно, тебе захочется остаться одному и послушать определенную музыку, "
                             "возможно, тебе захочется пойти в зал и побить грушу/побегать/потанцевать — в активности тоже отлично проживаются эмоции. "
                             "Главное, дать эмоциям время и место 👐", reply_markup=keyboard.as_markup())


@day_router20.callback_query(Text(text="Understood|20"))
@is_now_day(20)
async def answer_day20_1(message: CallbackQuery, state: FSMContext, bot: Bot):
    question = await message.message.answer("Итак, мы обсудили физиологический уровень, психологический, с его перцептивным и рефлексивными компонентами, и у нас остался поведенческий. "
                         "Как думаешь, что туда входит?")
    await state.set_state(InputMessage.input_answer_state20_3)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router20.message(F.text, InputMessage.input_answer_state20_3)
@is_now_day(20)
async def answer_day19_1(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    await state.clear()
    keyboard = InlineKeyboardBuilder()
    await message.answer_sticker(sticker=sticker_ids[5])
    keyboard.row(InlineKeyboardButton(text="Я так обычно и делаю", callback_data="OKAY_LETGO|20"))
    keyboard.row(InlineKeyboardButton(text="Возьму на заметку", callback_data="OKAY_LETGO|20"))
    keyboard.row(InlineKeyboardButton(text="Буду пробовать",
                                      callback_data="OKAY_LETGO|20"))
    await message.answer(
        "Что же можно сделать со стрессом на поведенческом уровне? Конечно, непосредственно решить проблему:\n"
        "1. Определи проблему: опиши её четко и конкретно, выдели основные аспекты, которые вызывают беспокойство.\n"
        "2. Проанализируй причины: выдели основными причины и что послужило их возникновению (тут может отлично помочь метод “5 почему”: "
        "ты задаешься вопросом, почему произошло то или иное, находишь ответ и далее задаешься вопросом, а что стало причиной этой причины, "
        "и так продолжаешь задаваться вопросом “почему?”, пока не доберешься до первоисточника проблемы).\n"
        "3. Поставь цель: определи, как должен выглядеть результат.\n"
        "4. Оцени требуемые и имеющиеся ресурсы: время, силы, знания, финансы, связи, инструменты и т.п.\n"
        "5. Разработай план действий: раздели цель на подцели, подцели — на задачи, а задачи — на конкретные шаги. "
        "Чем более определенным будет твой план, тем легче тебе будет приступить и продолжать идти к цели.\n"
        "6. Реализуй план: начни шаг за шагом выполнять план, оценивая прогресс и внося корректировки при необходимости.\n"
        "7. Оцени результат: посмотри, пришёл ли ты к той цели, которую ставил (или к какой-то другой), "
        "проанализируй, что сработало и что можно улучшить в будущем.\n"
        "8. Рассмотри и предприми возможные шаги для предотвращения повторного возникновения подобной проблемы😉")
    await message.answer("Попробуешь?", reply_markup=keyboard.as_markup())


@day_router20.callback_query(Text(text="OKAY_LETGO|20"))
@is_now_day(20)
async def answer_day20_1(message: CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.answer_sticker(sticker=sticker_ids[7])
    await message.message.answer("Ура! Мы прошлись по всем уровням проявления стресса и завтра вступим на финишную прямую🥳\n\n"
                         "Давай ещё быстренько посмотрим, что у тебя с состоянием")
    await start_LLIC(message, state, bot)
