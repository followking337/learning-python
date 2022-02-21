print('\nЗадача 1')
s = '45654'
# s = input()
count = [0] * 10
for i in s:
    count[int(i)] += 1
print(count)
for i in range(len(count)):
    if count[i] > 0:
        print(i, count[i])

print('\nЗадача 2')
n = 8
a = [66, -66, -48, -96, -17, -80, -57, -45]
# n = int(input())
# a = list(map(int, input().split()))
count = [0] * 201
for i in a:
    count[i + 100] += 1
for i in range(len(count)):
    if count[i] > 0:
        print((str(i - 100) + ' ') * count[i], end='')
