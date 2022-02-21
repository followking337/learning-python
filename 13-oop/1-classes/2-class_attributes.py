"""
АТРИБУТЫ КЛАССА

    1. Доступ к атрибутам:
        - [class].[attribute]
        - getattr(class, 'attribute', default if lacks)

    2. Создание и Изменение атрибутов:
        - [class].[attribute] = element
        - setattr(class, 'attribute', value)

    3. Удаление атрибутов:
        - del [class].[attribute]
        - delattr(class, 'attribute')

    · Любое создание, изменение или удаление в атрибутах класса имеет эффект на все экземпляры класса.
    · Переменная [class].__dict__ --> видеть все атрибуты класса.
"""


class Person:

    name = 'Ivan'
    age = 30


print('\n1. Доступ к атрибутам:')
print(Person.name)  # Ivan
print(Person.age)   # 30
print(Person.__dict__)  # видеть все атрибуты класса
print(type(Person.__dict__))  # <class 'mappingproxy'>
print(getattr(Person, 'name'))  # имя атрибута нужно вводить строкой
print(getattr(Person, 'x', 100))  # третий параметр - в случае отсуствия атрибута возвращает третий параметр, не создает

print('\n2. Создание и Изменение атрибутов:')
Person.name = 'Misha'
print(Person.name)  # Misha
Person.x = 100
print(Person.x)  # 100
setattr(Person, 'x', 200)
setattr(Person, 'y', 10)
print(Person.x)  # 200
print(Person.y)  # 10
print(Person.__dict__)

print('\n3. Удаление атрибутов:')
del Person.x
delattr(Person, 'y')
print(Person.__dict__)
