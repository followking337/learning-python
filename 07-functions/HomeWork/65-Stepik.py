print('\nЗадача 1.1')


def multiply(x):

    def inner(y):
        return x * y

    return inner


f_2 = multiply(2)
print("Умножение 2 на 5 =", f_2(5))
print("Умножение 2 на 15 =", f_2(15))

f_3 = multiply(3)
print("Умножение 3 на 5 =", f_3(5))
print("Умножение 3 на 15 =", f_3(15))

print('\nЗадача 1.2')


def multiply(n):
    return lambda x: x * n


f_2 = multiply(2)
print("Умножение 2 на 5 =", f_2(5))
print("Умножение 2 на 15 =", f_2(15))

f_3 = multiply(3)
print("Умножение 3 на 5 =", f_3(5))
print("Умножение 3 на 15 =", f_3(15))

print('\nЗадача 1.3')


multiply = lambda x: lambda y: x * y


f_2 = multiply(2)
print("Умножение 2 на 5 =", f_2(5))
print("Умножение 2 на 15 =", f_2(15))

f_3 = multiply(3)
print("Умножение 3 на 5 =", f_3(5))
print("Умножение 3 на 15 =", f_3(15))
