print('\nStepik HomeWork')

print('\nГипотеза Коллатца (1)')
n = 10
# n = int(input())
i = 0
while n != 1:
    if n % 2 == 0:
        n //= 2
    elif n % 2 == 1:
        n = 3 * n + 1
    i += 1
print(i)

print('\nГипотеза Коллатца (2)')
n = 10
# n = int(input())
i = 0
while True:
    i += 1
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    if n == 1:
        break
print(i)

print('\nГипотеза Коллатца (3)')
n = 10
# n = int(input())
i = 0
while n > 1:
    n = 3 * n + 1 if n & 1 else n >> 1
    i += 1
print(i)
