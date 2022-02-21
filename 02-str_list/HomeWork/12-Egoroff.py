print('\nEgoroff and YouTube HomeWork')

print('\nЗадача №3736. Количество слов')
x = 'hello world'
# x = input()
print(x.split())
print(len(x.split()))
# print(x.split().count(x.split()))

print('\n1108. Defanging an IP Address')
address = "1.1.1.1"
print(address.replace('.', '[.]'))

print('\nЗадача №3745. Удаление символа')
x = 'Bilbo.Baggins@bagend.hobbiton.shire.me'
# x = input()
print(x.replace('@', ''))

print('\nЗадача №3747. Вставка символов')
x = 'Python'
# x = input()
print(x.replace('', '*'))
print(x.replace('', '*')[1:-1])
print(x.replace('', '*', 6)[1:])
print('*'.join(x))

print('\nКапитализация слова')
x = 'konjac'
# x = input()
print(x.upper()[0] + x[1:])

print('\nЧат')
s = 'pnnepelqomhhheollvlo'
for i in range(len(s)):
    if 10 <= i <= 99:
        print(s[i].rjust(2, ' '), end=' ')
    else:
        print(s[i], end=' ')
print()
for i in range(len(s)):
    print(i, end=' ')
print()
if s.find('h') < s.find('e', s.find('h')+1) < s.find('l', s.find('e', s.find('h')+1)+1) < \
    s.find('l', s.find('l', s.find('e', s.find('h')+1)+1)+1) < \
        s.find('o', s.find('l', s.find('l', s.find('e', s.find('h')+1)+1)+1)+1):
    print('YES')
else:
    print('NO')

print(s.find('h'))
print(s.find('e', s.find('h')+1))
print(s.find('l', s.find('e', s.find('h')+1)+1))
print(s.find('l', s.find('l', s.find('e', s.find('h')+1)+1)+1))
print(s.find('o', s.find('l', s.find('l', s.find('e', s.find('h')+1)+1)+1)+1))

s = 'hlelo'
flag = 'YES'
for i in 'hello':
    if s.find(i) >= 0:
        s = s[s.find(i)+1:]
    else:
        flag = 'NO'
print(flag)

print('\nЗадача №3739. Первое и последнее вхождение')
s = 'oficef'
# s = input()
if 'f' in s[:s.find('f')+1] and 'f' in s[s.find('f')+1:]:
    print(s.find('f'), s.rfind('f'))
elif 'f' in s:
    print(s.find('f'))

print('\nЗадача №3741. Удаление фрагмента')
s = 'In the hole in the ground there lived a hobbit'
# s = input()
print(s[:s.find('h')] + s[s.rfind('h')+1:])

print('\nЗадача №3738. Переставить два слова')
s = 'Hello, world!'
print(s[s.find(' ')+1:], s[:s.find(' ')])
print(*s.split()[::-1])

print('\nЗадача №3740. Второе вхождение')
s = 'oficef'
# s = input()
if 'f' in s[:s.find('f')+1] and 'f' in s[s.find('f')+1:]:
    print(s.find('f', s.find('f') + 1))
elif 'f' in s:
    print(-1)
elif 'f' not in s:
    print(-2)

print('\nДабстеп')
s = 'WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB'
# s = input()
print(s.replace('WUB', ' ').strip().replace('  ', ' '))

print('\nКарточки')
N = 10
s = 'nznooeeoer'
# N = int(input())
# s = input()
z = s.count('z')
e = s.count('e')
r = s.count('r')
o = s.count('o')
n = s.count('n')
count_1 = min(o, n, e)
# print(count_1)
o -= count_1
n -= count_1
e -= count_1
count_0 = min(z, e, r, o)
# print(count_0)
print('1 ' * count_1, '0 ' * count_0, sep='')
