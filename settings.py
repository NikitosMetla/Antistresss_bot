import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage

bot_token = ""
storage = MemoryStorage()

start_text = "Здравствуй, дорогой студент!\nМы рады, что ты решил принять участие в исследовании. Исследование позволит определить, способствуют ли “цифровые помощники” снижению уровня стресса. Если у тебя появятся вопросы или предложения, ты всегда можешь выбрать команду “Связаться с нами”😉\n\nЧтобы поучаствовать в исследовании, необходимо подтвердить, что:\n    •Ты ознакомлен(а) с процедурой проведения исследования и его целя\n    •Тебе была предоставлена возможность задавать вопросы, на все заданные вопросы ты получил(а) удовлетворяющие ответы\n    •Информирован(а) о целях и характере предстоящих процедур\n    •У тебя было достаточно времени, чтобы принять решение об участии в исследовании\n    •Ты понимаешь, что можешь в любое время по собственному желанию отказаться от дальнейшего участия в исследовании, и, если ты это сделаешь, это не повлечёт за собой никаких негативных последствий\n    •Ты добровольно соглашаешься, чтобы твои данные, полученные в ходе исследования, использовались в научных целях и были опубликованы с условием соблюдения принципов анонимности и конфиденциальности."

class InputMessage(StatesGroup):
    not_student = State()
    input_answer_state22_100 = State()
    input_answer_state22_21 = State()
    answer_admin_to_user = State()
    connect_us = State()
    input_answer_state12_2 = State()
    input_answer_state22_20 = State()
    input_answer_state22_15 = State()
    input_answer_state22_14 = State()
    input_answer_state22_13 = State()
    input_answer_state22_12 = State()
    input_answer_state4_4 = State()
    input_answer_state4_3 = State()
    input_answer_state4_2 = State()
    input_answer_state4_1 = State()
    input_answer_state22_11 = State()
    input_answer_state22_9 = State()
    input_answer_state22_8 = State()
    input_answer_state22_7 = State()
    input_answer_state22_6 = State()
    input_answer_state22_5 = State()
    input_answer_state22_4 = State()
    input_answer_state22_3 = State()
    input_answer_state22_2 = State()
    input_answer_state22_1 = State()
    input_answer_state21_5 = State()
    input_answer_state21_4 = State()
    input_answer_state21_3 = State()
    input_answer_state21_2 = State()
    input_answer_state21_1 = State()
    input_answer_state20_3 = State()
    input_answer_state19_7 = State()
    input_answer_state19_6 = State()
    input_answer_state19_5 = State()
    input_answer_state19_4 = State()
    input_answer_state19_3 = State()
    input_answer_state19_1 = State()
    input_answer_state18_1 = State()
    input_answer_state17_1 = State()
    input_answer_state16_7 = State()
    input_answer_state16_6 = State()
    input_answer_state16_5 = State()
    input_answer_state16_1 = State()
    input_answer_state15_2 = State()
    input_answer_state15_1 = State()
    input_answer_state14_4 = State()
    input_answer_state14_2 = State()
    input_answer_state14_1 = State()
    input_answer_state13_4 = State()
    input_answer_state13_3 = State()
    input_answer_state13_2 = State()
    input_answer_state13_1 = State()
    input_answer_state11_5 = State()
    input_answer_state11_4 = State()
    input_answer_state11_3 = State()
    input_answer_state11_2 = State()
    input_answer_state11_1 = State()
    input_answer_state10_5 = State()
    input_answer_state10_4 = State()
    input_answer_state10_3 = State()
    input_answer_state10_2 = State()
    input_answer_state10_1 = State()
    input_answer_state9_5 = State()
    input_answer_state9_4 = State()
    input_answer_state9_3 = State()
    input_answer_state9_2 = State()
    input_answer_state9_1 = State()
    input_answer_state8_5 = State()
    input_answer_state8_4 = State()
    input_answer_state8_3 = State()
    input_answer_state8_2 = State()
    input_answer_state8_1 = State()
    input_answer_state7_4 = State()
    input_answer_state7_3 = State()
    input_answer_state7_2 = State()
    input_answer_state7_1 = State()
    input_answer_state6_3 = State()
    input_answer_state6_2 = State()
    input_answer_state6_1 = State()
    input_answer_state5_1 = State()
    input_answer_state3_4 = State()
    input_answer_state3_3 = State()
    input_answer_state3_2 = State()
    input_answer_state3_1 = State()
    start_state = State()
    state_age = State()
    state_education_direction = State()
    state_job_direction = State()
    enough_job_pro_state = State()
    enough_job_format_state = State()
    work_hours_state = State()
    stress_factors_state = State()
    user_motivation_state = State()
    oprosnik1_state = State()
    statement_user_state = State()

    input_answer_state1 = State()
    input_answer_state1_1 = State()
    input_answer_state1_2 = State()
    input_answer_state2 = State()
    input_answer_state3 = State()
    input_answer_state4 = State()
    input_answer_state5 = State()
    input_answer_state6 = State()
    input_answer_state22 = State()
    input_answer_state7 = State()
    input_answer_state8 = State()
    input_answer_state9 = State()
    input_answer_state10 = State()
    input_answer_state11 = State()
    input_answer_state12 = State()
    input_answer_state13 = State()
    input_answer_state14 = State()
    input_answer_state15 = State()
    input_answer_state16 = State()
    input_answer_state17 = State()
    input_answer_state18 = State()
    input_answer_state19 = State()
    input_answer_state20 = State()
    input_answer_state21 = State()




