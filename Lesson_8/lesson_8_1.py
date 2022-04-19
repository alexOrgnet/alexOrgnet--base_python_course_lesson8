
'''1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.'''

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def excavate(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def validate(day, month, year):

        error_exists = ''

        if 1 <= day <= 31:
            pass
        else:
            error_exists += ' Неправильный день'

        if 1 <= month <= 12:
            pass
        else:
            error_exists += ' Неправильный месяц'

        if 2022 >= year >= 0:
            pass
        else:
            error_exists += ' Неправильный год'

        if error_exists != '':
            return error_exists
        else:
            return f'Date is in correct formatt'



    def __str__(self):
        return f'Текущая дата {Data.excavate(self.day_month_year)}'


today = Data('14 - 12 - 2021')
print(today)
print(Data.validate(24, 2, 2022))
print(today.validate(24, 2, 2022))
print(Data.excavate('24 - 2 - 2022'))
print(today.excavate('24 - 2 - 2022'))

