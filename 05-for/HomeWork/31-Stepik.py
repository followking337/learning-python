print('\nСумма главной диагонали (1)')
# n = int(input())
# a = []
# accumulative = 0
# for i in range(n):
#     a.append(list(map(int, input().split())))
#     for j in range(n):
#         if i == j:
#             accumulative += a[i][j]
# print(accumulative)

print('\nСумма главной диагонали (2)')
# n = int(input())
# s = 0
# for i in range(n):
#     s += int(input().split()[i])
# print(s)

print('\nСумма главной диагонали (3)')
# n = int(input())
# a = []
# accumulative = 0
# for i in range(n):
#     a.append(list(map(int, input().split())))
#     accumulative += a[i][i]
# print(accumulative)

print('\nСумма главной диагонали (4)')
# n = int(input())
# a = [list(map(int, input().split())) for i in range(n)]
# a = [[int(j) for j in input().split()] for i in range(n)]
# print(sum(a[i][i] for i in range(n)))

print('\nТранспонирование - 1')
# n = int(input())
# a = []
# for i in range(n):
#     a.append(list(map(int, input().split())))
#
# for j in range(n):
#     for i in range(n):
#         print(a[i][j], end=' ')
#     print()

print('\nТранспонирование - 2')
# n = int(input())
# a = []
# for i in range(n):
#     a.append(list(map(int, input().split())))
#
# for j in range(n-1, -1, -1):
#     for i in range(n-1, -1, -1):
#         print(a[i][j], end=' ')
#     print()

print('\nТранспонирование - 3')
# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for i in range(n)]
#
# for i in range(n):
#     for j in range(m-1, -1, -1):
#         print(a[i][j], end=' ')
#     print()

print('\nТранспонирование - 4')
# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for i in range(n)]
#
# for i in range(n-1, -1, -1):
#     for j in range(m):
#         print(a[i][j], end=' ')
#     print()

print('\nA. Красивая матрица')
# a = [list(map(int, input().split())) for i in range(5)]
#
# for i in range(5):
#     for j in range(5):
#         if a[i][j] == 1:
#             print(abs(i+1-3) + abs(j+1-3))

print('\nСумма строк и столбцов двумерного массива')
# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for i in range(n)]
# for i in range(n):
#     rows = 0
#     for j in range(m):
#         rows += a[i][j]
#     print(rows, end=' ')
# print()
# for j in range(m):
#     columns = 0
#     for i in range(n):
#         columns += a[i][j]
#     print(columns, end=' ')

print('\nЗадача №355. Симметричная ли матрица?')
# n = int(input())
# a = [list(map(int, input().split())) for i in range(n)]
# symmetric = True
# for i in range(n):
#     for j in range(i, n):
#         if a[i][j] != a[j][i]:
#             symmetric = False
# print('Yes' if symmetric else 'No')

print('\nЗадача №356. Состязания (1)')
# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for i in range(n)]
# max_points = 0
# competitor = 0
# for i in range(n):
#     total = 0
#     for j in range(m):
#         total += a[i][j]
#     if total > max_points:
#         max_points = total
#         competitor = i
# print(max_points, competitor, sep='\n')

print('\nЗадача №356. Состязания (2)')
# n, m = map(int, input().split())
# a = []
# for i in range(n):
#     a.append(list(map(int, input().split())))
# points = []
# for i in range(n):
#     total = 0
#     for j in range(m):
#         total += a[i][j]
#     points.append(total)
# print(max(points), points.index(max(points)), sep='\n')

print('\nЗадача №356. Состязания (3)')
# n, m = map(int, input().split())
# max_val = (0, 0)
# for i in range(n):
#     s = sum(map(int, input().split()))
#     if s > max_val[0]:
#         max_val = s, i
# print(*max_val, sep='\n')

print('\nЗадача №357. Состязания - 2')
# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for i in range(n)]
# max_points = 0
# competitor = []
# for i in range(n):
#     for j in range(m):
#         if a[i][j] > max_points:
#             max_points = a[i][j]
#             competitor[0], competitor[1] = i, j
# print(max_points)
# print(*competitor)

print('\nЗадача №358. Состязания - 3 (1)')
# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for i in range(n)]
# max_general = 0
# champion = 0
# total_per_competitor = []
# for i in range(n):
#     total = 0
#     max_points = 0
#     for j in range(m):
#         total += a[i][j]
#         if a[i][j] > max_points:
#             max_points = a[i][j]
#     # print(i, max_points, total)
#     total_per_competitor.append(total)
#     if max_points > max_general:
#         max_general = max_points
#         champion = i
#     elif max_points == max_general:
#         if total_per_competitor[i] > total_per_competitor[champion]:
#             champion = i
# # print(total_per_competitor)
# print(champion)

