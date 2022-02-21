print('\nЗадача 5')
# d = {}
# s = input()
# while s != 'конец':
#     key, value = s.split(': ')
#     d[key] = int(value)
#     s = input()
# [print(key) for key, value in sorted(d.items(), key=lambda par: -par[1])]  # reverse=True
# [print(key) for key in sorted(d, key=d.get, reverse=True)]

print('\nРейтинг таксистов')
# d = {}
# while True:
#     s = input()
#     if s == 'конец':
#         break
#     name, mark = s.split(', ')
#     d[name] = d.get(name, []) + [int(mark)]
# # for i in d:
# #     d[i] = sum(d[i]) / len(d[i])
# for name, mark in d.items():
#     d[name] = sum(mark) / len(mark)
# for i in sorted(d.items(), key=lambda x: (-x[1], x[0])):
#     print(*i)

print('\nПремия Оскар (1)')
# d = {}
# n = int(input())
# for i in range(n):
#     s = input()
#     d[s] = d.get(s, 0) + 1
# print('\nСписок d:')
# for i in d.items():
#     print(*i)
# print('\nРешение 1:')
# print(f'{max(d, key=d.get)}, {d[max(d, key=d.get)]}')
# print(f'{min(d, key=d.get)}, {d[min(d, key=d.get)]}')
# v = {}
# for name, count in d.items():
#     v[count] = name
# print('\nСписок v:')
# for i in v.items():
#     print(*i)
# print('\nРешение 2:')
# print(f'{v[max(v)]}, {max(v)}')
# print(f'{v[min(v)]}, {min(v)}')

print('\nПремия Оскар (2)')
# d = {}
# for i in range(int(input())):
#     s = input()
#     d[s] = d.get(s, 0) + 1
# d = sorted(d.items(), key=lambda para: -para[1])
# print(d[0][0], d[0][1], sep=', ')
# print(d[-1][0], d[-1][1], sep=', ')

print('\nТелефонная книга (1)')
# d = {}
# for i in range(int(input())):
#     number, name = input().split()
#     d[name] = d.get(name, []) + [int(number)]
# for i in range(int(input())):
#     s = input()
#     if s in d:
#         print(*d[s])
#     else:
#         print('Неизвестный номер')

print('\nТелефонная книга (2)')
# d = {}
# for i in range(int(input())):
#     number, name = input().split()
#     d[name] = d.get(name, []) + [int(number)]
# for i in range(int(input())):
#     print(*d.get(input(), ['Неизвестный номер']))


print('\nТелефонная книга (3)')
# d = {}
# for i in range(int(input())):
#     number, name = input().split()
#     d[name] = d.get(name, '') + number + ' '
# for i in range(int(input())):
#     print(d.get(input(), 'Неизвестный номер ')[:-1])

print('\nДни рождения')
# d = {}
# for i in range(int(input())):
#     name, day, month = input().split()
#     d[month] = d.get(month, []) + [name]  # d.setdefault(month, []).append(name)
# for i in range(int(input())):
#     print(*sorted(d.get(input(), ['Нет данных'])))
