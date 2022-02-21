"""
DOUBLE UNDERSCORE (dunder) METHODS
    Магические Методы
    __method__ --> методы внутри класса
        · Вызываются (срабатывают):
            1. автоматически в определенный момент времени.
            2. вручную через [instance].__method__()

        __repr__--> как объект будет отображаться для разработчиков, срабатывает когда вызывается:
            - str(instance)
            - repr(instance)
            - print(instance)
            - variable in console
            - на прямую в console
            - [instance].__repr__()

        __str__ --> как объект будет отображаться для пользователей, срабатывает когда вызывается:
            - str(instance)
            - print(instance)
            - variable in console
            - [instance].__str__()

            · __str__ перезатирает __repr__ строки (кроме на прямую в console).

        · Методы отвечают за текстовое отображение объекта в системе.
        · Обязательно должны возвращать текс: return str.
"""


class Lion:

    def __init__(self, name):
        self.name = name


print('\nБез метода:')
a = Lion('Bob')
print(a)
print(str(a))


class Lion:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'The object {Lion.__name__} name {self.name} from __repr__'


print('\n__repr__:')
a = Lion('Simba')
print(a)
print(str(a))
print(a.__repr__())


class Lion:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'The object {Lion.__name__} name {self.name} from __str__'

    def __repr__(self):
        return f'The object {Lion.__name__} name {self.name} from __repr__'


print('\n__str__:')
a = Lion('Simba')
print(a)
print(str(a))
print(a.__str__())
print(a.__repr__())
