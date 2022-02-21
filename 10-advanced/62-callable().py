"""
callable() --> True or False
    Вызываемые объект - объект к которому можно применить оператор вызова '()'.
    7 видов вызываемых объектов (callable objects):
        1. Встроенные функции.
        2. Встроенные методы объектов.
        3. Пользовательские функции и lambda функции.
        4. Классы.
        5. Экземпляры классов.
        6. Методы классов.
        7. Функции - генераторы
"""
n = 10
# print(a())  # TypeError: 'int' object is not callable
s = 'hello'
# print(b())  # TypeError: 'str' object is not callable

print('\n1. Встроенные функции:')
print(len('hello'))
print(int('10'))
print(callable(len))
print(callable(10))

print('\n2. Встроенные методы объектов:')
a = [1, 2, 3]
a.sort()
print(a)
print(callable(a.sort))  # нельзя проверить метод на вызываемость без объекта.
print(callable('hello'.lower))
print(callable(str.upper))

print('\n3. Пользовательские функции и lambda функции:')


def f():
    print('hello world')


d = lambda: 'hi'  # lambda возвращает как return.
f()
print(d())
print(callable(f))
print(callable(d))

print('\n4. Классы:')


class Cat:
    pass


bob = Cat()
print(bob)  # является экземпляром класса.
print(callable(Cat))
print(callable(bob))

print('\n5. Экземпляры классов:')


class Cat:
    def __call__(self, *args, **kwargs):
        print('мяу')

    def say_hello(self):
        print('hello')


bob = Cat()
print(bob)
bob()
print(callable(bob))

print('\n6. Методы классов')
bob.say_hello()
print(callable(bob.say_hello))

print('\n7. Функции - генераторы')


def f():
    n = 0
    while True:
        yield n
        n += 1


print(callable(f))
