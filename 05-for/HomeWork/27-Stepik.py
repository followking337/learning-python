print('\nЗадача 1')
# n = int(input())
# a = []
# for i in range(n):
#     s = input()
#     a.append(s)
# print(a)

# print([input() for i in range(int(input()))])

print('\nЗадача 2')
s = 'a'
frase = 'Mary had a little lamb.'
# s = input()
# frase = input()
for i in frase.split():  # for i in range(len(frase.split())):
    if s in i.lower():  # if s in frase[i]:
        print(i)  # print(frase[i])

# s = input()
# print(*[i for i in input().split() if s in i.lower()], sep='\n')

print('\nЗадача 3')
a = [8, 11, -9, 0, 5, -20]
# a = list(map(int, input().split()))
b = []
for i in a:
    if i > 0:
        b.append(i)
print('Empty' if len(b) == 0 else min(b))

b = list(filter(lambda x: x > 0, a))
print('Empty' if len(b) == 0 else min(b))

print('\nЗадача 4 (1)')
s = 'Тот'
# s = input()
count = 0
for i in s.lower():
    if s.count(i) > count:
        count = s.count(i)
print(count)

print('\nЗадача 4 (2)')
s = 'Тот'
# s = input()
a = []
for i in s.lower():
    a.append(s.count(i))
print(max(a))

print('\nЗадача 4 (3)')
s = 'Тот'
# s = input()
d = {}
for i in s.lower():
    d[i] = d.get(i, 0) + 1
print(d)
# print(max(d, key=lambda x: x))

print('\nДелимость на 11 (1)')
s = '121'
# s = input()
par = 0
impar = 0
for i in range(len(s)):
    if i % 2 == 1:
        par += int(s[i])
    elif i % 2 == 0:
        impar += int(s[i])
if (par - impar) % 11 == 0:
    print('YES')
else:
    print('NO')

print('\nДелимость на 11 (2)')
s = '1211'
# s = input()
summa = 0
for index, value in enumerate(s):
    if index % 2 == 1:
        summa += int(value)
    elif index % 2 == 0:
        summa -= int(value)
if summa % 11 == 0:
    print('YES')
else:
    print('NO')

print('\nЗадача 6 (1)')
s = 'Europe cup 2021'
# s = input()
count = 0
total = 0
for i in s:
    if i.isdigit():
        count += 1
        total += int(i)
print(count, total)

print('\nЗадача 6 (2)')
s = 'Europe cup 2021'
# s = input()
a = []
for i in s:
    if i.isdigit():
        a.append(int(i))
print(len(a), sum(a))

# a = [int(i) for i in input() if i.isdigit()]
# print(len(a), sum(a))

print('\nПравильная скобочная последовательность (1) Error: out of time')
s = '{[]}()'
# s = input()
opened = '0([{'
closed = '0)]}'
a = []
for i in s:
    if i in opened:
        a.append(opened.find(i))
    elif i in closed:
        a.append(closed.find(i) * -1)
print(a)
i = 0
while len(a) - 1 > i:
    if a[i + 1] < 0 and a[i] > 0 and a[i + 1] + a[i] == 0:
        a.remove(a[i + 1])
        a.remove(a[i])
        print(a)
        i = 0
    else:
        i += 1
print('YES' if len(a) == 0 else 'NO')

print('\nПравильная скобочная последовательность (2) Stack (LIFO: Last In - First Out)')
s = '{[]}()'
# s = input()
stack = []
is_good = True
for i in s:
    if i in '([{':
        stack.append(i)
    elif i in ')]}':
        if not stack:
            is_good = False
            break
        opened_bracket = stack.pop()
        if opened_bracket == '(' and i == ')':
            continue
        if opened_bracket == '[' and i == ']':
            continue
        if opened_bracket == '{' and i == '}':
            continue
        is_good = False
        break
print('YES' if is_good and len(stack) == 0 else 'NO')

print('\nПравильная скобочная последовательность (3)')
s = '{[]}()'
# s = input()
for i in s:
    start = len(s)
    s = s.replace('()', '').replace('[]', '').replace('{}', '')
    if start == len(s):
        print('NO')
        break
    if len(s) == 0:
        print('YES')
        break

print('\nПравильная скобочная последовательность (4)')
s = '{[]}()'
# s = input()
t = ['[]', '()', '{}']
stack = []
for i in s:
    stack.append(i)
    # print(stack)
    while len(stack) > 1 and stack[-2] + stack[-1] in t:
        stack.pop()
        stack.pop()
print("NO" if stack else "YES")

