"""
Variables have 3 components:
    name -> starts with a small letter, without spaces and symbols.
    value
    type -> dynamic typing (the type of value is assigned to the variable automatically).

    name = value
    name: type = value
    name: type1 | type2 | type3 = value

    Оператор присваивания обозначается знаком равно "=". При этом он сперва вычисляет значение, стоящее в правой части,
    и сохраняет в переменную, находящуюся в левой.
"""

print('\na = 4:')
a = 4
print(a)
print(a * 5)
print(a + a)

print('\na = 54, b = 10:')
a = 54
print(a + 5)
b = 10
print(a + b)

print('\nПеременная = Выражение:')
b = 10
b = 2 * b
print(b)
b = 2 * b
print(b)
a = 5
c = b + 2 * a
print(c)

print('\nМассовое присвоение:')
a = b = c = r = 1
print(a, b, c, r)

print('\nМножественное присвоение:')
a, b = 2, 7
print(a, b)

print('\nМеняем местами переменные a и b (1):')
a, b = 2, 7
temp = a
a = b
b = temp
print(a, b)

print('\nМеняем местами переменные a и b (2):')
a, b = 2, 7
b = b - a
a = a + b
b = a - b
# b = abs(b - a)
print(a, b)
