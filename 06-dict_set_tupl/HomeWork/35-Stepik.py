print('\nЗадача 1')
s = 'ZZzzzZ34 WWw777'
# s = input()
d = {}
for i in s.lower():
    if i.isalpha():
        d[i] = d.get(i, 0) + 1
print(d)
# s = input().lower()
print({i: s.count(i) for i in s if i.isalpha()})

print('\nЗадача 2')
data = {
    'my_friends':
        {'count': 10,
         'items': [{'first_name': 'Kurt',
                    'id': 621547005,
                    'last_name': 'Cobain',
                    'bdate': '31.8.2005'},
                   {'first_name': 'Виолетта',
                    'id': 484200150,
                    'last_name': 'Кастилио'},
                   {'first_name': 'Иринка',
                    'id': 21886133,
                    'last_name': 'Бушуева',
                    'bdate': '28.8.1942'},
                   {'first_name': 'Данил',
                    'id': 282456573,
                    'last_name': 'Греков',
                    'bdate': '4.7.2002'},
                   {'first_name': 'Валентин',
                    'id': 184902932,
                    'last_name': 'Долматов',
                    'bdate': '25.5'},
                   {'first_name': 'Евгений',
                    'id': 620469646,
                    'last_name': 'Шапорин',
                    'bdate': '6.12.1982'},
                   {'first_name': 'Ангелина',
                    'id': 622328862,
                    'last_name': 'Краснова',
                    'bdate': '4.11.1995'},
                   {'first_name': 'Иван',
                    'id': 576015198,
                    'last_name': 'Вирин',
                    'bdate': '2.2.1915'},
                   {'first_name': 'Паша',
                    'id': 386922406,
                    'last_name': 'Воронов',
                    'bdate': '27.9'},
                   {'first_name': 'Ольга',
                    'id': 622170942,
                    'last_name': 'Савченкова',
                    'bdate': '20.12'}]
         }
}
a = []
for i in data['my_friends']['items']:
    a.append(i['first_name'])
for i in sorted(a):
    print(i)
# print(*sorted(a), sep='\n')
print('----------------------')
print(*sorted([i['first_name'] for i in data['my_friends']['items']]), sep='\n')
print('----------------------')
for i in sorted(data['my_friends']['items'], key=lambda x: x['first_name']):
    print(i['first_name'])

print('\nАнаграмма')
s1 = 'abracadabra'
s2 = 'cadabraabra'
# s1 = input()
# s2 = input()
d1, d2 = {}, {}
for i in s1:  # d1 = {i: s1.count(i) for i in s1}
    d1[i] = d1.get(i, 0) + 1
for i in s2:  # d2 = {i: s2.count(i) for i in s2}
    d2[i] = d2.get(i, 0) + 1
print('YES' if d1 == d2 else 'NO')

print('\nАзбука Морзе (1)')
morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
         'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
         'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••'}
s = 'Houston we have a problem'
# s = input()
for i in s.lower():
    if i != ' ':
        print(morze[i], end=' ')
    else:
        print()

print()

print('\nАзбука Морзе (2)')
s = 'Houston we have a problem'
# s = input()
a = s.lower().split()
for i in a:
    for j in i:
        print(morze.get(j), end=' ')
    print()

print('\nA. Щедрый Кефа')
n, k = 36, 13
s = 'bzbzcffczzcbcbzzfzbbfzfzzbfbbcbfccbf'
# n, k = map(int, input().split())
# s = input()
d = {i: s.count(i) for i in s}
v = {i: 0 for i in d}
# print(d)
while d != v and k > 0:
    for i in d:
        if d[i] > 0:
            d[i] -= 1
        # print(k, d)
    k -= 1
# print(d)
print('NO' if d != v else 'YES')
