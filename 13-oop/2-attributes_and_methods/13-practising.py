"""
Проблема:
    1. Есть доступ к атрибутам и методам вне класса.
    2. Есть возможность изменить атрибуты без ограничений.

Решение:
    1. Ограничить доступ к атрибутам и методам вне класса.
    2. Определить ограничения при изменении данных атрибутов.

Через property:
    1. Отлавливаем момент (событие) при доступе к атрибутам и методам вне класса и повлиять на него через getter.
    2. Отлавливаем момент (событие) при изменении атрибута и повлиять на него через setter.
"""
from string import digits


class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password  # password is property, not private attribute (__password)
        self.__secret = 'abracadabra'

    @property
    def password(self):
        print('getter called')
        return self.__password

    @property
    def secret(self):
        s = input('Введите ваш пароль: ')
        if s == self.password:
            return self.__secret
        else:
            raise ValueError('Доступ закрыт!!!')

    @staticmethod  # функция лежит в области видимости класса
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @password.setter
    def password(self, value):
        print('setter called')
        if not isinstance(value, str):
            raise TypeError('Пароль должен быть строкой')
        if len(value) < 4:
            raise ValueError('Длина пароля слишком мала, минимум должно быть 4 символа')
        if len(value) > 12:
            raise ValueError('Длина пароля слишком велика, максимум должно быть 12 символов')
        if not User.is_include_number(value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        self.__password = value


a = User('followking', '11223')  # при инициализации объекта сразу срабатывает password property setter
print(a.password)
a.password = 'qwerty123'
print(a.password)
print(a.secret)
