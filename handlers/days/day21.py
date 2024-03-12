from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from aiogram import types, Bot, F, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.users_stat import Users_stat
from handlers.user_handlers import start_LLIC
from settings import InputMessage, sticker_ids
from utils.is_now_day import is_now_day

day_router21 = Router()


@day_router21.callback_query(Text(text="confirm|21"), any_state)
@is_now_day(21)
async def start_day21(message: CallbackQuery, state: FSMContext, bot: Bot):
    if int(await Users_stat(message.from_user.id).get_user_day()) == int(message.data.split("|")[1]):
        await state.clear()
        await message.message.answer("Первое — мы все разные. Кому-то подойдёт один инструмент, кому-то другой. "
                                      "Любимый инструмент кого-то не будет работать у другого. Поэтому мы рекомендуем попробовать всё, "
                                      "а потом оставить для себя всё самое эффективное")
        await message.message.answer("Второе — важно сформировать намерение. Решить, что ты действительно собираешься следующий месяц "
                                      "уделить личному стресс-менеджменту, чтобы потом пожинать плоды, чувствуя себя лучше, "
                                      "продуктивно работая, испытывая меньше стресса и эффективно справляясь с ним")
        await message.message.answer("Мы считаем, что важно работать сразу над двумя аспектами: и над предупреждением стресса, и над его снижением. "
                                      "Поэтому давай посмотрим на всё, что нам удалось собрать за время программы")

        await message.message.answer("Во-первых, твои основные стрессоры. Выпиши их здесь снова")
        await state.set_state(InputMessage.input_answer_state21_1)


@day_router21.message(F.text, InputMessage.input_answer_state21_1)
@is_now_day(21)
async def answer_day21_1(message: types.Message, state: FSMContext, bot: Bot):
    await message.answer("Во-вторых, что можно сделать, чтобы исключить/минимизировать ✍️")
    await state.set_state(InputMessage.input_answer_state21_2)


@day_router21.message(F.text, InputMessage.input_answer_state21_2)
@is_now_day(21)
async def answer_day21_2(message: types.Message, state: FSMContext, bot: Bot):
    await message.answer("В-третьих, что ты делаешь, когда они возникают, и что бы ты хотел делать (в том числе какие техники применять)?")
    await state.set_state(InputMessage.input_answer_state21_3)


@day_router21.message(F.text, InputMessage.input_answer_state21_3)
@is_now_day(21)
async def answer_day21_3(message: types.Message, state: FSMContext, bot: Bot):
    await state.clear()
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Да, наслышан", callback_data="SMART_Yes|21"))
    keyboard.row(InlineKeyboardButton(text="Да, активно пользуюсь", callback_data="SMART_Using|21"))
    keyboard.row(InlineKeyboardButton(text="Нет, расскажите!", callback_data="SMART_No|21"))
    await message.answer(
        "Теперь выдели из всего этого то, над чем стоит поработать в первую очередь и сформулируй цель — результат, к которому ты хочешь прийти."
        " Знаешь ли ты, как формулируется цель по SMART?", reply_markup=keyboard.as_markup())


