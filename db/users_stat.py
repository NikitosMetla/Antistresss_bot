import json

from db.day_stat import DAY_STAT


class Users_stat:
    def __init__(self, user_id: int | str | None = ""):
        self.user_id = str(user_id)
        with open("data/users_stat.json", "r", encoding="utf-8") as users:
            self.users = json.load(users)

    async def add_user(self):
        await DAY_STAT().edit_day_stat(0)
        self.users[self.user_id] = {
            "day_now": 0,
            "end_day": 0,
            "last_LLIC": 1,
            "end_LLIC": 0,
            "last_statements": 1,
            "end_statements": 0,
            "LLIC_results": []
        }
        await self.save_data()

    async def append_LLIC_result(self, result):
        self.users[self.user_id]["LLIC_results"].append(result)
        await self.save_data()

    async def get_LLIC_result(self, user_id):
        user_id = str(user_id)
        return self.users.get(user_id).get("LLIC_results")

    async def edit_user_statements(self):
        self.users[self.user_id]["last_statements"] = int(self.users.get(self.user_id).get("last_statements")) + 1
        self.users[self.user_id]["end_statements"] = 0
        await self.save_data()

    async def edit_user_end_statements(self):
        self.users[self.user_id]["end_statements"] = 1
        await self.save_data()

    async def get_user_next_statements(self):
        if self.users.get(self.user_id).get("end_statements"):
            await self.edit_user_statements()
        return int(self.users.get(self.user_id).get("last_statements"))

    async def get_user_next_day(self):
        return int(self.users.get(self.user_id).get("day_now")) + 1

    async def edit_user_LLIC(self):
        self.users[self.user_id]["last_LLIC"] = int(self.users.get(self.user_id).get("last_LLIC")) + 1
        self.users[self.user_id]["end_LLIC"] = 0
        await self.save_data()

    async def edit_user_end_LLIC(self):
        self.users[self.user_id]["end_LLIC"] = 1
        await self.save_data()

    async def get_user_next_LLIC(self):
        if self.users.get(self.user_id).get("end_LLIC"):
            await self.edit_user_LLIC()
        return int(self.users.get(self.user_id).get("last_LLIC"))

    async def edit_user_day(self, edit_day_stat: bool | None):
        next_day = int(self.users.get(self.user_id).get('day_now')) + 1
        self.users[self.user_id]["day_now"] = next_day
        self.users[self.user_id]["end_day"] = 0
        if edit_day_stat is False
            await DAY_STAT().edit_day_stat(next_day)
        await self.save_data()

    async def edit_user_end_day(self):
        self.users[self.user_id]["end_day"] = 1
        await self.save_data()

    async def edit_day_back(self):
        day = int(self.users.get(self.user_id).get('day_now'))
        end_day = self.users.get(self.user_id).get("end_day")
        if end_day == 0:
            self.users[self.user_id]["day_now"] = day - 1
            self.users[self.user_id]["end_day"] = 1
            await self.save_data()

    async def remove_user(self):
        self.users.pop(self.user_id)
        await self.save_data()

    async def get_user_day(self):
        try:
            return int(self.users.get(self.user_id).get("day_now"))
        except:
            return None

    async def get_users_stat(self):
        return self.users

    async def get_user_end_day(self):
        try:
            return int(self.users.get(self.user_id).get("end_day"))
        except:
            return None

    async def save_data(self):
        with open("data/users_stat.json", "w", encoding="utf-8") as users:
            json.dump(self.users, users, indent=2)