days_start_questions = {
    "0": "Привет! Ну что, готов приступить к развитию собственной стрессоустойчивости?",
    "1": "Привет! Ну что, готов приступить к развитию собственной стрессоустойчивости?",
    "2": "Привет! Сегодня мы поговорим с тобой о том, что стресс — это состояние неоднородное, имеющее несколько стадий с совершенно разными проявлениями 🧐",
    "3": "Привет! Сегодня с тобой поговорим о признаках стресса)",
    "4": "Привет! Помнишь, перед началом программы ты заполнял большой опросник и по итогу получил график с разными показателями? ",
    "5": "Привет! Чтобы составить план действий по выведению тебя на новый уровень, в котором будет меньше стресса и выше твоя продуктивность, нам надо сначала разобраться с тем, что у тебя стресс вызывает и как он проявляется на разных уровнях. Готов?",
    "6": "Привет!",
    "7": "Привет! Сегодня задачка будет ещё немного сложнее",
    "8": "Привет! Как мы и говорили, эта неделя посвящена факторам развития твоего стресса и его проявлениям. Поэтому сегодня к своим заметкам про причины стресса, мысли, ощущения в теле и эмоции нужно добавить пункт “поведение” — а делаешь то ты что в стрессовой ситуации? Будь внимателен, не упускай кажущиеся на первый взгляд мелочи, хорошо?",
    "9": "Привет! Сегодня задачу усложнять не будем, продолжим наблюдать за теми же моментами: причины, мысли, ощущения в теле, эмоции и действия во время стресса Вечером вернёмся с расспросами 😉",
    "10": "Привет! Сегодня продолжи направлять внимание на причины возникновения напряжения, мысли, ощущения в теле, эмоции и действия во время стресса 👐",
    "11": "Привет! Сегодня завершающий день недели, который мы посвятим фокусу на том, что у тебя вызывает стресс, какие мысли, эмоции, ощущения в теле при этом возникают и что ты в этот момент делаешь) Не забудь вести пометки, вечером спросим😉",
    "12": "Итак, мы с тобой прошли недельный цикл наблюдения за разными факторами и следствиями стресса. Давай теперь проанализируем полученные результаты и составим общую картину",
    "13": "Привет! Вчера ты посмотрел на общую картину возникновения и развития стресса в твоей жизни, сегодня сфокусируемся на стратегиях преодоления стресса",
    "14": "Привет! Вчера мы поговорили о том, какие вообще стратегии совладания со стрессом бывают, а сегодня ты спросишь, что же конкретно делать? Стресс надо предотвращать — он, конечно, природой был не просто так придуман и выполняет важную функцию, но ежедневное действие даже небольшого стресса на длительном отрезке времени может привести к развитию хронического стресса, а там, как мы помним, апатия, отсутствие сил, соматические болезни всякие. Оно нам не надо",
    "15": "Привет! Сегодня мы продолжим говорить о том, как предотвращать стресс и перейдём от общих аспектов к частным, касающимся твоей профессиональной деятельности",
    "16": "Привет! Вчера мы говорили о процессуальной стороне твоей деятельности, сегодня же поговорим о смысловой",
    "17": "Привет! Предыдущие дни мы говорили о том, как предотвратить развитие хронического стресса, но что делать, если он всё-таки тебя настиг?",
    "18": "Привет! Сегодня мы начнём обсуждать конкретные инструменты нормализации состояния при остром стрессе🛠️ Готов включаться?",
    "19": "Привет! Сегодня продолжим говорить про способы нормализации состояния при остром стрессе 👐",
    "20": "Привет! Вчера мы с тобой наконец-то добрались до рефлексивного подуровня и успели поговорить про работу с мыслями, а сегодня переходим к работе с эмоциями 🙂",
    "21": "Привет! Сегодня мы переходим к финальному этапу нашей программы и твоей задачей станет поставить цель развития своей системы стресс-менеджмента на следующий месяц. Но сначала мы обозначим несколько важных моментов",
    "22": "Привет! Сегодня у нас с тобой предпоследний день, но это не повод для грусти!",
}

