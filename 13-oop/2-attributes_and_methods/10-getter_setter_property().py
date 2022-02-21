"""
GETTER, SETTER, PROPERTY

    - Проблема: при публичных атрибутах есть доступ к ним вне класса, а также возможность их изменять.

    - Решение:

        1. Мы не на прямую обращаемся к защищенной переменной а через два метода getter и setter:
        · getter --> это специальный метод, позволяющий получить доступ к приватному атрибуту.
            def getter(self):
                return self.__attribute

        · setter --> это специальный метод, дающий возможность присвоить новое значение приватному атрибуту.
            def setter(self, argument):
                if [condition]:
                    self.__attribute = argument

        · deleter --> это специальный метод, дающий возможность удалять приватный атрибут.
            def deleter(self):
                del self.__attribute

        Вызов методов getter и setter не очень интуитивно, поэтому есть класс property...

        2. property (свойство) --> class, позволяет установить getter, setter и deleter
            к определенному атрибуту вашего класса (property attribute).

            [property] = property(fget=, fset=, fdel=) --> уже не атрибут а свойство.

            [object].property --> тут срабатывает метод get который возвращает защищенный атрибут.
            [object].getter()

            [object].property = value --> тут срабатывает метод set который назначает защищенный атрибут.
            [object].setter()

            del [object].property --> тут срабатывает метод del который удаляет защищенный атрибут.
            [object].deleter()
"""


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


a = BankAccount('Ivan', 100)
print(a.name, a.balance)
a.balance = 'hello'
print(a.name, a.balance)
print(a.__dict__)


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # getter
    def get_balance(self):
        return self.__balance

    # setter
    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом!')
        self.__balance = value


print('\ngetter, setter:')
b = BankAccount('Tania', 200)
print(b.get_balance())
b.set_balance(999)
print(b.get_balance())
# b.set_balance('hello')  # ValueError: Баланс должен быть числом!
print(b.__dict__)


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # getter
    def get_balance(self):
        print('get balance')
        return self.__balance

    # setter
    def set_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом!')
        self.__balance = value

    # deleter
    def del_balance(self):
        print('delete balance')
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=del_balance)


print('\nproperty(fget=, fset=, fdel=):')
c = BankAccount('Misha', 400)
print(c.balance)
print(c.get_balance())
c.balance = 700
c.set_balance(700)
print(c.balance)
print(c.get_balance())
del c.balance
# print(c.balance)  # AttributeError: 'BankAccount' object has no attribute '_BankAccount__balance'
c.balance = 800
print(c.balance)
print(c.__dict__)
