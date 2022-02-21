"""
Словарь (dict) — неупорядоченная коллекция произвольных объектов с доступом по ключу.
Словарь более известен как ассоциативный массив. Словарь состоит из набора пар "Ключ-Значение".
И в отличии от списка, где к каждому элементу можно обратиться по его порядковому номеру(индексу),
в словаре обращение к элементу происходит по ключу.
key: value
"""
print('\nСозднания словаря:')
print('\nСпособ 1:')
d = {
    'Moscow': 495,
    'Piter': 812,
    'Penza': 8412
}
print(d)

print('\nСпособ 2:')
r = dict(Moscow=495, Piter=812, Penza=8412)  # только когда ключи типа str (без ковычек), функция dict приобразует
print(r)                                     # их в ключи, используеться когда ключи строковые типы.

print('\nСпособ 3:')
a = [['Moscow', 495], ['Piter', 812], ['Penza', 8412]]  # a = [[key1, value1], [key2, value2], [key3, value3]]
t = dict(a)
print(t)

print('\nСпособ 4:')
q = dict.fromkeys(['a', 'b', 'c'])
print(q)
q = dict.fromkeys(['a', 'b', 'c'], 100)
print(q)
q = dict.fromkeys(['a', 'b', 'c'], [1, 2, 3])
print(q)

print('\nПустой словарь:')
d = {}
print(d, type(d))
d = dict()
print(d, type(d))

print('\nKeys and Values:')  # key не может быть изменяемым типом объекта (list), value может быть любым типом значения
d = {
    1: 45,
    'hello': 'two',
    3: [1, 2, 3]
}
print(d)

print('\nОбращение к словарю:')
print(d[1])
print(d['hello'])
print(d[3])
# print(d[0])  # KeyError: 0

print('\nДобавление в словарь:')  # к не существующему ключу добавляем значение
d = {
    1: 'one',
    2: 'two',
    3: 'three'
}
d[4] = 'four'
d[5] = 'five'
print(d)

print('\nИзменения в словаре:')  # к существующему ключу изменяем значение
d[3] = 'три'
print(d)

print('\nУпражнение:')
person = {}
s = 'IVANOV IVAN Samara SGU 5 4 5 5 4 3 5'
s = s.split()
print(s)
person['lastName'] = s[0]
person['firstName'] = s[1]
person['city'] = s[2]
person['university'] = s[3]
person['marks'] = []
for i in s[4:]:
    person['marks'].append(int(i))
print(person)

print('\nУдаление из словаря:')  # keyword del
d = {
    1: 'one',
    2: 'two',
    3: 'three'
}
print(d)
del d[3]
print(d)
# del d[4]  # KeyError: 4

print('\nФункции подерживающии словаря:')
d = {
    1: 'one',
    2: 'two',
    3: 'three'
}
print(d)
print(len(d))
print(1 in d, 5 in d, 7 not in d)  # по ключу

print('\nИнструкция if elif else:')
if 4 in d:
    print(d[4])
else:
    d[4] = 'four'
print(d)

print('\nЦыкл for:')
for key in d:
    print(key, d[key])

print('\nМетоды словаря:')

print('\ndict.clear():')
d.clear()
print(d)

print('\ndict.get():')  # в случае существования, выдает значения существующего ключа
d = {                   # в случае отсуствия, выдает None либо назначеный в нем параметр
    1: 'one',
    2: 'two',
    3: 'three'
}
print(d.get(1))
print(d.get(4))
print(d.get(4, 'No such key'))
print(d.get(5, [1, 2, 3]))
print(d.get(3, 'No such key'))
print(d)

print('\ndict.setdefault():')  # в случае отсуствия, создает пару ключ-значение (None)
print(d.setdefault(1))         # в случае существования, выдает значения существующего ключа
print(d.setdefault(4))
print(d.setdefault(5, 'five'))
print(d.setdefault(1, 'seven'))
# print(d.setdefault())  # TypeError: setdefault expected at least 1 argument, got 0
print(d)

print('\ndict.pop():')  # удаляет назначеный ключ и выдает его значение
print(d.pop(4))
print(d.pop(5))
# print(d.pop(6))  # KeyError: 6
# print(d.pop())  # TypeError: pop expected at least 1 argument, got 0
print(d)

print('\ndict.popitem():')  # удаляет random пару ключ-значение и выводит её ключ-значение
print(d.popitem())
print(d)
print(d.popitem())
print(d)
print(d.popitem())
print(d)
# print(d.popitem())  # KeyError: 'popitem(): dictionary is empty'
# print(d)

print('\ndict.keys():')
d = {
    1: 'one',
    2: 'two',
    3: 'three'
}
print(d.keys(), type(d.keys()))
for key in d.keys():
    print(key, d[key])

print('\ndict.values():')
print(d.values(), type(d.values()))
for values in d.values():
    print(values)

print('\ndict.items():')
print(d.items(), type(d.items()))
for par in d.items():
    print(par)  # <class 'tuple'>
for par in d.items():
    print(par[0], par[1])  # par[2] IndexError: tuple index out of range
for key, value in d.items():
    print(key, value)
