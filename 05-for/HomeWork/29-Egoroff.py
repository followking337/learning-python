print('\nA. Переключение гравитации')
n = 4
a = [3, 2, 1, 2]
# n = int(input())
# a = list(map(int, input().split()))
count = [0] * 101
for i in a:
    count[i] += 1
# print(count)
for i in range(len(count)):
    if count[i] > 0:
        # print(i, count[i])
        print((str(i) + ' ') * count[i], end='')  # print(*sorted(a))

print('\n\nA. Щедрый Кефа')
n, k = 36, 13
s = 'bzbzcffczzcbcbzzfzbbfzfzzbfbbcbfccbf'
# n, k = map(int, input().split())
# s = input()

count = [0] * 26
for i in s.lower():
    count[ord(i) - 97] += 1

while 0 in count:
    count.remove(0)
print(count)

while any(count) and k > 0:
    i = 0
    for i in range(len(count)):
        if count[i] > 0:
            count[i] -= 1
        print(k, count)
    k -= 1

print(count)
print('NO' if any(count) else 'YES')

print('\nA. Веселая шутка')
a = ['SANTACLAUS', 'DEDMOROZ', 'SANTAMOROZDEDCLAUS']
# a = [input() for i in range(3)]

count = [0] * 26
for i in a[0] + a[1]:
    count[ord(i) - 65] += 1

count2 = [0] * 26
for i in a[2]:
    count2[ord(i) - 65] += 1

print('YES' if count == count2 else 'NO')
