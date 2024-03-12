import json


class DAY_STAT:
    def __init__(self):
        with open("data/day_stat.json", "r", encoding="utf-8") as users:
            self.users = json.load(users)

    async def get_day_stat(self):
        return [value for value in self.users.values()]

    async def edit_day_stat(self, day: str | int):
        day = str(day)
        self.users[day] = self.users.get(day) + 1
        if day != "0":
            self.users[str(int(day) - 1)] = self.users.get(str(int(day) - 1)) - 1
        await self.save_data()

    async def save_data(self):
        with open("data/day_stat.json", "w", encoding="utf-8") as users:
            json.dump(self.users, users, indent=2)