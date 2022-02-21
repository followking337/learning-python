from math import ceil

print('\nStepik HomeWork')

print('\nЗадача 1')
N = 203
# N = int(input())
print(ceil(N / 10))

print('\nЗадача 2')
N = 9
# N = int(input())
print(ceil(N / 4))

print('\nЗадача №2946. Парты')
a = 20
b = 21
c = 22
# a = int(input())
# b = int(input())
# c = int(input())
tables = ceil(a / 2) + ceil(b / 2) + ceil(c / 2)
print(tables)

print('\nЗадача 4')
L = 5
W = 6
H = 7
# L, W, H = map(int, input().split())
m2 = 2 * (W * H) + 2 * (H * L)
print(ceil(m2 / 16))
