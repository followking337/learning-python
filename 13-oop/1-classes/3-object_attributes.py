"""
АТРИБУТЫ ЭКЗЕМПЛЯРОВ КЛАССА

    1. Доступ к атрибутам:
        - [object].[attribute]
        - getattr(object, 'attribute', default if lacks)

    2. Создание и Изменение атрибутов:
        - [object].[attribute] = element
        - setattr(object, 'attribute', value)

    3. Удаление атрибутов:
        - del [object].[attribute]
        - delattr(object, 'attribute')

    · Любое создание, изменение или удаление в атрибутах одного объекта НЕ имеет эффект на остальные экземпляры класса.
    · Переменная [object].__dict__ --> видеть все атрибуты объекта.
"""


class Car:

    model = 'BMW'
    engine = 1.6


print('\n1. Доступ к атрибутам:')
a1 = Car()
a2 = Car()
print(a1.model, a1.engine)
print(a2.model, a2.engine)
print(getattr(a1, 'model'))
print(getattr(a2, 'engine'))
print(a1.__dict__, a2.__dict__)

print('\n2. Создание и Изменение атрибутов:')
a1.seat = 4
a2.size = 80
setattr(a2, 'doors', 5)
print(a1.__dict__, a2.__dict__)
a1.model = 'Lada'
setattr(a2, 'doors', 2)
print(a1.__dict__, a2.__dict__)

print('\n3. Удаление атрибутов:')
del a1.model
delattr(a2, 'doors')
print(a1.__dict__, a2.__dict__)
print(a1.model)
