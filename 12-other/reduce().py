from functools import reduce  # Esta función es utilizada para reducir una lista a un solo elemento.

lista = [2, 4, 6, 8, 10]
letras = ['h', 'o', 'l', 'a']

print('\nreduce & def:')


def unir(x, y):
    return x + y


print(reduce(unir, lista))
print(reduce(unir, letras))

print('\nreduce & lambda:')

print(reduce(lambda x, y: x + y, lista))
print(reduce(lambda x, y: x + y, letras))

print('\nclass complex:')
complejo = 1 + 2j
print(complejo, type(complejo))
print(complejo.real)
print(complejo.imag)

print('\nsumar dos listas:')
numeros = [1, 2, 3, 4, 5]
numeros2 = [1, 1, 1, 1, 1]
print(numeros + numeros2)
print(list(map(lambda l1, l2: l1 + l2, numeros, numeros2)))