print('\nЗадача №358. Состязания - 3 (2)')
# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for i in range(n)]
# max_general = 0
# champion = 0
# total_per_competitor = []
# for i in range(n):
#     total = sum(a[i])
#     max_points = max(a[i])
#     # print(i, max_points, total)
#     total_per_competitor.append(total)
#     if max_points > max_general:
#         max_general = max_points
#         champion = i
#     elif max_points == max_general:
#         if total_per_competitor[i] > total_per_competitor[champion]:
#             champion = i
# # print(total_per_competitor)
# print(champion)

print('\nЗадача №358. Состязания - 4.1')
# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for i in range(n)]
# max_per_competitor = []
# for i in range(n):
#     max_points = 0
#     for j in range(m):
#         if a[i][j] > max_points:
#             max_points = a[i][j]
#     max_per_competitor.append(max_points)
# print(max_per_competitor)
# print(max_per_competitor.count(max(max_per_competitor)))

print('\nЗадача №358. Состязания - 4.2')
# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for i in range(n)]
# max_general = 0
# count = 0
# for i in range(n):
#     max_points = 0
#     for j in range(m):
#         if a[i][j] > max_points:
#             max_points = a[i][j]
#     # print(i, max_points)
#     if max_points > max_general:
#         max_general = max_points
#         count = 1
#     elif max_points == max_general:
#         count += 1
# print(count)

print('\nЗадача №358. Состязания - 4.3')
# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for i in range(n)]
# max_general = 0
# count = 0
# for i in range(n):
#     max_points = max(a[i])
#     # print(i, max_points)
#     if max_points > max_general:
#         max_general = max_points
#         count = 1
#     elif max_points == max_general:
#         count += 1
# print(count)

print('\nСимпатичный узор (1) (прошел в Stepik но не прошел в acmp.ru)')
# a = [input() for i in range(4)]
# # print(a)
# charming = True
# index = [-1, -1]
# for i in a:
#     if 'BB' in i:
#         if index[0] == i.index('BB'):
#             charming = False
#             break
#         else:
#             index[0] = i.index('BB')
#     elif 'WW' in i:
#         if index[1] == i.index('WW'):
#             charming = False
#             break
#         else:
#             index[1] = i.index('WW')
# print('Yes' if charming else 'No')

print('\nСимпатичный узор (2)')
# a = [list(input()) for i in range(4)]
# # print(a)
# charming = 'Yes'
# for i in range(3):
#     for j in range(3):
#         if a[i][j] == a[i][j+1] == a[i+1][j] == a[i+1][j+1]:
#             charming = 'No'
#             break
# print(charming)

print('\nМиша и негатив')
# n, m = map(int, input().split())
# a = [input() for i in range(n)]
# input()
# b = [input() for j in range(n)]
# count = 0
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == b[i][j]:
#             count += 1
# print(count)

print('\nA. Таблица умножения (1)')
n, x = 6, 12
# n, x = map(int, input().split())
count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i * j == x:
            count += 1
print(count)

print('\nA. Таблица умножения (2)')
n, x = 6, 12
# n, x = map(int, input().split())
i = 1
count = 0
while i * i <= x:
    if x % i == 0 and i <= n and x//i <= n:
        # print(i, x//i)
        count += 1
        if i != x//i:
            count += 1
    i += 1
print(count)

print('\nA. Матчи (1)')
# n = int(input())
# a = [[int(j) for j in input().split()] for i in range(n)]
# count = 0
# for i in range(n):
#     for j in range(n):
#         if a[i][0] == a[j][1]:
#             count += 1
#             # print(a[i][0], a[j][1])
# print(count)

print('\nA. Матчи (2)')
# n = int(input())
# a = [list(map(int, input().split())) for i in range(n)]
# count = 0
# for i in range(n-1):
#     for j in range(i+1, n):
#         print(i, j, sep='', end=' ')
#         if a[i][0] == a[j][1]:
#             count += 1
#         if a[i][1] == a[j][0]:  # no puede ser elif porque al cumplir if no llega hasta elif
#             count += 1
#     print()
# print(count)

print('\nA. Матчи (3)')


# class Team:
#
#     def __init__(self, h, g):
#         self.home = h
#         self.guest = g
#
#
# n = int(input())
# a = []
# for i in range(n):
#     home, guest = map(int, input().split())
#     a.append(Team(home, guest))
# count = 0
# for i in range(n-1):
#     for j in range(i+1, n):
#         if a[i].home == a[j].guest:
#             count += 1
#         if a[i].guest == a[j].home:  # no puede ser elif porque al cumplir if no llega hasta elif
#             count += 1
# print(count)

