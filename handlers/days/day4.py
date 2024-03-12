from aiogram import types, Dispatcher, Router, F, Bot
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.users_stat import Users_stat
from handlers.user_handlers import start_LLIC
from settings import InputMessage
from utils.is_now_day import is_now_day

day_router4 = Router()


@day_router4.callback_query(Text(text="confirm|4"), any_state)
@is_now_day(4)
async def start_again(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    if int(await Users_stat(message.from_user.id).get_user_day()) == int(message.data.split("|")[1]):
        await state.clear()
        keyboard = InlineKeyboardBuilder()
        keyboard.row(InlineKeyboardButton(text="Утомление", callback_data="FALSE|4_1"))
        keyboard.row(InlineKeyboardButton(text="Монотония", callback_data="MONOTON|4_1"))
        keyboard.row(InlineKeyboardButton(text="Пресыщение", callback_data="FALSE|4_1"))
        keyboard.row(InlineKeyboardButton(text="Стресс", callback_data="FALSE|4_1"))
        await state.set_state(InputMessage.input_answer_state4_1)
        text_variable = """Мы тогда тебе обещали попозже рассказать, что они значат. Рассказываем
        
Стресс, как ты уже понял — это состояние, которое ты испытываешь, сталкиваясь со сложной и важной для тебя задачей. При этом у тебя возникает желание решить проблему или избавится от неё
Дада, повторение — мать учения
На графике ещё были утомление, монотония и пресыщение 
    
Утомление — это класс состояний, характеризующихся истощением и дискоординацией. Это усталость, которая развивается из-за длительных и интенсивных нагрузок. Индикатором утомления является твоё желание завершить работу и отдохнуть
    
Монотония — это состояния сниженного сознательного контроля за исполнением деятельности, возникающие в ситуациях однообразной работы с частым повторением стереотипных действий. Если ты слушаешь очень скучную лекцию и засыпаешь, хотя накануне наконец-то выспался (где это видано?), это монотония. Стоит тебе сменить деятельность и ты почувствуешь прилив энергии, спать уже не захочется
    
Психическое пресыщение — это состояния неприятия слишком простой и неинтересной/малоосмысленной деятельности. Такая работа сопровождается выраженным стремлением прекратить её или внести разнообразие в заданный стереотип исполнения. Если при монотонии тебе просто хочется заняться чем-нибудь другим, то при пресыщении тебе крайне хочется отказаться от этой работы 
    
Почему мы с тобой про это говорим?
Дело в том, что стресс часто путают с другими состояниями сниженной работоспособности (к которым и относятся утомление, монотония, психическое пресыщение, стресс и другие). Действительно, по внешним проявлениям эти состояния могут быть очень похожи. Но механизм возникновения разный, а значит и бороться с ними нужно по-разному
    
Итак, если ты хочешь заняться чем-нибудь поинтереснее, то у тебя"""
        await message.message.answer(text_variable, reply_markup=keyboard.as_markup())


@day_router4.callback_query(Text(text="FALSE|4_1"), InputMessage.input_answer_state4_1)
@is_now_day(4)
async def remembered(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Утомление", callback_data="FALSE|4_1"))
    keyboard.row(InlineKeyboardButton(text="Монотония", callback_data="MONOTON|4_1"))
    keyboard.row(InlineKeyboardButton(text="Пресыщение", callback_data="FALSE|4_1"))
    keyboard.row(InlineKeyboardButton(text="Стресс", callback_data="FALSE|4_1"))
    await message.message.answer("Неа, вернись к определениям, а после попробуй ещё😉\nИтак, если ты хочешь заняться чем-нибудь поинтереснее, у тебя",
                                 reply_markup=keyboard.as_markup())


@day_router4.callback_query(Text(text="MONOTON|4_1"), InputMessage.input_answer_state4_1)
@is_now_day(4)
async def remembered(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.answer("👍")
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Утомление", callback_data="FALSE|4_2"))
    keyboard.row(InlineKeyboardButton(text="Монотония", callback_data="FALSE|4_2"))
    keyboard.row(InlineKeyboardButton(text="Пресыщение", callback_data="STRESS|4_2"))
    keyboard.row(InlineKeyboardButton(text="Стресс", callback_data="FALSE|4_2"))
    await state.set_state(InputMessage.input_answer_state4_2)
    await message.message.answer("Если ты не хочешь продолжать какую-либо работу, то у тебя",
                                 reply_markup=keyboard.as_markup())


@day_router4.callback_query(Text(text="STRESS|4_2"), InputMessage.input_answer_state4_2)
@is_now_day(4)
async def remembered(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.answer("👍")
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Утомление", callback_data="UTOMLEN|4_3"))
    keyboard.row(InlineKeyboardButton(text="Монотония", callback_data="FALSE|4_3"))
    keyboard.row(InlineKeyboardButton(text="Пресыщение", callback_data="FALSE|4_3"))
    keyboard.row(InlineKeyboardButton(text="Стресс", callback_data="FALSE|4_3"))
    await state.set_state(InputMessage.input_answer_state4_3)
    await message.message.answer("Если ты устал и хочешь расслабиться, то у тебя",
                                 reply_markup=keyboard.as_markup())


@day_router4.callback_query(Text(text="FALSE|4_2"), InputMessage.input_answer_state4_2)
@is_now_day(4)
async def remembered(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Утомление", callback_data="FALSE|4_2"))
    keyboard.row(InlineKeyboardButton(text="Монотония", callback_data="FALSE|4_2"))
    keyboard.row(InlineKeyboardButton(text="Пресыщение", callback_data="STRESS|4_2"))
    keyboard.row(InlineKeyboardButton(text="Стресс", callback_data="FALSE|4_2"))
    await message.message.answer("Неа, вернись к определениям, а после попробуй ещё😉\nИтак, если ты не хочешь продолжать какую-либо работу, то у тебя",
                                 reply_markup=keyboard.as_markup())


@day_router4.callback_query(Text(text="FALSE|4_3"), InputMessage.input_answer_state4_3)
@is_now_day(4)
async def remembered(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Утомление", callback_data="UTOMLEN|4_3"))
    keyboard.row(InlineKeyboardButton(text="Монотония", callback_data="FALSE|4_3"))
    keyboard.row(InlineKeyboardButton(text="Пресыщение", callback_data="FALSE|4_3"))
    keyboard.row(InlineKeyboardButton(text="Стресс", callback_data="FALSE|4_3"))
    await message.message.answer("Неа, вернись к определениям, а после попробуй ещё😉\nИтак, если ты устал и хочешь расслабиться, то у тебя",
                                 reply_markup=keyboard.as_markup())



@day_router4.callback_query(Text(text="UTOMLEN|4_3"), InputMessage.input_answer_state4_3)
@is_now_day(4)
async def remembered(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.answer("👍")
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Утомление", callback_data="FALSE|4_4"))
    keyboard.row(InlineKeyboardButton(text="Монотония", callback_data="FALSE|4_4"))
    keyboard.row(InlineKeyboardButton(text="Пресыщение", callback_data="FALSE|4_4"))
    keyboard.row(InlineKeyboardButton(text="Стресс", callback_data="Stress|4_4"))
    await state.set_state(InputMessage.input_answer_state4_4)
    await message.message.answer("Если ты хочешь избавиться от возникшей проблемы (решив её/ закрыв на неё глаза/ передав ответственность коллеге или однокурснику и т.д.), то у тебя",
                                 reply_markup=keyboard.as_markup())


@day_router4.callback_query(Text(text="FALSE|4_4"), InputMessage.input_answer_state4_4)
@is_now_day(4)
async def remembered(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Утомление", callback_data="FALSE|4_4"))
    keyboard.row(InlineKeyboardButton(text="Монотония", callback_data="FALSE|4_4"))
    keyboard.row(InlineKeyboardButton(text="Пресыщение", callback_data="FALSE|4_4"))
    keyboard.row(InlineKeyboardButton(text="Стресс", callback_data="Stress|4_4"))
    await message.message.answer("Неа, вернись к определениям, а после попробуй ещё😉\nИтак, Если ты хочешь избавиться от возникшей проблемы (решив её/ закрыв на неё глаза/ передав ответственность коллеге или однокурснику и т.д.), то у тебя",
                                 reply_markup=keyboard.as_markup())


@day_router4.callback_query(Text(text="Stress|4_4"), InputMessage.input_answer_state4_4)
@is_now_day(4)
async def remembered(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.answer("👍")
    await state.clear()
    text = """Отлично! С понятиями разобрались, теперь главный вопрос: “А делать то что?”
Если коротко:

Устал — отдохни (безудержное листание тиктоков и рилсов — это не качественный отдых! Лучше полежи с закрытыми глазами и послушай спокойную музыку). А если серьёзно, отдых — это очень важно как для твоего психического, так и физиологического здоровья 

Скучно — добавь разнообразия, например, на лекции считай, загибая пальцы, сколько раз преподаватель говорит свое излюбленное словечко (мы всё-таки не хотим сливаться с задачи послушать лекцию (а не просто там посидеть или решать на ней рабочие задачки, раз уж ты пришел), поэтому предлагаем именно загибать пальцы или записывать результаты, если же ты будешь пытаться удержать цифру в голове, то часть лекции пройдет мимо)

Крайне неинтересно выполнять задачу и ты готов заниматься чем угодно, лишь бы её не делать — если тебе всё-таки очень надо её сделать, попробуй найти в ней новый смысл. Это может быть сложно, а кто сказал, что будет легко :) Представим, тебе нужно сделать какое-то, как тебе кажется, бесполезное задание по учебе, которое делать совершенно не хочется. В этой ситуации можно попробовать усмотреть в этой задаче что-то такое, чего не видно на первый взгляд, например, не навык решать какую-либо задачу, а навык на порядок выше — мыслить системно

Давай ещё быстренько посмотрим, что у тебя с состоянием
"""
    await message.message.answer(text)
    await start_LLIC(message, state, bot)