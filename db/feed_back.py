import asyncio
import pandas as pd


class FEED_BACK:
    def __init__(self, user_id: str | int | None = None):
        self.user_id = user_id
        self.users = pd.read_excel('data/feed_back.xlsx', index_col=0)
        for i in self.users.columns:
            self.users[i] = self.users[i].astype(str, int)

    async def add_new_user(self, user_id: str | int):
        if user_id not in self.users.index:
            self.user_id = int(user_id)
            self.users.loc[self.user_id] = [None] * len(self.users.columns)
            await self.save_data()

    async def question0(self, user_id, answer):
        user_id = int(user_id)
        self.users.at[user_id, "Как ты думаешь, с чем связана такая динамика?"] = answer
        await self.save_data()

    async def question1(self, user_id, answer):
        user_id = int(user_id)
        self.users.at[user_id, "Что изменилось вследствие прохождения программы?"] = answer
        await self.save_data()

    async def question2(self, user_id, answer):
        user_id = int(user_id)
        self.users.at[user_id, "Что изменилось в твоем поведении?"] = answer
        await self.save_data()

    async def question3(self, user_id, answer):
        user_id = int(user_id)
        self.users.at[user_id, "Что изменилось в твоем самоощущении, в том числе в стрессовых ситуациях и после них?"] = answer
        await self.save_data()

    async def question4(self, user_id, answer):
        user_id = int(user_id)
        self.users.at[user_id, "Какие инструменты, с которыми мы тебя познакомили, ты будешь использовать?"] = answer
        await self.save_data()

    async def question5(self, user_id, answer):
        user_id = int(user_id)
        self.users.at[user_id, "Как ты оцениваешь свой прогресс в совладании со стрессом по шкале от 1 до 7, где 7 — максимальное значение?"] = answer
        await self.save_data()

    async def question6(self, user_id, answer):
        user_id = int(user_id)
        self.users.at[user_id, "Любая обратная связь от тебя"] = answer
        await self.save_data()

    async def question7(self, user_id, answer):
        user_id = int(user_id)
        self.users.at[user_id, "Ух ты! Как тебе результаты?"] = answer
        await self.save_data()

    async def question8(self, user_id, answer):
        user_id = int(user_id)
        self.users.at[user_id, "Что ты замечал за этот месяц?"] = answer
        await self.save_data()

    async def question9(self, user_id, answer):
        user_id = int(user_id)
        self.users.at[user_id, "Что изменилось в твоем поведении?"] = answer
        await self.save_data()

    async def question10(self, user_id, answer):
        user_id = int(user_id)
        self.users.at[user_id, "Что изменилось в твоем самоощущении, в том числе в стрессовых ситуациях и после них?"] = answer
        await self.save_data()

    async def question11(self, user_id, answer):
        user_id = int(user_id)
        self.users.at[user_id, "Какие инструменты, с которыми мы тебя познакомили, ты использовал?"] = answer
        await self.save_data()

    async def question12(self, user_id, answer):
        user_id = int(user_id)
        self.users.at[user_id, "Любая обратная связь от тебя"] = answer
        await self.save_data()

    async def save_data(self):
        self.users.to_excel('data/feed_back.xlsx')