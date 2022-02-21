"""
ФУНКЦИЯ КАК АТРИБУТ КЛАССА
    Статический метод класса
    Методы класса
    Статические атрибуты класса

    1. Доступ к функции класса:
        - [class].[function]
        - getattr(class, 'function')()

    2. Доступ к методу экземпляра класса:
        - [object].[method]
        - getattr(object, 'method')()
"""


class Car:

    model = 'BMW'
    engine = 1.6

    @staticmethod
    # @classmethod  # с аргументом cls
    def drive():
        print('lets go')


print('\n1. Доступ к функции класса:')
print(Car.__dict__)
Car.drive()
print(Car.drive)  # без () обращаемся к объекту <function Car.drive at 0x7fb728ad0940>
getattr(Car, 'drive')()

print('\n2. Доступ к методу экземпляра класса:')
a = Car()
print(a.__dict__)
a.drive()  # TypeError: drive() takes 0 positional arguments but 1 was given (не работает без декоратора)
getattr(a, 'drive')()
