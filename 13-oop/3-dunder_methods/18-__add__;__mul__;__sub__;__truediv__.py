"""
DOUBLE UNDERSCORE (dunder) METHODS
    Магические Методы
    __method__ --> методы внутри класса
        · Вызываются (срабатывают):
            1. автоматически в определенный момент времени.
            2. вручную через [instance].__method__()

        __add__ --> срабатывает когда экземпляр класса участвует в операции сложения:
            - [instance] + int/float/str == [instance].__add__(int/float/str)
            - int/float/str + [instance] == [instance].__radd__(int/float/str)
            - [instance1] + [instance2]  == [instance2] + [instance1]

        __mul__ --> срабатывает когда экземпляр класса участвует в операции умножения:
            - [instance] * int/float/str == [instance].__mul__(int/float/str)
            - int/float/str * [instance] == [instance].__mul__(int/float/str)
            - [instance1] * [instance2]  == [instance2] + [instance1]

        __sub__ --> срабатывает когда экземпляр класса участвует в операции вычитания:
            - [instance] - int/float/str == [instance].__sub__(int/float/str)
            - int/float/str - [instance] == [instance].__sub__(int/float/str)
            - [instance1] - [instance2]  == [instance2] + [instance1]

        __truediv__ --> срабатывает когда экземпляр класса участвует в операции деления:
            - [instance] / int/float/str == [instance].__truediv__(int/float/str)
            - int/float/str / [instance] == [instance].__truediv__(int/float/str)
            - [instance1] / [instance2]  == [instance2] / [instance1]

        · TypeError: unsupported operand type(s) for +: 'BankAccount' and 'int' --> когда метод __add__ не определен
        · TypeError: unsupported operand type(s) for +: 'int' and 'BankAccount' --> когда метод __radd__ не определен
"""


class BankAccount:

    def __init__(self, name, balance):
        print('__init__ called')
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print('__add__ called')
        # if isinstance(other, (int, float)):
        #     return self.balance + other
        if isinstance(other, (int, float)):
            return BankAccount(self.name, self.balance + other)  # тут возвращается совершено новый объект
        if isinstance(other, str):
            return self.name + ' ' + other
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        raise NotImplemented

    def __radd__(self, other):
        print('__radd__ called')
        return self + other

    def __repr__(self):
        return f'Клиент {self.name} с балансом {self.balance}'


a = BankAccount('Ivan', 78)
b = BankAccount('Tanya', 900)
print(a.balance)
print(a.balance + 400)

print('\n[instance] + int/float:')
print(a + 12)       # TypeError: unsupported operand type(s) for +: 'BankAccount' and 'int'
print(12 + a)       # TypeError: unsupported operand type(s) for +: 'int' and 'BankAccount'

print('\n[instance] + str:')
print(a + 'hello')  # TypeError: unsupported operand type(s) for +: 'BankAccount' and 'str'
print('hello' + a)  # TypeError: unsupported operand type(s) for +: 'str' and 'BankAccount'

print('\n[instance] + [instance]:')
print(a + b)
print(b + a)
