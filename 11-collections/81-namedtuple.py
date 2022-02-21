from collections import namedtuple
from typing import NamedTuple
from datetime import datetime

person = ('Megan', 'Jones', '1998-07-16', 'Bolivia')
print(person.__sizeof__())
# В кортежах (tuple), обращение идет по индексам в случае больших кортежей это может быть проблеммой.


class Person:
    def __init__(self, name, surname, year, country):
        self.name = name
        self.surname = surname
        self.year = year
        self.country = country


print('\nclass:')
Human = Person
print(Human)  # ссылка на класс Person
p1 = Human('Megan', 'Jones', '1998-07-16', 'Bolivia')
print(p1.name, p1.surname, p1.year, p1.country)
print(p1.__sizeof__())
# В экземплярах класса (объектах), обращение уже идет по именам (атрибутам).

print('\nСвойства:')
print(isinstance(p1, tuple))
print(isinstance(p1, Human))
print(isinstance(p1, Person))

print('\nnamedtuple():')
Human = namedtuple('Person', 'name surname year country')
print(Human)  # ссылка на класс Person
p1 = Human('Joseph', 'Bauer', country='Canada', year='1980-05-19')
print(p1.name, p1.surname, p1.year, p1.country)
print(p1[0], p1[1], p1[2], p1[3])
# Через namedtuple к атрибутам можно обращаться как по имени так и по индексам.

print('\nСвойства:')
print(isinstance(p1, tuple))
print(isinstance(p1, Human))
print(isinstance(p1, Person))
print(p1.count('Bauer'))
print(p1._asdict())
# p1.name = 'Victor'  # AttributeError: can't set attribute
print(p1._replace(name='Ivan', surname=666))
# Атрибуты tuple все же можно изменить и записать другой тип данных чем изначально.

print('\nТотже тип данных:')


class Person(NamedTuple):
    name: str
    surname: str
    year: datetime
    country: str


p1 = Person('Megan', 'Jones', '1998-07-16', 'Bolivia')
print(p1.name, p1.surname, p1.year, p1.country)
print(p1[0], p1[1], p1[2], p1[3])
print(p1.__sizeof__())
