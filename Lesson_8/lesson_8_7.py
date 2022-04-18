'''
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
'''


class MyComplexNumber:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'({self.a}+{self.b}j)'

    def __add__(self, others):
        new_a = self.a + others.a
        new_b = self.b + others.b
        return MyComplexNumber(new_a, new_b)

    def __mul__(self, others):
        new_a = self.a * others.a - self.b * others.b
        new_b = self.b * others.a + self.a * others.b
        return MyComplexNumber(new_a, new_b)


z1 = MyComplexNumber(1, 2)
z2 = MyComplexNumber(2, 3)

# проверка

print(f"{z1} + {z2} = ", z1 + z2)
print(f"{z1} * {z2} = ", z1 * z2)

