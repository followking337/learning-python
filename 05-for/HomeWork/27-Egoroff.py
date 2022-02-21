print('\nЗадача №3748. Удалить каждый третий символ')
n = 'Python'
# n = input()
t = ''
for i in range(len(n)):
    if i % 3 != 0:
        t += n[i]
print(t)

print('\nA. Полицейские-рекруты')
n = 3
a = [-1, -1, 1]
# n = int(input())
# a = list(map(int, input().split()))
cases = 0
policemen = 0
for i in a:
    if i == -1 and policemen == 0:
        cases += 1
    elif i == -1 and policemen > 0:
        policemen -= 1
    elif i > 0:
        policemen += i
print(cases)

print('\nA. I_love_%username%')
n = 5
a = [100, 50, 200, 150, 200]
# n = int(input())
# a = list(map(int, input().split()))
min_record = a[0]
max_record = a[0]
count = 0
for i in a:
    if i > max_record:
        max_record = i
        count += 1
    elif i < min_record:
        min_record = i
        count += 1
print(count)

print('\nA. Следующий раунд')
n, k = 8, 5
a = [10, 9, 8, 7, 7, 7, 5, 5]
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
count = 0
for i in a:
    if i >= a[k - 1] > 0 or i > a[k - 1] == 0:
        count += 1
print(count)

print('\nA. Праздник равенства')
n = 5
a = [0, 1, 2, 3, 4]
# n = int(input())
# a = list(map(int, input().split()))
expenses = 0
for i in a:
    if i < max(a):
        expenses += max(a) - i
print(expenses)

print('\nA. Тренировки Егора')
n = 7
a = [3, 3, 2, 7, 9, 6, 8]
# n = int(input())
# a = list(map(int, input().split()))
chest = 0
biceps = 0
back = 0
for i in range(n):
    if i % 3 == 0:
        chest += a[i]
    elif i % 3 == 1:
        biceps += a[i]
    elif i % 3 == 2:
        back += a[i]
b = [chest, biceps, back]
if chest == max(b):
    print('chest')
elif biceps == max(b):
    print('biceps')
elif back == max(b):
    print('back')

print('\nA. Упражнение на строки (1)')
s = 'Codeforces'
# s = input()
t = ''
for i in s.lower():
    if i in 'aeoiuy':
        continue
    else:
        t += '.' + i
print(t)

print('\nA. Упражнение на строки (2)')
s = 'Codeforces'.lower()
# s = input().lower()
for i in 'aeoiuy':
    s = s.replace(i, '')
s = '.' + '.'.join(s)
print(s)

print('\nA. Не смешите мои подковы')
a = [1, 7, 3, 3]
# a = list(map(int, input().split()))
count = 0
color = 0
for i in sorted(a):
    if i != color:
        color = i
        continue
    elif i == color:
        count += 1
print(count)

print('\nB. Напитки')
n = 3
a = [50, 50, 100]
# n = int(input())
# a = list(map(int, input().split()))
total = 0
for i in a:
    total += i
print(total / n)  # print(sum(a) / n)

print('\nA. Выбор команд')
n, k = 5, 2
a = [0, 4, 5, 1, 0]
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
count = 0
team = 0
for i in a:
    if 5 - i >= k:
        count += 1
    if count == 3:
        team += 1
        count -= count
print(team)

print('\nA. Быстрый математик')
s = '1010100'
t = '0100101'
# s = input()
# t = input()
v = ''
for i in range(len(s)):
    if s[i] == t[i]:
        v += '0'
    else:
        v += '1'
print(v)

print('\nA. Ваня и забор')
n, k = 3, 7
a = [4, 5, 14]
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
width = 0
for i in a:
    if i > k:
        width += 2
    else:
        width += 1
print(width)

print('\nA. Башни')
n = 25
a = [47, 30, 94, 41, 45, 20, 96, 51, 110, 129, 24, 116, 9, 47, 32, 82, 105, 114, 116, 75, 154, 151, 70, 42, 162]
# n = int(input())
# a = list(map(int, input().split()))
print(sorted(a))
length = 0
height = 1
towers = 0
for i in sorted(a):
    if i != length:
        length = i
        towers += 1
    elif a.count(i) > height:
        height = a.count(i)
print(height, towers)

print('\nA. Антон и Даник')
n = 6
s = 'ADAAAA'
# n = int(input())
# s = input()
Anton = 0
Danik = 0
for i in s:
    if i == 'A':
        Anton += 1
    elif i == 'D':
        Danik += 1
if Anton > Danik:
    print('Anton')
elif Anton < Danik:
    print('Danik')
else:
    print('Friendship')

print('\nA. Свободная касса')
# n = int(input())
# hour = -1
# minutes = -1
# cash = 1
# count = 1
# for i in range(n):
#     a = list(map(int, input().split()))
#     if a[0] == hour and a[1] == minutes:
#         count += 1
#         if count > cash:
#             cash = count
#     elif a[0] != hour or a[1] != minutes:
#         count = 1
#     hour, minutes = a[0], a[1]
# print(cash)