@day_router21.callback_query(Text(text="SMART_Yes|21"))
@is_now_day(21)
async def smart_yes_day21(message: CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.answer("Отлично! Немножко освежим:")
    await message.message.answer("SMART – это аббревиатура из английских слов, характеризующих цель. "
                                 "Чтобы достичь успеха, твоя цель должна быть:"
                                 "\n1   Specific – конкретная: тебе нужно отчётливо понимать, как будет выглядеть результат"
                                 "\n2   Measurable – измеримая: подумай, как ты сможешь определить, что цель достигнута "
                                 "(обычно это выражается в цифрах, например, ты можешь решить снизить уровень стресса на 10%, "
                                 "через месяц мы пришлём тебе опросник на уровень стресса, "
                                 "так что пройдя его, ты сможешь оценить, удалось ли тебе это) или убрать 3 конкретных стресс-фактора из твоей работы"
                                 "\n3   Achievable – достижимая: не стоит пытаться разобраться сразу со всеми пунктами стресс-менеджмента, "
                                 "это большая работа, требующая твоего внимания и энергии. "
                                 "Подумай, сколько ресурсов ты готов высвободить под эту задачу в следующем месяце и подбери соответствующую цель"
                                 "\n4   Relevant – значимая: не ставь цель, которую в целом было бы хорошо достичь, "
                                  "выбирай то, с чем тебе важно поработать именно сейчас"
                                 "\n5   Time bound – мы предлагаем тебе поставить цель на месяц, но ты, конечно, можешь выбрать и другой интервал")
    await message.message.answer("Какую же цель ты поставишь?")
    await state.set_state(InputMessage.input_answer_state21_4)


@day_router21.callback_query(Text(text="SMART_Using|21"))
@is_now_day(21)
async def smart_using_day21(message: CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.answer("Отлично! Пойдём дальше)")
    await message.message.answer("Какую же цель ты поставишь?")
    await state.set_state(InputMessage.input_answer_state21_4)


@day_router21.callback_query(Text(text="SMART_No|21"))
@is_now_day(21)
async def smart_no_day21(message: CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.answer("SMART – это аббревиатура из английских слов, характеризующих цель. "
                                 "Чтобы достичь успеха, твоя цель должна быть:"
                                 "\n1   Specific – конкретная: тебе нужно отчётливо понимать, как будет выглядеть результат"
                                 "\n2   Measurable – измеримая: подумай, как ты сможешь определить, что цель достигнута "
                                 "(обычно это выражается в цифрах, например, ты можешь решить снизить уровень стресса на 10%, "
                                 "через месяц мы пришлём тебе опросник на уровень стресса, "
                                 "так что пройдя его, ты сможешь оценить, удалось ли тебе это) или убрать 3 конкретных стресс-фактора из твоей работы"
                                 "\n3   Achievable – достижимая: не стоит пытаться разобраться сразу со всеми пунктами стресс-менеджмента, "
                                 "это большая работа, требующая твоего внимания и энергии. "
                                 "Подумай, сколько ресурсов ты готов высвободить под эту задачу в следующем месяце и подбери соответствующую цель"
                                 "\n4   Relevant – значимая: не ставь цель, которую в целом было бы хорошо достичь, "
                                  "выбирай то, с чем тебе важно поработать именно сейчас"
                                 "\n5   Time bound – мы предлагаем тебе поставить цель на месяц, но ты, конечно, можешь выбрать и другой интервал")
    await message.message.answer("Какую же цель ты поставишь?")
    await state.set_state(InputMessage.input_answer_state21_4)


@day_router21.message(F.text, InputMessage.input_answer_state21_4)
@is_now_day(21)
async def answer_day21_2(message: types.Message, state: FSMContext, bot: Bot):
    await state.clear()
    keyboard = InlineKeyboardBuilder().row(
        InlineKeyboardButton(text="Да", callback_data="SMART_Yes_Final|21"),
        InlineKeyboardButton(text="Нет", callback_data="SMART_No_Final|21")
    )
    await message.answer("Она соответствует всем критериям SMART?", reply_markup=keyboard.as_markup())


@day_router21.callback_query(Text(text="SMART_Yes_Final|21"))
@day_router21.message(F.text, InputMessage.input_answer_state21_5)
@is_now_day(21)
async def smart_yes_final_day21(message: CallbackQuery | Message, state: FSMContext, bot: Bot):
    if type(message) is types.Message:
        await message.answer_sticker(sticker=sticker_ids[4])
        # await message.answer_sticker()
        await message.answer("На сегодня всё 👐 Ты проделал большую работу! Главное — продолжать идти 🙂")
    else:
        # await message.message.answer_sticker()
        await message.message.answer_sticker(sticker=sticker_ids[4])
        await message.message.answer("На сегодня всё 👐 Ты проделал большую работу! Главное — продолжать идти 🙂")
    await Users_stat(message.from_user.id).edit_user_end_day()


@day_router21.callback_query(Text(text="SMART_No_Final|21"))
@is_now_day(21)
async def smart_no_final_day21(message: CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.answer("Попробуй докрутить")
    await state.set_state(InputMessage.input_answer_state21_5)