print('\nМорской бой - 2 (1)')
# n, m = map(int, input().split())
# a = ['.' + input() + '.' for i in range(n)]
# b = ['.' * (m+2)]
# a = b + a + b
# # for i in a:
# #     print(i)
# count = 0
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         if a[i][j] == '.':
#             if a[i+1][j] == '.' and a[i-1][j] == '.' and a[i][j+1] == '.' and a[i][j-1] == '.':
#                 count += 1
# print(count)

print('\nМорской бой - 2 (2)')
# n, m = map(int, input().split())
# a = ['.' + input() + '.' for i in range(n)]
# b = ['.' * (m+2)]
# a = b + a + b
# for i in a:
#     print(i)
# count = 0
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         temp = a[i-1][j] + a[i][j-1:j+2] + a[i+1][j]
#         # print(a[i-1][j], a[i][j-1:j+2], a[i+1][j])
#         count += temp.count('*') == 0
# print(count)

print('\nЗадача №363. Заполнение змейкой')
n, m = 4, 10
# n, m = map(int, input().split())
for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            print(j+(m*i), end=' ')
        elif i % 2 == 1:
            print((m-1)+(m*i)-j, end=' ')
    print()

print('\nA. Фотографии Брейна (1)')
# n, m = map(int, input().split())
# a = [input() for i in range(n)]
# s = '#Black&White'
# for i in a:
#     if 'C' in i or 'Y' in i or 'M' in i:
#         s = '#Color'
# print(s)

print('\nA. Фотографии Брейна (2)')
# n, m = map(int, input().split())
# a = [input().split() for i in range(n)]
# s = '#Black&White'
# for i in range(n):
#     for j in range(m):
#         if a[i][j] in 'CYM':  # if a[i][j] not in 'BWG':
#             s = '#Color'
# print(s)

print('\nA. Фотографии Брейна (3)')
# n, m = map(int, input().split())
# a = ' '.join([input() for i in range(n)])
# print(a)

print('\nСпираль (1)')
n = 4
# n = int(input())
a = [[0] * n for i in range(n)]
for i in range(1, n+1):
    for j in range(1, n+1):
        print(j, end=' ')
    print()

print('\nСпираль (2)')
n = 10
# n = int(input())
a = [['**'] * n for i in range(n)]
turn = 0
count = 1
rows = n
columns = n
i = 0.5
for i in range(2):
    if turn == 0:
        for j in range(n-columns, columns):
            a[n-rows][j] = count
            count += 1
        rows -= 1
    elif turn == 1:
        for j in range(n-rows, rows):
            a[j][columns-1] = count
            count += 1
    # elif turn == 2:
    #     for j in range(n-1-int(i), -1, -1):
    #         a[rows][j] = count
    #         count += 1
    # elif turn == 3:
    #     for j in range(n-1-1, 0, -1):
    #         a[j][0] = count
    #         count += 1
    # elif turn == 4:
    #     for j in range(1, columns):
    #         a[1][j] = count
    #         count += 1
    turn += 1
    if turn == 5:
        turn = 1


for i in a:
    print(*i)

print('\nA. Тортминатор (1)')
# r, c = map(int, input().split())
# a = [input() for i in range(r)]
# row_count = 0
# column_count = 0
# for i in a:
#     if 'S' not in i:
#         row_count += 1
# # print(row_count)
# b = []
# for j in range(c):
#     t = ''
#     for i in range(r):
#         t += a[i][j]
#     b.append(t)
# for i in b:
#     if 'S' not in i:
#         column_count += 1
# # print(column_count)
# print(r * column_count + c * row_count - row_count * column_count)

print('\nA. Тортминатор (2)')
# r, c = map(int, input().split())
# a = [input() for i in range(r)]
# b = [[0] * c for i in range(r)]
# for i in range(r):
#     if 'S' not in a[i]:
#         for j in range(c):
#             b[i][j] = 1
# for j in range(c):
#     is_find = False
#     for i in range(r):
#         if a[i][j] == 'S':
#             is_find = True
#             break
#     if not is_find:
#         for i in range(r):
#             b[i][j] = 1
# count = 0
# for i in b:
#     count += i.count(1)
# print(count)

print('\nEgoroff HomeWork')

print('\nСумма матриц')
# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for i in range(n)]
# input()
# b = [list(map(int, input().split())) for i in range(n)]
# c = [[0] * m for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         c[i][j] = a[i][j] + b[i][j]
# for i in c:
#     print(*i)