print('\nA. Слово')
s = 'maTRIx'
# s = input()
count = 0
for i in s:
    if 'A' <= i <= 'Z':
        count += 1
    elif 'a' <= i <= 'z':
        count -= 1
print(count)
if count > 0:
    print(s.upper())
else:
    print(s.lower())

print('\nA. IQ тест')
n = 3
a = [1, 2, 2]
# n = int(input())
# a = list(map(int, input().split()))
b = []
for i in a:
    if i % 2 == 0:
        b.append(0)
    elif i % 2 == 1:
        b.append(1)
print(b)
if b.count(0) == 1:
    print(b.index(0) + 1)
else:
    print(b.index(1) + 1)

print('\nB. Максимальный непрерывный отдых')
n = 10
a = [1, 1, 1, 0, 0, 1, 0, 1, 1, 1]
# n = int(input())
# a = list(map(int, input().split()))
count = 1
rest = 0
for i in range(len(a)):
    if i == len(a) - 1:
        if a[i] == 1 and a[0] == 1:
            j = 0
            while a[j] == 1:
                count += 1
                if rest < count:
                    rest = count
                j += 1
        else:
            break
    elif a[i] == 1 and a[i + 1] == 1:
        count += 1
        if rest < count:
            rest = count
    elif a[i] != a[i + 1]:
        count = 1
        if rest < count:
            rest = count
print(rest)

print('\nA. Командная олимпиада')
n = 7
a = [1, 3, 1, 3, 2, 1, 2]
# n = int(input())
# a = list(map(int, input().split()))
teams = min(a.count(1), a.count(2), a.count(3))
print(teams)
previous = [0, 0, 0]
for i in range(teams):
    team = []
    j = 1
    while j < 4:
        team.append(a.index(j, previous[j - 1]) + 1)
        j += 1
    previous = team
    print(*team)

print('\nA. Мокрая Акула и чётность')
n = 5
a = [999999999, 999999999, 999999999, 999999999, 999999999]
# n = int(input())
# a = list(map(int, input().split()))
summa = sum(a)
for i in range(n):
    if summa % 2 == 0:
        break
    else:
        summa -= min(a)
        a.remove(min(a))
        print(a)
print(summa)

print('\nA. Панграмма')
n = 35
s = 'TheQuickBrownFoxJumpsOverTheLazyDog'
# n = int(input())
# s = input()
abc = 'abcdefghijklmnopqrstuvwxyz'
all_letters = True
for i in abc:
    if i not in s.lower():
        all_letters = False
if all_letters:
    print('YES')
else:
    print('NO')

print('\nA. Клавиатура')
s = 'R'
t = 's;;upimrrfod;pbr'
# s = input()
# t = input()
a = ['qwertyuiop', 'asdfghjkl;', 'zxcvbnm,./']
v = ''
for i in t:
    for j in a:
        if i in j:
            if s == 'R':
                if j.index(i) == 0:
                    v += j[j.index(i)]
                else:
                    v += j[j.index(i) - 1]
            elif s == 'L':
                if j.index(i) == -1:
                    v += j[j.index(i)]
                else:
                    v += j[j.index(i) + 1]
print(v)

print('\nA. Кодовый замок')
n = 5
k = '82195'
q = '64723'
# n = int(input())
# k = input()
# q = input()
count = 0
for i in range(n):
    a = abs(int(k[i]) - int(q[i]))
    b = min(int(k[i]), int(q[i])) + 10 - max(int(k[i]), int(q[i]))
    count += min(a, b)
print(count)

print('\nA. Подарки')
n = 4
a = [2, 3, 4, 1]
# n = int(input())
# a = list(map(int, input().split()))
for i in range(1, n+1):
    print(a.index(i)+1, end=' ')

print('\n\nB. Ваня и фонари')
nl = [2, 5]
a = [2, 5]
# nl = list(map(int, input().split()))
# a = list(map(int, input().split()))
d = []
previous = 0
distance = 0
a = a + nl[1:]
for i in sorted(a):
    d.append(i - previous)
    previous = i
print(d)
if len(d) == 2:
    print(max(d))
else:
    if d[0] > d[-1] and d[0] > (max(d[1:-1]) / 2):
        print(d[0])
    elif d[-1] > d[0] and d[-1] > (max(d[1:-1]) / 2):
        print(d[-1])
    elif (max(d[1:-1]) / 2) < d[-1] == d[0]:
        print(d[-1])
    else:
        print(max(d[1:-1]) / 2)

print('\nA. Близнецы')
n = 7
a = [1, 10, 1, 2, 1, 1, 1]
# n = int(input())
# a = list(map(int, input().split()))
b = []
for i in range(n):
    b.append(max(a))
    a.remove(max(a))
    if sum(b) > sum(a):
        break
print(b, a)
print(len(b))

print('\nA. Автобус в Удайлэнд')
# n = int(input())
# t = ''
# for i in range(n):
#     s = input()
#     if 'OO' in s and '++' not in t:
#         s = s.replace('OO', '++', 1)
#     t += s + '\n'
# if '++' in t:
#     print('YES')
#     print(t)
# else:
#     print('NO')

