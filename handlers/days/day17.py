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

day_router17 = Router()

@day_router17.callback_query(Text(text="confirm|17"), any_state)
@is_now_day(17)
async def start_day17(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.edit_reply_markup()
    await state.clear()
    keyboard = InlineKeyboardBuilder()
    question = await message.message.answer(
        "Если ты вспомнишь стадии развития стресса, о которых мы говорили в самом начале программы, то сам придешь к выводу, что первый шаг — обратится к врачу, так как стадия истощения характеризуется целым рядом соматических проблем."
        " Вероятно, тебе потребуется фармакотерапия или витаминотерапия для восстановления баланса в организме💊"
        "\n\nКроме того, врач скорее всего порекомендует длительный отдых. И мы тоже рекомендуем. Если в таком состоянии продолжать работать, восстановление будет идти крайне медленно, если вообще будет идти…"
        "\n\nИ на этом можно было закончить…но мы прекрасно понимаем, что не у всех есть возможность совсем приостановить деятельность, поэтому рекомендуем:"
        "\n1. Максимально соблюдать предписания врача"
        "\n2. Наладить work-life balance — если вариант не работать и/или не учиться совсем из области фантастики (хотя, вероятно, всё-таки возможен, если хорошо подумать), то нужно постараться снизить нагрузку и четко её ограничить (человек на этой стадии в целом уже не в состоянии много работать, поэтому может растягивать задачи на весь день и выходные, не оставляя времени на качественный полноценный отдых)"
        "\n3. Делать все то, о чем мы говорили предыдущие 3 дня:"
        "\n     • замечать и устранять/минимизировать стрессоры"
        "\n     • нормализовать питьевой режим, режимы питания и сна"
        "\n     • регулярно заниматься физической активностью и выходить на прогулки на свежем воздухе"
        "\n     • создать комфортные условия дома и на рабочем месте"
        "\n     • оптимизировать процессы"
        "\n     • сбалансировать режим труда и отдыха в течении рабочего/учебного дня"
        "\n     • чередовать задания и формы активной занятости"
        "\n     • определить смысл своей деятельности"
        "\n     • наладить взаимодействие с другими людьми"
        "\n     • Кроме того, не забывай привносить в свою жизнь маленькие и большие радости."
        "\n\nПодумай сейчас и напиши, какие 33 вещи/события/действия/т.д. приносят тебе удовольствие 🤔"
    )
    await state.set_state(InputMessage.input_answer_state17_1)
    await state.update_data(question=str(await Users_stat(message.from_user.id).get_user_day()) + ". " + question.text)


@day_router17.message(F.text, InputMessage.input_answer_state17_1)
@is_now_day(17)
async def answer_day17_1(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question = data.get("question")
    answers = Answers()
    await answers.add_answer(question=question, answer=message.text, user_id=message.from_user.id)
    await state.clear()
    await message.answer_sticker(sticker=sticker_ids[-3])
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Да! Спасибо, что напомнили", callback_data="YES|17"))
    keyboard.row(InlineKeyboardButton(text="Никогда не забываю себя радовать😄", callback_data="YES|17"))
    await message.answer("Есть что-то из этого списка, что хотелось бы привнести в жизнь в ближайшее время?", reply_markup=keyboard.as_markup())


@day_router17.callback_query(Text(text="YES|17"))
@is_now_day(17)
async def end_day17(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.answer("Отлично! У нас ещё остались методы активного изменения собственного состояния, о них мы поговорим в ближайшие дни 😉")
    await message.message.answer("На сегодня все👐")
    await Users_stat(message.from_user.id).edit_user_end_day()