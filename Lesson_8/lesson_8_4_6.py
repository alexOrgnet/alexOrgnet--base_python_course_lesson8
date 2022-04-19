
'''4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
'''


class WareHouse:
    def __init__(self, name):
        self.name = name
        self.storage = {}

    def __str__(self):
        return f' {self.name}'


class Order:
    def __init__(self, goods, location_from, location_to):
        self.goods = goods
        self.location_from = location_from
        self.location_to = location_to
        self._quantity = 0

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        try:
            self._quantity = int(quantity)
        except:
            self._quantity = 0
            print("Quantity is not set as integer. Please try to enter quantity again")

        # self.quantity = quantity

    # @classmethod
    def move(self):
        whs_goods_from = self.location_from.storage
        whs_goods_to = self.location_to.storage

        whs_goods_from[self.goods] = -self.quantity
        whs_goods_to[self.goods] = self.quantity

        print(
            f'Перемещены товары {self.goods} в количестве {self.quantity} со склада {self.location_from} на склад {self.location_to} \n ')


class Goods:

    def __init__(self, model, price):
        self.price = price
        self.model = model

    def __str__(self):
        return f' модель {self.model} цена {self.price}'


class Printer(Goods):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(Goods):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(Goods):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


# создаем 2 товара

printer = Printer('Canon', 100)

scanner = Scanner('Epson', 80)

warehouse_central = WareHouse('Центральный склад')

warehouse_central.storage[printer] = 20

warehouse_branch = WareHouse('Склад филиала')

warehouse_branch.storage[scanner] = 30

# утром отгружаем принтеры с центрального склада на склад филиала

printer_quantity = input('Введите количество принтеров отгружаемых с центрального склада на склад филиала')

order1 = Order(printer, warehouse_central, warehouse_branch)

order1.quantity = printer_quantity

order1.move()

# вечером возвращаем сканнеры со склада филиала на центральный склад

scanner_quantity = input('Введите количество сканеров возвращаемых со склада филиала на центральный склад')

order2 = Order(scanner, warehouse_branch, warehouse_central)

order2.quantity = scanner_quantity

order2.move()

print(f'движение товара {printer} на складе {warehouse_central}: {warehouse_central.storage[printer]}')
print(f'движение товара {printer} на складе {warehouse_branch}: {warehouse_branch.storage[printer]}')

print(f'движение товара {scanner} на складе {warehouse_central}: {warehouse_central.storage[scanner]}')
print(f'движение товара {scanner} на складе {warehouse_branch}: {warehouse_branch.storage[scanner]}')