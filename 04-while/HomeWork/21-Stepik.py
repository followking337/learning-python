print('\nStepik HomeWork')

print('\nСумма цифр')
n = 891101
# n = int(input())
summa = 0
while n > 0:
    last = n % 10
    summa += last
    n = n // 10
print(summa)

print('\nПроизведение цифр')
n = 102
# n = int(input())
pr = 1
while n > 0:
    last = n % 10
    pr *= last
    n = n // 10
print(pr)

print('\nЦифра 7')
n = 127
# n = int(input())
count = 0
while n > 0:
    last = n % 10
    if last == 7:
        count += 1
    n = n // 10
print(count)
