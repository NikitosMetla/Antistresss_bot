import asyncio
from aiogram import types, Dispatcher, Router, F, Bot
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.users_stat import Users_stat
from handlers.user_handlers import start_LLIC
from settings import InputMessage, sticker_ids
from utils.is_now_day import is_now_day

day_router18 = Router()


@day_router18.callback_query(Text(text="confirm|18"), any_state)
@is_now_day(18)
async def start_day18(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    if int(await Users_stat(message.from_user.id).get_user_day()) == int(message.data.split("|")[1]):
        await state.clear()
        keyboard = InlineKeyboardBuilder()
        keyboard.row(InlineKeyboardButton(text="Подышал 🙂", callback_data="BREATHED|18"))
        await message.message.answer(
            "Итак, мы с тобой не зря разбирали уровни проявления стресса (физиологический, психологический и поведенческий), ведь на каждом из них можно и нужно работать!"
            "\n\nНачнём с физиологического уровня — что на нём можно сделать? Если тебе в голову пришла идея про спорт, то мы крайне рады, ведь это значит, что физическая активность присутствует в твоей жизни, что, безусловно, оказывает положительное влияние на твоё состояние. И если в момент сильного напряжения у тебя есть возможность пойти побегать, это, конечно, здорово, но… маловероятно😁 Поэтому мы предложим тебе инструменты, которые можно использовать быстро и в любой обстановке😉\n"
            "\n<b>Первое</b> — это, конечно, дыхание. Самое универсальное, но от того не менее эффективное средство. \n\nПопробуй прямо сейчас: постарайся расслабить мышцы и направить своё внимание на дыхание (можешь положить руку на живот, если тебе так будет легче сфокусироваться). Следи за тем, чтобы вдох был короче, чем выдох (примерно в два раза). Если сконцентрироваться не получается, начни обратный отсчёт: 100 — вдох, 100 — выдох, 99 — вдох, 99 — выдох и тд. Попробуй, попробуй, заблокируй телефон на пару минут и сконцентрируйся на дыхании, вдруг тебе понравится и это станет твоей палочкой-выручалочкой ",
            reply_markup=keyboard.as_markup()
        )


@day_router18.callback_query(Text(text="BREATHED|18"))
@is_now_day(18)
async def after_breathing_day18(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Напрягся 💪", callback_data="TENSED|18"))
    await message.message.answer(
        "Хорошо. В момент острого стресса продолжай фокусироваться на своём размеренном дыхании пока не почувствуешь, что напряжение постепенно уходит (или столько минут, сколько у тебя есть в распоряжении, очевидно)"
        "\n\n<b>Вторым</b> простым и доступным каждому инструментом является напряжение мышц тела: на 5-7 секунд напряги все"
        " мышцы тела примерно на 7 баллов, где 10 — максимальное напряжение. Сделай паузу на несколько секунд и повтори"
        " ещё несколько раз, пока не почувствуешь, что напряжение стало отступать. Если тебя никто не видит (или ты не"
        " из стеснительных), не забудь также напрячь мышцы лица (морщины от этого не появятся, не переживай). \nПопробуй сделать прямо сейчас. Если просто прочитаешь, то ни за что не вспомнишь об этом лайфхаке, когда напряжение тебя настигнет",
        reply_markup=keyboard.as_markup()
    )


@day_router18.callback_query(Text(text="TENSED|18"))
@is_now_day(18)
async def after_tensing_day18(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Сделал, что там дальше?", callback_data="DONE|18"))
    await message.message.answer(
        "Отлично, идем дальше\n\n<b>Третий</b> способ является своеобразным миксом первых двух: глубоко вдохни и медленно выдохни. Поставь обе ступни на пол. Почувствуй, как они упираются в пол (если ты совсем не чувствуешь своих ног, делай технику в движении). Пройдись внутренним взором по своему телу: от кончиков пальцев ног до макушки головы. Что ты чувствуешь? В каких частях тела есть напряжение? Если напряжение во всём теле, используй предыдущий способ. Если напряжение в отдельных частях тела, поочередно напрявляй туда своё внимание и с каждым выдохом расслабляй эту часть тела всё сильнее"
        "\nЕсли ты не понаслышке знаком с практикой медитаций, то выполнение этого упражнения не составит для тебя труда. Если ты никогда ничего подобного не пробовал, обязательно сделай это упражнение прямо сейчас. Как минимум, это новый необычный опыт, как максимум — этот инструмент станет твоим любимым способом регуляции состояния",
        reply_markup=keyboard.as_markup()
    )

@day_router18.callback_query(Text(text="DONE|18"))
@is_now_day(18)
async def continue_psycho_day18(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Ага, нашёл", callback_data="FOUND|18"))
    await message.message.answer(
        "А дальше мы переходим с тобой на новый уровень😁 Психологический. Как ты помнишь, там 2 компонента: перцептивный и рефлексивный"
        "\n\nПерцепция — это восприятие, и тут фокус в том, что в момент, когда тебя накрывает волной страха и мыслей о том, что всё пропало, переключить своё внимание на что-то во вне. Например, найти в окружающей обстановке 7 предметов какого-либо цвета. Прямо сейчас оглянись вокруг и найди 7 предметов синего цвета (если синий в интерьере преобладает, выбери какой-нибудь другой цвет)",
        reply_markup=keyboard.as_markup()
    )


@day_router18.callback_query(Text(text="FOUND|18"))
@is_now_day(18)
async def continue_psycho2_day18(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Ок", callback_data="OK|18"))
    await message.message.answer(
        "Ну как? Есть ощущение, что ты очнулся? Конечно, само по себе это действие не поможет тебе сразу вернуться к продуктивной работе (если, конечно, не делать его достаточно долго), но оно поможет остановить поток негативных мыслей и чувств, а дальше уже можно применить другие способы"
        "\n\nПохожий на этот инструмент, но немного более временно затратный, предполагает концентрацию не разных каналах восприятия:"
        "\n     • Выбери 5 окружающих тебя объектов и рассмотри их"
        "\n     • Сконцентрируйся на 5 тактильных ощущениях: это может быть то, к чему ты можешь прикоснуться, или то, что ты ощущаешь постоянно, но не замечаешь (например, ощущение того, как одежда прилегает к телу)"
        "\n     • Выдели три звука в окружающей тебя обстановке"
        "\n     • Постарайся ощутить 2 разных запаха"
        "\n     • Распробуй что-то на вкус (может у тебя есть шоколадка в закромах?)",
        reply_markup=keyboard.as_markup()
    )


@day_router18.callback_query(Text(text="OK|18"))
@is_now_day(18)
async def end_day18(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.answer_sticker(sticker=sticker_ids[2])
    await message.message.answer(
        "Хорошо) Мы с тобой сегодня попробовали много инструментов, какой из них ты используешь завтра в случае возникновения напряжения?"
    )
    await state.set_state(InputMessage.input_answer_state18_1)


@day_router18.message(F.text, InputMessage.input_answer_state18_1)
@is_now_day(18)
async def answer_day18_1(message: types.Message, state: FSMContext, bot: Bot):
    await message.answer("Давай ещё быстренько посмотрим, что у тебя с состоянием")
    await state.clear()
    await start_LLIC(message, state, bot)

