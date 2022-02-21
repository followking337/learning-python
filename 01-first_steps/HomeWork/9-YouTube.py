print('\nYouTube HomeWork:')

print('\nПроверка на положительность:')
x = 5
y = -47
print(x > 0, y > 0)

print('\nПроверка на четность:')
x = 5
y = -46
print(x % 2 == 0, y % 2 == 0)

print('\nПроверка на кратность 6:')
x = 5
y = -54
print(x % 6 == 0, y % 6 == 0)

print('\nЧисло НЕ кратно 9 (не делиться на 9):')
x = 5
y = -54
print(x % 9 != 0, not y % 9 == 0)

print('\nПоследняя цифра числа 2:')
x = 5
y = 52
print(x % 10 == 2, y % 10 == 2)

print('\nДеления на 10 от нигативного числа:')
y = -63
print(y % 10 == 3)
print(y % 10)

print('\nОба числа делятся на 7:')
x = 7
y = 21
print(x % 7 == 0 and y % 7 == 0)

print('\nТреугольник правильный:')
a = 5
b = 5
c = 5
print(a == b == c)
print(a == b and b == c)

print('\nПринадлежность диапазону:')
x = 15
print(5 < x <= 19)
print(x > 5 and x <= 19)

print('\nХотя бы одно делится на 4:')
x = 13
y = 19
print(x % 4 == 0 or y % 4 == 0)

print('\nТреугольник равнобедренный:')
a = 6
b = 5
c = 5
print(a == b or b == c or a == c)

print('\nЧисло двузначное:')
x = 13
y = 212
print(10 <= x <= 99, 10 <= y <= 99)
print(x // 100 == 0 and x // 10 != 0)

print('\nТреугольник прямоугольный:')
a = 8
b = 6
c = 10
print(a ** 2 + b ** 2 == c ** 2 or c ** 2 + a ** 2 == b ** 2 or c ** 2 + b ** 2 == a ** 2)
