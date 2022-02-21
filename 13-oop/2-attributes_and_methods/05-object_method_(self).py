"""
МЕТОДЫ ЭКЗЕМПЛЯРА и АРГУМЕНТ SELF

    · Методы и Функции:
        - Отличия:
            1. Метод это функция объявленная внутри класса.
            2. Метод связан с объектом.
            3. При вызове метода, объект, с кем связан метод, подставляется в качестве аргумента в функцию.

    · Аргумент Self - тот самый объект при котором был вызван метод.
        - def method(self):
              {code}
"""

print('\n\tБез аргумента:')


class Cat:

    @staticmethod
    def hello():
        print('hello world from kitty')


Cat.hello()
bob = Cat()
bob.hello()     # TypeError: hello() takes 0 positional arguments but 1 was given (if @staticmethod lacks)
print(Cat.hello)  # <function Cat.hello at 0x7f8920ad5940>
print(bob.hello)  # <bound method Cat.hello of <__main__.Cat object at 0x7f8920adefa0>>

print('\n\tС аргументом:')


class Cat:

    def hello(*args):
        print('hello world from kitty', args)


Cat.hello()
jim = Cat()
jim.hello()  # hello world from kitty (<__main__.Cat object at 0x7fe3b42d8c10>,)
print(jim)   # <__main__.Cat object at 0x7fe3b42d8c10>

print('\n\tС атрибутом и с аргументом:')


class Cat:

    breed = 'pers'

    def show_breed(instance):
        print(f'my breed is {instance.breed}')


walt = Cat()
walt.show_breed()
walt.breed = 'siam'
walt.show_breed()

print('\n\tС аргументом:')


class Cat:

    def show_name(instance):
        if hasattr(instance, 'name'):
            print(f'my name is {instance.name}')
        else:
            print('nothing')


mary = Cat()
mary.show_name()
mary.name = 'MARY'
mary.show_name()

print('\n\tАргументы 1 + 1:')


class Cat:

    def show_name(instance):
        if hasattr(instance, 'name'):
            print(f'my name is {instance.name}')
        else:
            print('nothing')

    def set_name(koshka, name):
        koshka.name = name


tom = Cat()
tom.show_name()
tom.set_name('Tom')
print(tom.name)
tom.show_name()

print('\n\tАргументы 1 + 2:')


class Cat:

    def show_name(instance):
        if hasattr(instance, 'name'):
            print(f'my name is {instance.name}')
        else:
            print('nothing')

    def set_name(koshka, name, age=0):
        koshka.name = name
        koshka.age = age


jerry = Cat()
jerry.set_name('Jerry', 15)
print(jerry.name, jerry.age)
