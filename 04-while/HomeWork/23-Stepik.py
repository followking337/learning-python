print('\nStepik HomeWork')

print('\nЗадача 1 (1)')
n = 5
# n = int(input())
i = 1
a = []
while i * i <= n:
    if n % i == 0:
        a.append(i)  # count += 2
        if i != n//i:
            a.append(n//i)
    i += 1
a.sort()
print(a)
print('Yes' if len(a) == 2 else 'No')  # if count == 2  # if a == [1, n]

print('\nЗадача 1 (2)')
n = 5
# n = int(input())
i = 2
while n % i != 0 and i < n:
    i += 1
print('Yes' if i == n else 'No')

print('\nЗадача 2')
n = 10
# n = int(input())
i = 1
a = []  # s = 0
while i * i <= n:
    if n % i == 0:  # if not(n % i):
        a.append(i)  # s += i
        if i != n//i:
            a.append(n//i)  # s += n//i
    i += 1
a.sort()
print(sum(a))  # print(s)
