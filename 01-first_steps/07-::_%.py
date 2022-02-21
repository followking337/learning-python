print('\n// and %:')

print('\nTenemos 41 huevos y cestas de 12 huevos:')
print('Cuantas cestas necesitamos?')
print(41 // 12)

print('\nCuantos huevos quedan sin cesta?')
print(41 % 12)

print('\n3 = 41 // 12')
print('5 = 41 % 12')
print('41 = 12 * 3 + 5')

print('\nОстаток по числам:')
print('8, 15, 22, 29,...')
print(8 % 7)
print('\n10, 17, 24, 31,...')
print(10 % 7)

print('\nОстаток по числам на 1, 10, 100, 1000 (оставляем справа):')
print(654987.5 % 1)
print(654987 % 10)
print(654987 % 100)
print(654987 % 1000)

print('\nДеление на цело на 1, 10, 100, 1000 (убираем справа):')
print(654987.5 // 1)
print(654987 // 10)
print(654987 // 100)
print(654987 // 1000)

print('\nВытащить цифру:')
print('4(7)865:')
print(47865 // 1000 % 10)
print('47(8)65:')
print(47865 // 100 % 10)

print('\nРазложение числа:')
x = 47865
a = x // 10000
b = x // 1000 % 10
c = x // 100 % 10
d = x // 10 % 10
e = x % 10
print(a, b, c, d, e)
