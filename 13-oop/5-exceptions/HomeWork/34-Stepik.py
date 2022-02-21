class Wallet:

    def __init__(self, currency: str, balance):
        if type(currency) != str:
            raise TypeError('Неверный тип валюты')
        if len(currency) != 3:
            raise NameError('Неверная длина названия валюты')
        if not currency.isupper():
            raise ValueError('Название должно состоять только из заглавных букв')
        self.currency = currency
        self.balance = balance

    def __eq__(self, other):
        if not isinstance(other, Wallet):
            raise TypeError(f'Wallet не поддерживает сравнение с {other}')
        if self.currency != other.currency:
            raise ValueError('Нельзя сравнить разные валюты')
        return self.balance == other.balance

    def exception(self, other):
        if not isinstance(other, Wallet) or self.currency != other.currency:
            raise ValueError('Данная операция запрещена')

    def __add__(self, other):
        self.exception(other)
        return Wallet(self.currency, self.balance + other.balance)

    def __sub__(self, other):
        self.exception(other)
        return Wallet(self.currency, self.balance - other.balance)


a = Wallet('EUR', 100)
b = Wallet('EUR', 250)
c = Wallet('USD', 50)

print(a.currency, a.balance)
print(a == b)
# print(a == c)  # ValueError: Нельзя сравнить разные валюты
# print(a == 5)  # TypeError: Wallet не поддерживает сравнение с 5
tt = a + b
print(tt.currency, tt.balance)
# rr = a + c
# ss = a + 5

wallet1 = Wallet('USD', 50)
wallet2 = Wallet('RUB', 100)
wallet3 = Wallet('RUB', 150)
# wallet4 = Wallet(12, 150)                 # исключение TypeError('Неверный тип валюты')
# wallet5 = Wallet('qwerty', 150)           # исключение NameError('Неверная длина названия валюты')
# wallet6 = Wallet('abc', 150)              # исключение ValueError('Название должно состоять только из заглавных букв')
print(wallet2 == wallet3)                 # False
# print(wallet2 == 100)                     # TypeError('Wallet не поддерживает сравнение с 100')
# print(wallet2 == wallet1)                 # ValueError('Нельзя сравнить разные валюты')
wallet7 = wallet2 + wallet3
print(wallet7.currency, wallet7.balance)  # печатает 'RUB 250'
# wallet2 + 45                              # ValueError('Данная операция запрещена')
