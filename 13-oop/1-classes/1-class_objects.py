"""
ОБЪЕКТ, КЛАСС, ЭКЗЕМПЛЯР КЛАССА

    1. Объект - контейнер, состоящий из:
        1.1. Attributes, Propiedades, Data.
        1.2. Methods (métodos, методы), Behavior (comportamiento, поведение).
        · Каждое значение представляет объект:
            - isinstance(5, object)
            - isinstance([1, 2, 3], object)
            - isinstance(list, object)
            - type(list) --> <class 'type'>

    2. Класс - шаблон создания объектов (шаблон при помощи которого создаются объекты),
    в классе описывается какие данные будут хранить объекты и какое у них будет поведение.
        · Каждый объект принадлежит к классу.
            узнать класс:
             - type()
             - isinstance(__obj, __class_or_tuple).
        2.1. Встроенные классы (с маленькой буквы):
            - int
            - float
            - bool
            - str
            - list
            - dict
            - tuple
            - set
            · Когда создаем объект класса list например: a = [1, 2, 3]
                - Данные [1, 2, 3] попадают в память.
                - Присваивается поведение (методы).
        2.2. Собственные классы (с большой буквы).

    3. Экземпляр класса - конкретный объект данного класса.
        · Результат вызова класса вернет создание экземпляра класса (конкретного объекта).
"""

print(isinstance(5, object))
print(isinstance([1, 2, 3], object))
print(isinstance(list, object))
print(type([1, 2, 3]))  # <class 'list'>
print(type(list))       # <class 'type'>
print('---------------------------------------')


class Car:  # создание класса

    model = 'BMW'  # атрибуты класса, данные которые присваиваются объектам при создании.
    engine = 1.6


print(Car)      # <class '__main__.Car'>
a = Car()       # вызов класса
print(a)        # <__main__.Car object at 0x7f9df11c9520> (объект класса Car).
print(type(a))  # <class '__main__.Car'>
print(isinstance(a, Car))  # True