days_answers = {
    "0": "Готов",
    "1": "Готов",
    "2": "Ого!",
    "3": "Снова?",
    "4": "Ага, вспомнил",
    "5": "Готов",
    "6": "Привет) ",
    "7": "Что на сегодня?",
    "8": "Так точно🫡",
    "9": "Хорошо)",
    "10": "Будет сделано!",
    "11": "Окей",
    "12": "Давай)",
    "13": "Хорошо",
    "14": "Согласен. А делать то что?",
    "15": "Это что-то новенькое!",
    "16": "О, давайте!",
    "17": "Не знаю :(",
    "18": "Готов 🙂",
    "19": "Так, что там ещё?",
    "20": "Погнали",
    "21": "Что же это?",
    "22": "Согласен, не буду грустить",
}

sticker_ids = [
    "CAACAgEAAxkBAAITNGXvir0yWyaBPQmrS78EepokqPUNAALrAQACOA6CEbOGBM7hnEk5NAQ",
    "CAACAgIAAxkBAAITN2XvisQmFa2Tw2Tfsr1hURICk0imAAKPAQACK15TC1JZlsxRJSLCNAQ",
    "CAACAgIAAxkBAAITOmXviskcdeu74aeKTTa7Obx4C05xAAJGAANZu_wlEuv9Ztyr3f00BA",
    "CAACAgIAAxkBAAITPWXvis-chDRyGOkx4l3TQCaSGHKOAAJFDAACep2YSjYZ6HXrpFMsNAQ",
    "CAACAgIAAxkBAAITQGXviuX9WjipXlC-TJINpds2L_jXAAI_AAM7YCQUnpaTS1ey2Tg0BA",
    "CAACAgIAAxkBAAITQ2Xviuo5PfQ_Rpla7IqFxpMjoymJAAKgAAP3AsgPw0cdAaCbwBo0BA",
    "CAACAgIAAxkBAAITRmXviu-3HlULiDQoQSQaXGeT7ydJAAKzAQACFkJrCnhafx6fPWbENAQ",
    "CAACAgIAAxkBAAITSWXvivdktvD7hOXWGKtEglfs26gEAAIxAAMkcWIa4jAl_i3V6u00BA",
    "CAACAgIAAxkBAAITTGXvivwReibdpv4uv8sC2qdGzu-FAAKiAQACFkJrCqF3d2OaToMhNAQ",
    "CAACAgIAAxkBAAITT2XviwTqwgtlg9lnbLHyz7mWd-LKAAKwAQACVp29CpMY9ItOKJbJNAQ",
    "CAACAgIAAxkBAAITUmXvixTtJgAB4B6gUTHegGRHI6cAASIAAk4AA61lvBQhbM5fKyvbPDQE"
]

