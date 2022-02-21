"""
PUBLIC PROTECTED PRIVATE
    Attributes and Methods

        - Уровни доступа:

            · Public: атрибуты и методы доступны как внутри класса так и вне класса.

            · Protected: атрибуты и методы все же доступны вне класса.
                Применение --> конвенция на уровне согласования среди разработчиков что данные атрибуты и методы лучше
                    не использовать вне класса, только внутри класса, но доступ к ним вне класса все же есть.

            · Private: позволяют закрыть доступ к данным вне нашего класса, мы скрываем (инкапсулируем) логику работы
                нашей программы от пользователя и предоставляем ему только конечный результат.
                · Инкапсуляция - метод, при помощи которого, происходит закрытие обработки
                    защищенных атрибутов и методов.
                · Предоставляем метод пользователю для работы с данными, через этот метод пользователь
                    получает доступ к защищенным данным, тем самым пользователь не может обратится к ним на прямую.
                · К private атрибутам и методам все же можно обратиться не на прямую:
                    - print(dir(obj))
                    - print(obj._[class]__[attribute or method])

        - Module accessify включает в себя два декоратора для полной защиты приватных атрибутов и методов.
"""


class BankAccount:

    def __init__(self, name, balance, passport):
        self.name = name
        self.balance = balance
        self.passport = passport

    def print_public_data(self):
        print(self.name, self.balance, self.passport)


account1 = BankAccount('Bob', 100000, 'AE454513R')

print('\n\tДоступ внутри класса:')
account1.print_public_data()

print('\n\tДоступ вне класса:')
print(account1.name)
print(account1.balance)
print(account1.passport)

print('\nProtected:')


class BankAccount:

    def __init__(self, name, balance, passport):
        self._name = name
        self._balance = balance
        self._passport = passport

    def print_protected_data(self):
        print(self._name, self._balance, self._passport)


account1 = BankAccount('Bob', 100000, 'AE454513R')

print('\n\tДоступ внутри класса:')
account1.print_protected_data()

print('\n\tДоступ вне класса:')
print(account1._name)
print(account1._balance)
print(account1._passport)

print('\nPrivate:')


class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_private_data(self):
        print(self.__name, self.__balance, self.__passport)


account1 = BankAccount('Bob', 100000, 'AE454513R')

print('\n\tДоступ внутри класса:')
account1.print_private_data()

print('\n\tДоступ вне класса:')
# print(account1.__name)
# print(account1.__balance)
# print(account1.__passport)  # AttributeError: 'BankAccount' object has no attribute '__name'
print(dir(account1))
print(account1._BankAccount__passport)

print('\nPrivate Method:')


class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_public_data(self):  # инкапсуляция
        self.__print_private_data()

    def __print_private_data(self):  # private method
        print(self.__name, self.__balance, self.__passport)


account1 = BankAccount('Bob', 100000, 'AE454513R')

print('\n\tДоступ внутри класса:')
account1.print_public_data()

print('\n\tДоступ вне класса:')
# account1.__print_private_data()  # AttributeError: 'BankAccount' object has no attribute '__print_private_data'
print(dir(account1))
account1._BankAccount__print_private_data()
