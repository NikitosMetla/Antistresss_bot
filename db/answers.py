import pandas as pd


class Answers:
    def __init__(self, user_id: str | int | None = None):
        self.user_id = user_id
        self.users = pd.read_excel('data/answers.xlsx', index_col=0)
        for i in self.users.columns:
            self.users[i] = self.users[i].astype(str, int)

    async def add_new_user(self, user_id: str | int):
        if user_id not in self.users.index:
            self.user_id = int(user_id)
            self.users.loc[self.user_id] = ["1"]
            await self.save_data()

    async def add_answer(self, question: str, answer: str, user_id: str | int):
        if question not in self.users.columns:
            self.users[question] = pd.Series(dtype="object")
        self.users.at[user_id, question] = answer
        await self.save_data()

    async def save_data(self):
        self.users.to_excel('data/answers.xlsx')