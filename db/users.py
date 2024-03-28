import pandas as pd


class Users:
    def __init__(self, user_id: str | int | None = None):
        self.user_id = user_id
        self.users = pd.read_excel('data/users.xlsx', index_col=0)
        for i in self.users.columns:
            self.users[i] = self.users[i].astype(str, int)

    async def add_new_user(self, user_id: str | int):
        if user_id not in self.users.index:
            self.user_id = int(user_id)
            self.users.loc[self.user_id] = [None] * len(self.users.columns)
            await self.save_data()

    async def user_gender(self, gender: str, user_id: str | int):
        user_id = int(user_id)
        # self.users['Пол'] = self.users['Пол'].astype(str)
        self.users.at[user_id, 'Пол'] = gender
        await self.save_data()

    async def user_age(self, age: int | str, user_id: str | int):
        self.users.at[user_id, 'Возраст'] = age
        await self.save_data()

    async def user_course(self, course: str, user_id: str | int):
        user_id = int(user_id)
        self.users['Курс'] = self.users['Курс'].astype(str)
        self.users.at[user_id, 'Курс'] = course
        await self.save_data()

    async def user_education_form(self, education_form: str, user_id: str | int):
        user_id = int(user_id)
        self.users['Форма_обучение'] = self.users['Форма_обучение'].astype(str)
        self.users.at[user_id, 'Форма_обучение'] = education_form
        await self.save_data()

    async def user_education_direction(self, education_direction: str, user_id: str | int):
        user_id = int(user_id)
        self.users['Направл.обр'] = self.users['Направл.обр'].astype(str)
        self.users.at[user_id, 'Направл.обр'] = education_direction
        await self.save_data()

    async def user_job_direction(self, job_direction: str, user_id: str | int):
        user_id = int(user_id)
        self.users.at[user_id, 'Направл.раб'] = job_direction
        await self.save_data()

    async def user_professional_compatibility(self, compatibility: str, user_id: str | int):
        user_id = int(user_id)
        self.users.at[user_id, 'Соотв.проф._работе'] = compatibility
        await self.save_data()

    async def user_work_format(self, work_format: str, user_id: str | int):
        user_id = int(user_id)
        self.users.at[user_id, 'Формат_раб.сотр'] = work_format
        await self.save_data()

    async def user_work_format_full_time(self, work_format: str, user_id: str | int):
        user_id = int(user_id)
        self.users.at[user_id, 'Формат_раб.очн.'] = work_format
        await self.save_data()

    async def user_work_schedule(self, work_schedule: str, user_id: str | int):
        user_id = int(user_id)
        self.users.at[user_id, 'График_работы'] = work_schedule
        await self.save_data()

    async def user_work_hours(self, work_hours: str, user_id: str | int):
        user_id = int(user_id)
        self.users.at[user_id, 'Часы_работы'] = work_hours
        await self.save_data()

    async def user_psychologist_visit(self, psychologist_visit: str, user_id: str | int):
        user_id = int(user_id)
        self.users.at[user_id, 'Посещение_психолога'] = psychologist_visit
        await self.save_data()

    async def user_stress_factors(self, stress_factors: str, user_id: str | int):
        user_id = int(user_id)
        self.users.at[user_id, 'Факторы_стресса'] = stress_factors
        await self.save_data()

    async def user_motivation(self, motivation: str, user_id: str | int):
        user_id = int(user_id)
        self.users.at[user_id, 'Мотивация_участия'] = motivation
        await self.save_data()

    async def user_isk(self,numbers_isc, isk_value: int, user_id: str | int):
        user_id = int(user_id)
        self.users.at[user_id, f'ИСК_{numbers_isc}'] = isk_value
        await self.save_data()

    async def user_isk_level(self,number_isc, isk_level: str, user_id: str | int):
        user_id = int(user_id)
        self.users.at[user_id, f'ур.ИСК_{number_isc}'] = isk_level
        await self.save_data()

    async def user_fatigue(self, number_test: int, fatigue_value: int, user_id: str | int):
        user_id = int(user_id)
        self.users.at[user_id, f'Утомление_{number_test}'] = fatigue_value
        await self.save_data()

    async def user_fatigue_level(self, number_test: int, fatigue_level: str, user_id: str | int):
        user_id = int(user_id)
        self.users.at[user_id, f'ур.Утомления_{number_test}'] = fatigue_level
        await self.save_data()

    async def user_monotony(self, number_test: int, monotony_value: int, user_id: str | int):
        user_id = int(user_id)
        self.users.at[user_id, f'Монотония_{number_test}'] = monotony_value
        await self.save_data()

    async def user_monotony_level(self, number_test: int, monotony_level: str, user_id: str | int):
        user_id = int(user_id)
        self.users.at[user_id, f'ур.Монотонии_{number_test}'] = monotony_level
        await self.save_data()

    async def user_saturation(self, number_test: int, saturation_value: int, user_id: str | int):
        user_id = int(user_id)
        self.users.at[user_id, f'Пресыщение_{number_test}'] = saturation_value
        await self.save_data()

    async def user_saturation_level(self, number_test: int, saturation_level: str, user_id: str | int):
        user_id = int(user_id)
        self.users.at[user_id, f'ур.Пресыщения_{number_test}'] = saturation_level
        await self.save_data()

    async def user_stress(self, number_test: int, stress_value: int, user_id: str | int):
        user_id = int(user_id)
        self.users.at[user_id, f'Стресс_{number_test}'] = stress_value
        await self.save_data()

    async def user_stress_level(self, number_test: int, stress_level: str, user_id: str | int):
        user_id = int(user_id)
        self.users.at[user_id, f'ур.Стресса_{number_test}'] = stress_level
        await self.save_data()

    async def user_self_progress(self, self_progress: int, user_id: str | int):
        user_id = int(user_id)
        self.users.at[user_id, 'Самооц.прогресса'] = self_progress
        await self.save_data()

    async def save_data(self):
        self.users.to_excel('data/users.xlsx')