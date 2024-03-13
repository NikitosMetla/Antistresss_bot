import asyncio

from aiogram import Router, types, Bot, F
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state
from aiogram.types import BufferedInputFile, InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.admins import Admin
from db.day_stat import DAY_STAT
from db.users import Users
from db.users_stat import Users_stat
from keyboards import confirm_keyboard, gender_keyboard, course_keyboard, job_pro_keyboard, education_form_keyboard, \
    format_job_keyboard, format_job_fulltime_keyboard, work_schedule_keyboard, visit_psychology_keyboard, \
    ready_stress_keyboard
from settings import start_text, InputMessage
from utils.Oprosnik1 import oprosnik1_keyboard, generate_plot_statements
from utils.is_main_admin import is_main_admin
from utils.is_now_day import is_now_day
from utils.statements_user import statements, statements_keyboard, level_state, generate_plot

user_router = Router()


@user_router.message(Text(text="/admin"), any_state)
@is_main_admin
async def start(message: types.Message, state: FSMContext, bot: Bot):
    text = "Статистика по дню:"
    results = await DAY_STAT().get_day_stat()
    for i in range(len(results)):
        text += f"\n{i} день: {results[i]}"
    await message.answer(text=text)
    await message.answer_document(document=FSInputFile("data/users.xlsx"))
    await message.answer_document(document=FSInputFile("data/answers.xlsx"))
    await message.answer_document(document=FSInputFile("data/feed_back.xlsx"))


@user_router.message(F.text, InputMessage.connect_us)
async def start(message: types.Message, state: FSMContext, bot: Bot):
    await state.clear()
    admin_id = await Admin().get_admins()
    admin_id = admin_id[1]
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Ответить пользователю", callback_data=f"admin_answer_user|{message.from_user.id}"))
    await bot.send_message(chat_id=admin_id, text=f"Сообщение от пользователя с id {message.from_user.id}:\n{message.text}",
                           reply_markup=keyboard.as_markup())


