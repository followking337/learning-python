print('\nclass bool:')
print('\nСравнение чисел:')
print(5 > 1)
print(5 > 9)
print(5 == 7 - 2)
print(6 != 6)
print(6 <= 4)

print('\nПроверка на положительные:')
x = 6
print(x > 0)

print('\nПроверка на четные числа:')
x = -4
print(x % 2 == 0)

print('\nПроверка на кратный четырем:')
x = 13
print(x % 4 == 0)

print('\nПроверка на НЕ кратный четырем:')
x = 13
print(x % 4 != 0)

print('\nkeyword: not:')
print(not x % 4 == 0)  # не кратно четырем

print('\nkeyword: and:')
a = -5
b = 7
print(a > 0 and b > 0)
a = 8
print(a % 2 == 0 and a % 3 == 0)
a = 12
print(a % 2 == 0 and a % 3 == 0)

print('\nkeyword: or:')
a = -5
b = 7
print(a > 0 or b > 0)
a = 8
print(a % 2 == 0 or a % 3 == 0)
a = 7
print(a % 2 == 0 or a % 3 == 0)

print('\nПроверка в интервале:')
a = 21
print(a >= 12 and a < 31)
print(12 <= a < 31)

print('\nПроверка на двузначность:')
a = 51
print(10 <= a < 99)

print('\nПроверка число заканчивается на 7:')
a = 46
print(a % 10 == 7)

print('\nKeywords Order (not, and, or):')
a = 517
print(a > 5 or a % 2 == 0 and a % 10 == 7)
print(a > 5 or (a % 2 == 0 and a % 10 == 7))
print((a > 5 or a % 2 == 0) and a % 10 == 7)

# в bool можно преобразовать любые типы данных int, float, str в True и 0, '' (пустая строка) в False
print('\nПреображение в bool:')
print(bool(124))
print(bool(0))
print(bool(0.000001))
print(bool('srgsr'))
print(bool(''))
print(bool(' '))
print(bool('r'))

print('\nTrue -> 1; False -> 0:')
n = 5
print(int(n / 2) + (n % 2 > 0))
print((n // 2) + (n % 2 > 0))
print(int(n / 2))
print(int(n % 2 > 0))
print(int(False))
print(int(True))

print('\nЗаписывать результат сравнения в переменную:')
x = 5 > 2
y = 6 < 8
print(x, y)
print(x and y)

print('\nbool():')
# любой объект можно преобразовать в bool, правило: если переданное значение пустое - False; если не пустое - True.
print('\nint:')
print(bool(45))
print(bool(-75))
print(bool(0.005))
print(bool(0))

print('\nstr:')
print(bool('hello'))
print(bool('2'))
print(bool(' '))
print(bool(''))

print('\nlist:')
print(bool([7, 8]))
print(bool([0]))
print(bool([1]))
print(bool([]))
