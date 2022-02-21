# Словарь для брута, most common-passwords.txt содержит англоязычные самые распространённые пароли.
with open('common-passwords.txt', 'r') as file:
    data = file.read().split('\n')
# print(type(data))
# print(data)


class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def password(self):
        print('getter called')
        return self.__password

    @staticmethod
    def is_weak(password):
        if password in data:
            return True
        return False

    @password.setter
    def password(self, value):
        print('setter called')
        if not isinstance(value, str):
            raise TypeError('Пароль должен быть строкой')
        if len(value) < 4:
            raise ValueError('Длина пароля слишком мала, минимум должно быть 4 символа')
        if User.is_weak(value):
            raise ValueError('Пароль слабый, введите другой пароль')
        self.__password = value


a = User('followking', '11223')
print(a.password)
a.password = 'admin'
print(a.password)
