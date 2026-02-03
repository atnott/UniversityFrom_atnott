from datetime import date

class BirthInfo:

    def __init__(self, birth_date):
        if isinstance(birth_date, date):
            self.birth_date = birth_date
        elif isinstance(birth_date, str):
            try:
                self.birth_date = date.fromisoformat(birth_date)
            except ValueError:
                raise ValueError("Некорректный формат даты. Используйте ISO формат: YYYY-MM-DD")
        elif isinstance(birth_date, (list, tuple)):
            if len(birth_date) != 3:
                raise ValueError("Список/кортеж должен содержать ровно 3 элемента: год, месяц, день")
        else:
            raise TypeError("Аргумент переданного типа не поддерживается")

    @property
    def age(self):
        return self.current_age(self.birth_date, date.today())

    @staticmethod
    def current_age(birthday, today):
        ans = today.year - birthday.year
        if (today.month, today.day) < (birthday.month, birthday.day):
            ans -= 1
        return ans

birthinfo = BirthInfo("2025-02-25")
print(birthinfo.age)