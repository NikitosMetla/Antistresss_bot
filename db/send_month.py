import json


class SendMonth:
    def __init__(self, user_id: int | str | None = None):
        self.user_id = str(user_id)
        with open("data/send_month.json", "r", encoding="utf-8") as users:
            self.users = json.load(users)

    async def add_time(self, time):
        self.users[self.user_id] = {"send": False, "timestamp": time}
        await self.save_data()

    async def edit_send(self):
        self.users[self.user_id]["send"] = True
        await self.save_data()

    async def get_users(self):
        return self.users

    async def save_data(self):
        with open("data/send_month.json", "w", encoding="utf-8") as users:
            json.dump(self.users, users, indent=2)