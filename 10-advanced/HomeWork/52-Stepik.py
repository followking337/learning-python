print('\nЗадача 1.1')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kvadrat = list(map(lambda x: x ** 2, numbers))
cub = list(map(lambda x: x ** 3, numbers))
print(kvadrat, cub, sep='\n')

print('\nЗадача 1.2')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
func = lambda y: lambda x: x ** y
print(list(map(func(2), numbers)))
print(list(map(func(3), numbers)))

print('\nЗадача 1.3')


def func(y):
    return lambda x: x ** y


print(list(map(func(2), numbers)))
print(list(map(func(3), numbers)))

print('\nЗадача 1.4')


def func(y):

    def inner(x):
        return x ** y

    return inner


print(list(map(func(2), numbers)))
print(list(map(func(3), numbers)))
f2 = func(2)
print(f2(6))
f3 = func(3)
print(f3(2))