@user_router.callback_query(Text(startswith="admin_answer_user|"), any_state)
async def start(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    data = message.data.split("|")
    user_id = data[1]
    message_delete = message.message.message_id
    await state.set_state(InputMessage.answer_admin_to_user)
    await state.update_data(user_id=user_id, message_delete=message_delete)
    await message.message.answer(f"Ты отвечаешь пользователю с id {user_id}")


@user_router.message(F.text, InputMessage.answer_admin_to_user)
async def start(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    user_id = data.get("user_id")
    message_delete = data.get("message_delete")
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Вы ответили", callback_data=f"sqwertyuiop"))
    await bot.send_message(chat_id=user_id, text=f"Сообщение от администратора бота:\n{message.text}")
    await bot.edit_message_reply_markup(chat_id=message.from_user.id, message_id=message_delete,
                                        reply_markup=keyboard.as_markup())
    await state.clear()


@user_router.message(Text(text="/start"), any_state)
async def start(message: types.Message, state: FSMContext, bot: Bot):
    user = Users_stat(message.from_user.id)
    user_day = await user.get_user_day()
    if user_day is None:
        await state.clear()
        keyboard = await confirm_keyboard(0)
        await message.answer(start_text, reply_markup=keyboard.as_markup())
        await message.delete()
    else:
        await message.reply("Ты уже прошел этап знакомства, продолжи с того момента,"
                            " где ты в последний раз остановился!")



@user_router.callback_query(Text(text="confirm|0"), any_state)
async def start(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await state.clear()
    user = Users_stat(message.from_user.id)
    await user.add_user()
    await message.message.answer("Укажи, пожалуйста, свой пол", reply_markup=gender_keyboard.as_markup())
    await message.message.delete()


@user_router.callback_query(Text(startswith="gender|"))
@is_now_day(0)
async def start(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    users = Users()
    await call.message.answer('В программе мы будем обращаться к тебе в мужском роде как к "студенту". Не удивляйся 😉')
    await users.add_new_user(user_id=call.from_user.id)
    await users.user_gender(gender=call.data.split("|")[1], user_id=call.from_user.id)
    await call.message.answer("Укажи, пожалуйста, свой возраст")
    await state.set_state(InputMessage.state_age)
    await call.message.delete()


@user_router.message(F.text, InputMessage.state_age)
@is_now_day(0)
async def start(message: types.Message, state: FSMContext, bot: Bot):
    await Users().user_age(age=message.text, user_id=message.from_user.id)
    await message.answer("Укажи, пожалуйста, твой курс ", reply_markup=course_keyboard.as_markup())
    await state.clear()


@user_router.callback_query(Text(startswith="course|"))
@is_now_day(0)
async def start(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    await Users().user_course(course=call.data.split("|")[1], user_id=call.from_user.id)
    await call.message.answer("Укажи, пожалуйста, форму обучения", reply_markup=education_form_keyboard.as_markup())
    await call.message.delete()


@user_router.callback_query(Text(startswith="NOT_STUDENT"), any_state)
@is_now_day(0)
async def start(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    await call.message.answer("Мы очень рады, что ты заинтересовался нашей программой)) К сожалению, так как мы проводим исследование, мы не можем предложить тебе прохождение программы")
    await state.set_state(InputMessage.not_student)
    await call.message.delete()

@user_router.callback_query(Text(startswith="education_form|"), any_state)
@is_now_day(0)
async def start(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    await Users().user_education_form(education_form=call.data.split("|")[1], user_id=call.from_user.id)
    await call.message.answer("Укажи, пожалуйста, направление образования, которое ты получаешь")
    await state.set_state(InputMessage.state_education_direction)


@user_router.message(F.text, InputMessage.state_education_direction)
@is_now_day(0)
async def start(message: types.Message, state: FSMContext, bot: Bot):
    await Users().user_education_direction(education_direction=message.text, user_id=message.from_user.id)
    await message.answer("Укажи, пожалуйста, твоё направление работы")
    await state.set_state(InputMessage.state_job_direction)


@user_router.message(F.text, InputMessage.state_job_direction)
@is_now_day(0)
async def start(message: types.Message, state: FSMContext, bot: Bot):
    await Users().user_job_direction(job_direction=message.text, user_id=message.from_user.id)
    await message.answer("Ты работаешь по профессии?", reply_markup=job_pro_keyboard.as_markup())
    await state.clear()


@user_router.callback_query(Text(startswith="job_pro|"), any_state)
@is_now_day(0)
async def start(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    if call.data.split("|")[1] != "Enough":
        await Users().user_professional_compatibility(compatibility=call.data.split("|")[1], user_id=call.from_user.id)
        await call.message.answer("Твой формат работы?", reply_markup=format_job_keyboard.as_markup())
    else:
        await call.message.answer("Напиши, пожалуйста, что ты подразумеваешь под другим")
        await state.set_state(InputMessage.enough_job_pro_state)


@user_router.message(F.text, InputMessage.enough_job_pro_state)
@is_now_day(0)
async def start(message: types.Message, state: FSMContext, bot: Bot):
    await Users().user_job_direction(job_direction="Другое: " + message.text, user_id=message.from_user.id)
    await message.answer("Твой формат работы?", reply_markup=format_job_keyboard.as_markup())
    await state.clear()


@user_router.callback_query(Text(startswith="form_job|"), any_state)
@is_now_day(0)
async def start(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    if call.data.split("|")[1] != "Enough":
        await Users().user_work_format(work_format=call.data.split("|")[1], user_id=call.from_user.id)
        await call.message.answer("Твой формат работы?", reply_markup=format_job_fulltime_keyboard.as_markup())
    else:
        await call.message.answer("Напиши, пожалуйста, что ты подразумеваешь под другим")
        await state.set_state(InputMessage.enough_job_format_state)


@user_router.message(F.text, InputMessage.enough_job_format_state)
@is_now_day(0)
async def start(message: types.Message, state: FSMContext, bot: Bot):
    await Users().user_work_format(work_format="Другое: " + message.text, user_id=message.from_user.id)
    await message.answer("Твой формат работы?", reply_markup=format_job_fulltime_keyboard.as_markup())
    await state.clear()


@user_router.callback_query(Text(startswith="form_job_fulltime|"), any_state)
@is_now_day(0)
async def start(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    await Users().user_work_format_full_time(work_format=call.data.split("|")[1], user_id=call.from_user.id)
    await call.message.answer("Твой график работы?", reply_markup=work_schedule_keyboard.as_markup())


@user_router.callback_query(Text(startswith="work_schedule|"), any_state)
@is_now_day(0)
async def start(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    await Users().user_work_schedule(work_schedule=call.data.split("|")[1], user_id=call.from_user.id)
    await call.message.answer("Какое количество часов в неделю ты работаешь?")
    await state.set_state(InputMessage.work_hours_state)


@user_router.message(F.text, InputMessage.work_hours_state)
@is_now_day(0)
async def start(message: types.Message, state: FSMContext, bot: Bot):
    await Users().user_work_hours(work_hours=message.text, user_id=message.from_user.id)
    await message.answer("Посещаешь ли ты психолога/психотерапевта?",
                         reply_markup=visit_psychology_keyboard.as_markup())
    await state.clear()


@user_router.callback_query(Text(startswith="visit_psychology|"), any_state)
@is_now_day(0)
async def start(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    await Users().user_psychologist_visit(psychologist_visit=call.data.split("|")[1], user_id=call.from_user.id)
    await call.message.answer("Назови, пожалуйста, 3 основные стресс-фактора, с которыми ты сталкиваешься в"
                              " учебной и профессиональной деятельности")
    await state.set_state(InputMessage.stress_factors_state)


@user_router.message(F.text, InputMessage.stress_factors_state)
@is_now_day(0)
async def start(message: types.Message, state: FSMContext, bot: Bot):
    await Users().user_stress_factors(stress_factors=message.text, user_id=message.from_user.id)
    await message.answer("Почему ты решил принять участие в исследовании?")
    await state.set_state(InputMessage.user_motivation_state)


@user_router.message(F.text, InputMessage.user_motivation_state)
@is_now_day(0)
async def start(message: types.Message, state: FSMContext, bot: Bot):
    await Users().user_motivation(motivation=message.text, user_id=message.from_user.id)
    await state.clear()
    await message.answer("Ух! Теперь посмотрим на твой уровень стресса)"
                         " Для этого тебе нужно ответить на 50 вопросов 🙂 Готов? ",
                         reply_markup=ready_stress_keyboard.as_markup())


@user_router.callback_query(Text(text="ready_stress"), any_state)
async def start_LLIC(call: types.CallbackQuery | types.Message, state: FSMContext, bot: Bot):
    number_test = await Users_stat(call.from_user.id).get_user_next_LLIC()
    if type(call) is types.CallbackQuery:
        await call.message.delete()
        await call.message.answer("Тебе предлагается ряд шкал, в каждой из которых нужно выбрать то значение, которое наиболее"
                             " точно характеризует твоё состояние <b>В НАСТОЯЩИЙ МОМЕНТ</b>."
                             " Помни, что нужно выбрать <b>только одно</b> значение по каждой шкале")
    else:
        await call.answer(
            "Тебе предлагается ряд шкал, в каждой из которых нужно выбрать то значение, которое наиболее"
            " точно характеризует твоё состояние <b>В НАСТОЯЩИЙ МОМЕНТ</b>."
            " Помни, что нужно выбрать <b>только одно</b> значение по каждой шкале")
    keyboard = await oprosnik1_keyboard("1 вопрос", number_test, last_question=0, points=0)
    await state.set_state(InputMessage.oprosnik1_state)
    await state.update_data(last_question=1)
    if type(call) is types.CallbackQuery:
        await call.message.answer("Выбери значение, которое отображает твое состояние в настоящий момент:",
                                  reply_markup=keyboard.as_markup())
    else:
        await call.answer("Выбери значение, которое отображает твое состояние в настоящий момент:",
                                  reply_markup=keyboard.as_markup())


@user_router.callback_query(Text(startswith="answer_oprosnik"), InputMessage.oprosnik1_state)
async def start(call: types.CallbackQuery | types.Message, state: FSMContext, bot: Bot):
    data = call.data.split("|")
    number_test = int(data[0][15:])
    point = await state.get_data()
    point = point.get("last_question")
    isc, last_question = int(data[2]), int(data[1])
    if point is None or (int(point) != last_question):
        return
    if last_question == 10:
        if isc >= 62:
            level = "Высокий уровень субъективного комфорта"
        elif 54 <= isc <= 61:
            level = "Повышенный уровень субъективного комфорта"
        elif 48 <= isc <= 53:
            level = "Приемлемый уровень субъективного комфорта"
        elif 41 <= isc <= 47:
            level = "Сниженный уровень субъективного комфорта"
        else:
            level = "Низкий уровень субъективного комфорта"
        await Users().user_isk(numbers_isc=number_test, isk_value=isc, user_id=call.from_user.id)
        await Users().user_isk_level(number_isc=number_test, isk_level=level, user_id=call.from_user.id)
        caption = "По результатам данного опроса у тебя тебя " + level.lower() + "(" + str(isc) + ")"
        user = Users_stat(call.from_user.id)
        await user.edit_user_end_LLIC()
        await user.append_LLIC_result(isc)
        if number_test != 1:
            photo = await generate_plot_statements(user_id=call.from_user.id)
            await call.message.answer_photo(photo=BufferedInputFile(file=photo, filename="huy.png"), caption=caption)
        else:
            await call.message.answer(text=caption)
        if number_test == 1  or number_test == 13:
            await call.message.answer("Тебе предлагается ряд высказываний, характеризующих чувства и ощущения,"
                                      " которые могут возникать у тебя в процессе работы. Прочитай, пожалуйста,"
                                      " внимательно каждое из них и оцени, насколько оно соответствует твоим обычным"
                                      " переживаниям во время рабочего дня")
            await state.set_state(InputMessage.statement_user_state)
            await state.update_data(last_statement=1)
            next_test = await user.get_user_next_statements()
            keyboard = await statements_keyboard(number_test=next_test, last_statement=0, points="")
            await call.message.answer(statements.get("1 утверждение"), reply_markup=keyboard.as_markup())
        elif number_test == 12:
            await dinamic_22(call, state, bot)
        else:
            await state.clear()
            if type(call) is types.CallbackQuery:
                await call.message.answer("На сегодня все👐")
            else:
                await call.answer("На сегодня все👐")
            await user.edit_user_end_day()
    else:
        keyboard = await oprosnik1_keyboard(f"{last_question + 1} вопрос", number_test,
                                            last_question=last_question, points=isc)
        await call.message.answer("Выбери значение, которое отображает твое состояние сейчас:",
                                  reply_markup=keyboard.as_markup())
        await state.update_data(last_question=last_question + 1)


@user_router.callback_query(Text(startswith="statements_user"), InputMessage.statement_user_state)
async def start(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    data = call.data.split("|")
    number_test = int(data[0][-1])
    point = await state.get_data()
    point = point.get("last_statement")
    points, last_statement = data[2], int(data[1])
    if point is None or (int(point) != last_statement):
        return
    if last_statement == 40:
        points_list = [int(i) for i in list(points)]
        fatigue = (sum([points_list[int(i) - 1] for i in "9, 11, 12, 21, 32".split(", ")]) -
                   sum([points_list[int(i) - 1] for i in "2, 10, 14, 27, 28".split(", ")]) + 25)
        monotony = (sum([points_list[int(i) - 1] for i in "5, 6, 16, 23, 24, 33, 35".split(", ")]) -
                    sum([points_list[int(i) - 1] for i in "3, 25, 30".split(", ")]) + 15)
        satiety = (sum([points_list[int(i) - 1] for i in "4, 13, 15, 19, 36, 39".split(", ")]) -
                   sum([points_list[int(i) - 1] for i in "1, 17, 20, 26".split(", ")]) + 20)
        stress = (sum([points_list[int(i) - 1] for i in "7, 18, 22, 31, 34, 37, 40".split(", ")]) -
                  sum([points_list[int(i) - 1] for i in "8, 29, 38".split(", ")]) + 15)
        level_fatigue = await level_state(object="Утомление", number=fatigue)
        level_monotony = await level_state(object="Монотония", number=monotony)
        level_satiety = await level_state(object="Пресыщение", number=satiety)
        level_stress = await level_state(object="Стресс", number=stress)
        caption = (f"Твой результат по пройденным методикам👇\n"
                   f"{level_fatigue} - {fatigue}\n"
                   f"{level_monotony} - {monotony}\n"
                   f"{level_satiety} - {satiety}\n"
                   f"{level_stress} - {stress}")
        data_list = [fatigue, monotony, satiety, stress]
        photo = await generate_plot(numbers=data_list, user_id=call.from_user.id)
        await call.message.answer_photo(photo=BufferedInputFile(file=photo, filename="huy.png"),
                                        caption=caption)
        user = Users_stat(call.from_user.id)
        await user.edit_user_end_day()
        await user.edit_user_end_statements()
        await Users().user_fatigue(number_test=number_test, fatigue_value=fatigue, user_id=call.from_user.id)
        await Users().user_monotony(number_test=number_test, monotony_value=monotony, user_id=call.from_user.id)
        await Users().user_saturation(number_test=number_test, saturation_value=satiety, user_id=call.from_user.id)
        await Users().user_stress(number_test=number_test, stress_value=stress, user_id=call.from_user.id)
        await Users().user_fatigue_level(number_test=number_test, fatigue_level=level_fatigue, user_id=call.from_user.id)
        await Users().user_monotony_level(number_test=number_test, monotony_level=level_monotony, user_id=call.from_user.id)
        await Users().user_saturation_level(number_test=number_test, saturation_level=level_satiety, user_id=call.from_user.id)
        await Users().user_stress_level(number_test=number_test, stress_level=level_stress, user_id=call.from_user.id)
        if number_test == 3:
            await call.message.answer("Ну вот и всё! Ты — большой молодец, что вложил время и силы в свое саморазвитие."
                                      " Думаем, это окупится сполна спользуй полученные знания во благо своего состояния, а мы вернёмся через месяц, чтобы посмотреть, удалось ли тебе интегрировать пройденную программу в свою жизнь👐")
            await state.clear()
            await asyncio.sleep(30*24*60*60)
            await call.message.answer("Привет! Месяц назад ты закончил проходить нашу программу 🤩Давай посмотрим, как изменилось твоё состояние?")
            await start_LLIC(call, state, bot)
            return
        elif number_test == 1:
            await call.message.answer("Интересно, как можно расшифровать все эти данные и чем различаются эти понятия?"
                                  " Об этом ты совсем скоро узнаешь в нашей программе😉")
            await call.message.answer("На сегодня все👐")
        elif number_test == 4:
            keyboard = InlineKeyboardBuilder()
            keyboard.row(InlineKeyboardButton(text="😍", callback_data="answer|23😍"))
            keyboard.row(InlineKeyboardButton(text="🙂", callback_data="answer|23🙂"))
            keyboard.row(InlineKeyboardButton(text="😟", callback_data="answer|23😟"))
            await call.message.answer("Ух ты! Как тебе результаты?", reply_markup=keyboard.as_markup())
        else:
            await call.message.answer("На сегодня все👐")
        await state.clear()
    else:
        keyboard = await statements_keyboard(number_test=number_test, last_statement=last_statement, points=points)
        await state.update_data(last_statement=int(point) + 1)
        await call.message.answer(f"{statements.get(str(last_statement + 1) + ' утверждение')}",
                                  reply_markup=keyboard.as_markup())


async def start_statement_next_days(message: types.Message | types.CallbackQuery, state: FSMContext, bot: Bot):
    if type(message) == types.CallbackQuery:
        await message.message.answer("Тебе предлагается ряд высказываний, характеризующих чувства и ощущения,"
                                  " которые могут возникать у тебя в процессе работы. Прочитай, пожалуйста,"
                                  " внимательно каждое из них и оцени, насколько оно соответствует твоим обычным"
                                  " переживаниям во время рабочего дня")
    else:
        await message.answer("Тебе предлагается ряд высказываний, характеризующих чувства и ощущения,"
                                     " которые могут возникать у тебя в процессе работы. Прочитай, пожалуйста,"
                                     " внимательно каждое из них и оцени, насколько оно соответствует твоим обычным"
                                     " переживаниям во время рабочего дня")
    await state.set_state(InputMessage.statement_user_state)
    await state.update_data(last_statement=1)
    user = Users_stat(message.from_user.id)
    next_test = await user.get_user_next_statements()
    keyboard = await statements_keyboard(number_test=next_test, last_statement=0, points="")
    if type(message) == types.CallbackQuery:
        await message.message.answer(statements.get("1 утверждение"), reply_markup=keyboard.as_markup())
    else:
        await message.answer(statements.get("1 утверждение"), reply_markup=keyboard.as_markup())


async def dinamic_22(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    await message.message.answer("Как ты думаешь, с чем связана такая динамика?")
    await state.set_state(InputMessage.input_answer_state22_100)
