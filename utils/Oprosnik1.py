import io

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from matplotlib import pyplot as plt

from db.users_stat import Users_stat

questions = {
    '1 вопрос': ['сильный\nслабый', [3, 2, 1, 0, 1, 2, 3], [7, 6, 5, 4, 3, 2, 1]],
    '2 вопрос': ['веселый\nгрустный', [3, 2, 1, 0, 1, 2, 3], [7, 6, 5, 4, 3, 2, 1]],
    '3 вопрос': ['сонный\nбодрый', [3, 2, 1, 0, 1, 2, 3], [1, 2, 3, 4, 5, 6, 7]],
    '4 вопрос': ['спокойный\nвзволнованный', [3, 2, 1, 0, 1, 2, 3], [7, 6, 5, 4, 3, 2, 1]],
    '5 вопрос': ['счастливый\nнесчастный', [3, 2, 1, 0, 1, 2, 3], [7, 6, 5, 4, 3, 2, 1]],
    '6 вопрос': ['ленивый\nэнергичный', [3, 2, 1, 0, 1, 2, 3], [1, 2, 3, 4, 5, 6, 7]],
    '7 вопрос': ['свежий\nусталый', [3, 2, 1, 0, 1, 2, 3], [7, 6, 5, 4, 3, 2, 1]],
    '8 вопрос': ['расслабленный\nнапряженный', [3, 2, 1, 0, 1, 2, 3], [7, 6, 5, 4, 3, 2, 1]],
    '9 вопрос': ['полный сил\nистощенный', [3, 2, 1, 0, 1, 2, 3], [7, 6, 5, 4, 3, 2, 1]],
    '10 вопрос': ['скучный\nзаинтересованный', [3, 2, 1, 0, 1, 2, 3], [1, 2, 3, 4, 5, 6, 7]]
}


async def oprosnik1_keyboard(question: str, number_test: int, last_question: int, points: int):
    keyboard = InlineKeyboardBuilder()
    data = questions.get(question)
    for i in range(7):
        if i == 0:
            keyboard.row(InlineKeyboardButton(text=str(data[1][i]) + " — " + data[0].split("\n")[0],
                                              callback_data=f"answer_oprosnik{number_test}|"
                                                            f"{last_question + 1}|" + str(points + data[2][i])))
        elif i == 6:
            keyboard.row(InlineKeyboardButton(text=str(data[1][i]) + " — " + data[0].split("\n")[1],
                                              callback_data=f"answer_oprosnik{number_test}|"
                                                            f"{last_question + 1}|" + str(points + data[2][i])))
        else:
            keyboard.row(InlineKeyboardButton(text=str(data[1][i]),
                                              callback_data=f"answer_oprosnik{number_test}|"
                                                            f"{last_question + 1}|" + str(points + data[2][i])))
    return keyboard


async def generate_plot_statements(user_id):
    results = await Users_stat().get_LLIC_result(user_id)
    results = [int(x) for x in results]
    parametrs = [f"{i + 1}" for i in range(len(results))]
    plt.plot(parametrs, results, color='blue', marker='o', linestyle='-')
    plt.ylim(0, 80)
    plt.xlabel('ЗАМЕРЫ')
    plt.ylabel('ЗНАЧЕНИЯ')
    # plt.savefig(f"data/LLIC_users/LLIC_{user_id}.png")
    buffer = io.BytesIO()

    # Сохраняем график в буфер
    plt.savefig(buffer, format='png')

    # Очищаем график из памяти
    plt.close()

    # Получаем байты из буфера
    buffer.seek(0)
    byte_data = buffer.read()

    return byte_data
