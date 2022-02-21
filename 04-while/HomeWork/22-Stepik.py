print('\nStepik HomeWork')

print('\nНОД: методом вычитания')
a, b = 77, 22
# a, b = map(int, input().split())
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(a)

print('\nНОД: методом остаток от деления')
a, b = 77, 22
# a, b = map(int, input().split())
while b > 0:
    a, b = b, a % b
print(a)

print('\nНОК: наименьшее общее кратное')
a, b = 6, 15
# a, b = map(int, input().split())
c = a * b
while b > 0:
    a, b = b, a % b
# print(a)
print(c // a)
