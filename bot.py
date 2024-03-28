import asyncio

from aiogram import Dispatcher, Bot

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from db.users_stat import Users_stat
from handlers.days.day1 import day_router2
from handlers.days.day10 import day_router10
from handlers.days.day11 import day_router11
from handlers.days.day12 import day_router12
from handlers.days.day13 import day_router13
from handlers.days.day14 import day_router14
from handlers.days.day15 import day_router15
from handlers.days.day16 import day_router16
from handlers.days.day17 import day_router17
from handlers.days.day18 import day_router18
from handlers.days.day19 import day_router19
from handlers.days.day2 import day_router1
from handlers.days.day20 import day_router20
from handlers.days.day21 import day_router21
from handlers.days.day22 import day_router22
from handlers.days.day3 import day_router3
from handlers.days.day4 import day_router4
from handlers.days.day5 import day_router5
from handlers.days.day6 import day_router6
from handlers.days.day7 import day_router7
from handlers.days.day8 import day_router8
from handlers.days.day9 import day_router9
from handlers.user_handlers import user_router
from keyboards import confirm_keyboard
from settings import storage, days_start_questions, bot_token

bot = Bot(token=bot_token, parse_mode="html")

async def main():
    print(await bot.get_me())
    data = await edit_data()
    await asyncio.sleep(7)
    await message_after_start(data)
    await asyncio.sleep(5)
    await bot.delete_webhook(drop_pending_updates=True)
    dp = Dispatcher(storage=storage)
    dp.include_routers(user_router, day_router1, day_router2, day_router3, day_router4, day_router5, day_router6,
                       day_router7, day_router8, day_router9, day_router10, day_router11, day_router12, day_router13, day_router14,
                       day_router15, day_router16, day_router17, day_router18, day_router19, day_router20, day_router21, day_router22)
    scheduler = AsyncIOScheduler()
    scheduler.add_job(func=call_next_day, trigger="cron", hour=10, minute=4)
    scheduler.add_job(func=call_remind_user_day, trigger="cron", hour=18, minute=30)
    scheduler.start()
    await dp.start_polling(bot)


async def message_after_start(users_without_end):
    for user in users_without_end:
        user_data = Users_stat(user)
        next_day = int(await user_data.get_user_day()) + 1
        try:
            if next_day <= 22:
                await user_data.edit_user_day(edit_day_stat=False)
                keyboard = await confirm_keyboard(str(next_day))
                await bot.send_message(text="Кажется, что-то пошло не так и день ты не закончил…Давай, все-таки, пройдем его сегодня целиком?\n\n"
                                            + days_start_questions.get(str(next_day)), chat_id=user, reply_markup=keyboard.as_markup())
        except:
            continue

async def edit_data():
    users_data = await Users_stat().get_users_stat()
    users_without_end = []
    for user in users_data.keys():
        end_day = int(users_data.get(user).get("end_day"))
        if end_day == 0:
            users_without_end.append(user)
    for user in users_without_end:
        await Users_stat(user).edit_day_back()
    # tasks = [asyncio.create_task(Users_stat(users).edit_day_back()) for users in users_data]
    # await asyncio.gather(*tasks)
    users_data = await Users_stat().get_users_stat()
    return users_without_end


async def remind_user(user_id, bot: Bot):
    try:
        day = await Users_stat(user_id).get_user_day()
        if not(await Users_stat(user_id).get_user_end_day()) and day not in [5, 6, 7, 8, 9, 10, 11, 12, 14]:
            await bot.send_message(chat_id=user_id, text="Ты куда пропал?) Давай закончим сегодняшнее задание, осталось немного!)")
    except:
        return


async def call_remind_user_day():
    users_data = await Users_stat().get_users_stat()
    task_list = [asyncio.create_task(remind_user(user_id=user_id, bot=bot)) for user_id in users_data.keys()]
    await asyncio.gather(*task_list)


async def mailing_next_day(next_day: int, user_id, replace: bool, bot: Bot):
    try:
        user = Users_stat(user_id)
        if next_day <= 22:
            if replace:
                await user.edit_user_day()
                keyboard = await confirm_keyboard(str(next_day))
                await bot.send_message(text=days_start_questions.get(str(next_day)), chat_id=user_id, reply_markup=keyboard.as_markup())
            elif next_day in [5, 6, 7, 8, 9, 10, 11, 12, 14]:
                await bot.send_message(
                    text="Привет)Не забудь выполнить задание👐",
                    chat_id=user_id)
            else:
                await bot.send_message(text="Мы остановились с тобой на кое-чем интересном! Ответь, пожалуйста, на последний заданный вопрос или продолжи программу!", chat_id=user_id)
    except:
        return

async def call_next_day():
    users_data = await Users_stat().get_users_stat()
    task_list1 = [asyncio.create_task(mailing_next_day(users_data.get(user).get("day_now") + 1, user_id=user, bot=bot, replace=True))
                  if users_data.get(user).get("end_day")
                  else asyncio.create_task(mailing_next_day(users_data.get(user).get("day_now"), bot=bot, user_id=user,
                                                            replace=False))
                  for user in users_data.keys()]
    await asyncio.gather(*task_list1)


if __name__ == "__main__":
    asyncio.run(main())
