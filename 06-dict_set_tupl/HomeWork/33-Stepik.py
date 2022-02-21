print('\nЗадача 1')
# a = set(map(int, input().split()))
# b = set(map(int, input().split()))
# print(*sorted(a & b))  # print(*sorted(a.intersection(b)))

print('\nЗадача 2')
# a = set(map(int, input().split()))
# b = set(map(int, input().split()))
# print(*sorted(a-b))

print('\nЗадача 3')
s = 'qwerty123'
# s = input()
a = sorted([int(i) for i in set(s) if i.isdigit() and s.count(i) > 1])
print(*a if a else ['NO'])

print('\nЗадача 4.1')
s = 'hello_world!'
# s = input()
a = sorted([s.index(i) for i in set(s)])
t = ''
for i in a:
    t += s[i]
print(t)

print('\nЗадача 4.2')
s = 'hello_world!'
# s = input()
t = ''
for i in s:
    if i not in t:
        t += i
print(t)

print('\nДили Вили Били')
# d = {'Дили': set(),
#      'Вили': set(),
#      'Били': set()
#      }
# text = input()
# while text != 'конец':
#     name, comment = text.split(': ')
#     d[name].add(comment)
#     text = input()
# e = {i: len(d[i]) for i in d}
# for k, v in sorted(e.items(), reverse=True, key=lambda par: par[1]):
#     print(f'Количество уникальных комментаторов у {k} - {v}')

print('\nA. Девушка или Юноша')
s = 'sevenkplus'
# s = input()
if len(set(s)) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')

print('\nA. Не смешите мои подковы')
a = [1, 7, 3, 3]
# a = list(map(int, input().split()))
print(4 - len(set(a)))

print('\nA. Красивый год')
y = 1987
# y = int(input())
y += 1
while len(set(str(y))) != 4:
    y += 1
print(y)

print('\nA. Антон и буквы (1)')
s = '{a, b, c, b, c}'
# s = input()
s = s.lstrip('{').rstrip('}')
if len(s) == 0:
    print(0)
else:
    s = s.split(', ')
    print(len(set(s)))

print('\nA. Антон и буквы (2)')
s = '{a, b, c, b, c}'
# s = input()
s = s[1:-1].replace(', ', '')
print(len(set(s)))

print('\nA. Антон и буквы (3)')
s = '{a, b, c, b, c}'
# s = input()
print(len(set(s) - set('{} ,')))

print('\nA. Антон и буквы (4)')
s = '{a, b, c, b, c}'
# s = input()
a = set(s)
b = set()
for i in a:
    if i.isalpha():
        b.add(i)  # count += 1
print(len(b))  # print(count)

print('\nA. Панграмма')
n = 12
s = 'toosmallword'
# n = int(input())
# s = input()
a = set(s.lower())
for i in a:
    if not i.isalpha():  # no es necesario, ya que segun las condiciones texto solo contendrá letras
        a.remove(i)
print('YES' if len(a) == 26 else 'NO')

print('\nA. Почти счастливое число')
n = str(444444444444444444)
# n = input()
count = n.count('4') + n.count('7')
if count == 4 or count == 7:
    print('YES')
else:
    print('NO')

print('\nA. Счастливое деление')
n = str(799)
# n = input()
count = n.count('4') + n.count('7')
if count == len(n):
    print('YES')
else:
    if int(n) % 4 == 0 or int(n) % 7 == 0 or int(n) % 47 == 0 or int(n) % 74 == 0:
        print('YES')
    else:
        print('NO')

print('\nA. I Wanna Be the Guy')
# n = int(input())
# x = list(map(int, input().split()))
# y = list(map(int, input().split()))
# a = set(x[1:]) | set(y[1:])
# a.discard(0)
# if len(a) == n:
#     print('I become the guy.')
# else:
#     print('Oh, my keyboard!')
