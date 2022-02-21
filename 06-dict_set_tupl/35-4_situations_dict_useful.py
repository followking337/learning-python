print('\n1. Подсчет количества объектов (1. Всех)')
s = 'qqwwer'
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for i in d:
    print(i, d[i])

print('\nВывод отсортированый')
for i in sorted(d):
    print(i, d[i])

print('\n1. Подсчет количества объектов (2. Только букв через if)')
s = 'qqww1234541sfe34dsf4524?=)=/(%·"$aefe156er'
d = {}
for i in s:
    if i.isalpha():
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
for i in sorted(d):
    print(i, d[i])

print('\n1. Подсчет количества объектов (2. Только букв через get)')
s = 'qqww1234541sfe34dsf4524?=)=/(%·"$aefe156er'
d = {}
for i in s:
    if i.isalpha():
        d[i] = d.get(i, 0) + 1
for i in sorted(d):
    print(i, d[i])

print('\n2. Замена разряженного списка')
s = 'assaqw'
d = {}
for i in s:
    if i.isalpha():
        d[i] = d.get(i, 0) + 1
print(d)

print('\n3. Установление соответствия между объектами')
# words = {}
# while True:
#     s = input()
#     if s in words:
#         print(f'Слово {s} переводится как {words[s]}')
#     else:
#         print(f'Введите перевод слова {s}')
#         words[s] = input()

print('\n4. Хранение данных об объекте')
contacts = {
    'John Kennedy': {
        'birthday': '29-05-1917',
        'city': 'New York',
        'phone': None,
        'children': 3
    },
    'Arnold Schwarzenegger': {
        'birthday': '30-07-1947',
        'city': 'Gradec',
        'phone': '555-555-555',
        'children': 5
    },
    'Donald John Trump': {
        'birthday': '14-07-1946',
        'city': 'New York',
        'phone': '777-777-777',
        'children': 4
    }
}
persons = ['John Kennedy', 'Arnold Schwarzenegger', 'Donald John Trump']
print('\nОбращение ко всем данным')
for i in persons:
    print(i, contacts[i])

print('\nОбращение только к birthday')
for i in persons:
    print(i, contacts[i]['birthday'])

print('\nОбращение ко всем данным 1')
for i in persons:
    birthday = contacts[i]['birthday']
    city = contacts[i]['city']
    phone = contacts[i]['phone']
    children = contacts[i]['children']
    print(i, phone, city)

print('\nОбращение ко всем данным 2')
for i in persons:
    print(i)
    for data in contacts[i]:
        print(data, contacts[i][data])
