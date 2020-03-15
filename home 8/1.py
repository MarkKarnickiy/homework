class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)
    @classmethod
    def extract(cls, day_month_year):
        date_list = []
        for i in day_month_year.split():
            if i != ' ': date_list.append(i)
        return int(date_list[0]), int(date_list[1]), int(date_list[2])
    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            pass
        else:
            return f'Что?'
        if 1 <= month <= 12:
            pass
        else:
            return f'Не понял?'
        if 2019 >= year >= 0:
            return f'Nice'
        else:
             return f'А это еще что такое?'
    def __str__(self):
        return f'Дата на сегодня {Data.extract(self.day_month_year)}'


today = Data('15 7 2018')
print(today)
print(Data.valid(89, 10, 2067))
print(today.valid(26, 78, 2018))
print(Data.extract('9 9 2019'))
print(today.extract('6 12 2021'))
print(Data.valid(1, 1, 2001))
