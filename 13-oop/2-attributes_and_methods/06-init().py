"""
МАГИЧЕСКИЙ МЕТОД __init__
    <КОНСТРУКТОР>
        - Срабатывает после создания объекта.
        - Служит для инициализации объекта, для заполнения объекта атрибутами при его создании.

    def __init__(self, argument1, argument2, ...)
        self.attribute1 = argument1
        self.attribute2 = argument2
        ...

    Инициализация объекта:
        1. Вначале создается объект магическим методом __new__
        2. Создается пространство имен объекта, доступ к которому осуществляется через магическую переменную .__dict__
        3. Запускается магический метод __init__
"""


class Cat:
    breed = 'pers'

    def set_name(self, name, age=0):
        self.name = name
        self.age = age

    def __init__(self):
        print('hello new object is', self)


tom = Cat()
print(tom)
jerry = Cat()
print(jerry)


class Cat:

    def __init__(self, name, breed='pers', age=1, color='white'):
        print('new object has:', name, breed, age, color)
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color


walt = Cat('Walt')
kelly = Cat('Kelly', 'siam', age=40, color='black')
print(walt.__dict__)
print(kelly.__dict__)
