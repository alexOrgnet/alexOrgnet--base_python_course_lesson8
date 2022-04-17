'''3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.'''


class ErrorCheck:
    def __init__(self):
        self.my_list = []

    def my_numbers(self):

        while True:
            val = input('Введите значения и нажимайте Enter - ')
            if val == 'stop':
                return f'Текущий список - {self.my_list} \n '
            else:
                try:
                    self.my_list.append(int(val))
                except:
                    print(f"Недопустимое значение - строка и булево")



exceptional_input = ErrorCheck()
print(exceptional_input.my_numbers())