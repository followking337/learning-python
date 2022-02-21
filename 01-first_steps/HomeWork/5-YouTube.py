print('\nYouTube HomeWork')

print('\nБисер')
n = 3
# n = int(input())
print(n + 1)
# print(int(input()) + 1)

print('\nЖуравлики (1)')
s = 24
# s = int(input())
x = s // 6
print(x, x * 4, x)

print('\nЗадача №2936. Гипотенуза')
a = 5
b = 4
# a = int(input())
# b = int(input())
print((a ** 2 + b ** 2) ** (1 / 2))

print('\nМагазин канцелярских товаров')
x, y, z = 1, 1, 1
# x, y, z = map(int, input().split())
print(3 * x + 5 * y + 12 * z)

print('\nЗадача №2949. Обмен значений')
a = 8
b = 5
# a = int(input())
# b = int(input())
temp = a
a = b
b = temp
print(a, b)

print('\nЭния')
n, a, b = 14, 23, 5
# n, a, b = map(int, input().split())
print(n * a * b * 2)

print('\nЗадача №2952. Разность времен')
h1 = 1
min1 = 2
sec1 = 30
h2 = 1
min2 = 3
sec2 = 20
# h1 = int(input())
# min1 = int(input())
# sec1 = int(input())
# h2 = int(input())
# min2 = int(input())
# sec2 = int(input())
print((h2 - h1) * 3600 + (min2 - min1) * 60 + (sec2 - sec1))

print('\nДва бандита (1)')
Xg, Xl = 4, 7
# Xg, Xl = map(int, input().split())
Yg = Xl - 1
Yl = Xg - 1
print(Yg, Yl)

print('\nДва бандита (2)')
Xg, Xl = 4, 7
# Xg, Xl = map(int, input().split())
s = Xg + Xl - 1
print(s - Xg, s - Xl)

print('\nЗадача №3466. Шнурки')
a = 2
b = 1
l = 3
N = 4
# a = int(input())
# b = int(input())
# l = int(input())
# N = int(input())
print(a + (2 * l) + ((2 * a) + (2 * b)) * (N - 1))

print('\nExpression (1)')
a = 2
b = 10
c = 3
# a = int(input())
# b = int(input())
# c = int(input())
num = 0
if (a == 1 and b == 1 and c == 1) or (a == 1 and c == 1):
    num = a + b + c
elif a == 1:
    num = (a + b) * c
elif b == 1:
    if a < c:
        num = (a + b) * c
    else:
        num = a * (b + c)
elif c == 1:
    num = a * (b + c)
else:
    num = a * b * c
print(num)
