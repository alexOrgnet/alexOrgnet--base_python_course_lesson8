
'''2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.'''


class DivideByNullError:
    def __init__(self, denominator, divider):
        self.denominator = denominator
        self.divider = divider

    @classmethod
    def divide_by_null(cls, denominator, divider):
        try:
            return divider / denominator
        except:
            return (f"Деление на ноль недопустимо")


div = DivideByNullError(100, 10)
print(DivideByNullError.divide_by_null(0, 100))
print(DivideByNullError.divide_by_null(1, 1000))
print(div.divide_by_null(0, 100))
