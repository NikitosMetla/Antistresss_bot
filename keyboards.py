from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from settings import days_answers

confirm_keyboard = InlineKeyboardBuilder()
confirm_keyboard.row(InlineKeyboardButton(text="Подтверждаю", callback_data="confirm"))

gender_keyboard = InlineKeyboardBuilder()
gender_keyboard.row(InlineKeyboardButton(text="Мужской", callback_data="gender|male"))
gender_keyboard.row(InlineKeyboardButton(text="Женский", callback_data="gender|female"))

course_keyboard = InlineKeyboardBuilder()
courses = "1 курс бакалавриата, 2 курс бакалавриата, 3 курс бакалавриата, 4 курс бакалавриата, 1 курс магистратуры, 2 курс магистратуры, 1 курс специалитета, 2 курс специалитета, 3 курс специалитета, 4 курс специалитета, 5 курс специалитета, 6 курс специалитета, я не студент".split(", ")
for i in range(len(courses) - 1):
    course_keyboard.row(InlineKeyboardButton(text=courses[i], callback_data="course|" + courses[i]))
course_keyboard.row(InlineKeyboardButton(text="я не студент", callback_data="NOT_STUDENT"))

education_form_keyboard = InlineKeyboardBuilder()
education_form_keyboard.row(InlineKeyboardButton(text="очная(дневная)", callback_data="education_form|очная(дневная)"))
education_form_keyboard.row(InlineKeyboardButton(text="очно-заочная(вечерняя)",
                                                 callback_data="education_form|очно-заочная(вечерняя)"))
education_form_keyboard.row(InlineKeyboardButton(text="вечерняя", callback_data="education_form|вечерняя"))


job_pro_keyboard = InlineKeyboardBuilder()
job_pro_keyboard.row(InlineKeyboardButton(text="Да", callback_data="job_pro|Yes"))
job_pro_keyboard.row(InlineKeyboardButton(text="Нет", callback_data="job_pro|No"))
job_pro_keyboard.row(InlineKeyboardButton(text="Другое", callback_data="job_pro|Enough"))

format_job_keyboard = InlineKeyboardBuilder()
format_job_keyboard.row(InlineKeyboardButton(text="Сотрудник", callback_data="form_job|Сотрудник"))
format_job_keyboard.row(InlineKeyboardButton(text="Фрилансер", callback_data="form_job|Фрилансер"))
format_job_keyboard.row(InlineKeyboardButton(text="Другое", callback_data="form_job|Enough"))

format_job_fulltime_keyboard = InlineKeyboardBuilder()
format_job_fulltime_keyboard.row(InlineKeyboardButton(text="Очный", callback_data="form_job_fulltime|Очный"))
format_job_fulltime_keyboard.row(InlineKeyboardButton(text="Дистанционный", callback_data="form_job_fulltime|Дистанционный"))
format_job_fulltime_keyboard.row(InlineKeyboardButton(text="Гибридный", callback_data="form_job_fulltime|Гибридный"))

work_schedule_keyboard = InlineKeyboardBuilder()
work_schedule_keyboard.row(InlineKeyboardButton(text="Фиксированный", callback_data="work_schedule|Фиксированный"))
work_schedule_keyboard.row(InlineKeyboardButton(text="Гибкий", callback_data="work_schedule|Гибкий"))

visit_psychology_keyboard = InlineKeyboardBuilder()
visit_psychology_keyboard.row(InlineKeyboardButton(text="Да", callback_data="visit_psychology|Yes"))
visit_psychology_keyboard.row(InlineKeyboardButton(text="Нет", callback_data="visit_psychology|No"))

ready_stress_keyboard = InlineKeyboardBuilder()
ready_stress_keyboard.row(InlineKeyboardButton(text="Готов", callback_data="ready_stress"))


async def confirm_keyboard(day: int | str):
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text=days_answers.get(str(day)), callback_data=f"confirm|{day}"))
    return keyboard