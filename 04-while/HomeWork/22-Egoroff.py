print('\nStepik HomeWork')

print('\nАпельсины')
n, m = 3, 5
# n, m = map(int, input().split())
c = n * m
oranges = m
while m > 0:
    n, m = m, n % m
print(f'НОД: {n}')
print(f'НОК: {c // n}')
print(f'Дольки одного апельсина: {c // n // oranges}')

print('\nA. Эпическая игра')
a, b, n = 3, 5, 9
# a, b, n = map(int, input().split())
i = 1
while n > 0:
    # print('i:', i)
    y = n
    if i % 2 == 1:
        x = a
    elif i % 2 == 0:
        x = b
    # print('x:', x)
    while y > 0:
        x, y = y, x % y
    # print('НОД:', x)
    n = n - x
    # print('n:', n)
    i += 1
if i % 2 == 1:
    print(1)
elif i % 2 == 0:
    print(0)

