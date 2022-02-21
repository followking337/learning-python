"""
DECORATOR PROPERTY

    - Проблема: при использовании свойства property определяется двойной функционал,
        к приватному атрибуту можно обратится как через свойство так и через методы getter, setter и deleter.

    - Решение:

     · Decorator Property --> позволяет создавать свойства, которые в свою очередь устанавливают getter,
        setter и deleter к определенному атрибуту вашего класса (property attribute), к которым возможно обратиться
        только через свойства а не через методы getter, setter и deleter (которые в этот момент являются свойствами).

        - Использование:
            @property  --> по умолчанию создает метод getter

            и затем мы навешиваем setter и deleter:
            @[property].setter
            @[property].deleter

        - Имена методов getter, setter и deleter должны быть одинаковы, если же у одного метода (пр. метод setter)
            будет другое имя оно будет работать как getter и как setter.
"""
x = property()
print(x)  # экземпляр свойства
print(x.getter(90))  # результат вывода является тоже свойства


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
        print('del balance')
        del self.__balance

    my_balance = property()  # my_balance = property(get_balance)
    my_balance = my_balance.getter(get_balance)  # заменяет строчкой выше
    my_balance = my_balance.setter(set_balance)
    my_balance = my_balance.deleter(del_balance)


print('\nproperty():')
a = BankAccount('Ivan', 100)
print(a.my_balance)
a.my_balance = 1000
a.set_balance(1000)
print(a.get_balance())


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # getter
    @property  # --> создали свойство в переменной my_balance  # my_balance = property(my_balance)
    def my_balance(self):
        print('get balance')
        return self.__balance

    # my_property = my_balance  # сохраняем свойство в переменную чтоб оно не затерлось определением функции.

    # setter
    @my_balance.setter  # my_balance = my_property.setter(my_balance)
    def my_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом!')
        self.__balance = value

    # my_property = my_balance  # сохраняем свойство в переменную чтоб оно не затерлось определением функции.

    # deleter
    @my_balance.deleter  # my_balance = my_property.deleter(my_balance)
    def my_balance(self):
        print('del balance')
        del self.__balance


print('\ndecorator property:')
b = BankAccount('Misha', 200)
print(b.my_balance)
# print(b.my_balance())  # AttributeError: 'BankAccount' object has no attribute 'get_balance'
# TypeError: 'int' object is not callable
b.my_balance = 999
print(b.my_balance)
del b.my_balance
# print(b.my_balance)  # AttributeError: 'BankAccount' object has no attribute '_BankAccount__balance'
b.my_balance = 500
print(b.my_balance)
