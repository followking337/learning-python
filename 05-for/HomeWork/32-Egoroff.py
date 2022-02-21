print('\nХудожник (1)')
# w, h = map(int, input().split())
# n = int(input())
# b = [[0] * w for j in range(h)]
# count = 0
# for i in range(n):
#     x1, y1, x2, y2 = map(int, input().split())
#     for x in range(x1, x2):
#         for y in range(y1, y2):
#             if b[x][y] == 0:
#                 b[x][y] = 1
#                 count += 1
# print(h * w - count)
# for i in b:
#     print(*i)

print('\nХудожник (2)')
# w, h = map(int, input().split())
# n = int(input())
# b = [[0] * w for j in range(h)]
# for i in range(n):
#     x1, y1, x2, y2 = map(int, input().split())
#     for x in range(x1, x2):
#         b[x][y1:y2] = [1] * (y2 - y1)
# count = 0
# for i in b:
#     for j in i:
#         if j == 0:
#             count += 1
# print(count)
# for i in b:
#     print(*i)

print('\nХудожник (3)')
# w, h = map(int, input().split())
# n = int(input())
# a = [list(map(int, input().split())) for i in range(n)]
# b = [[0] * w for j in range(h)]
# count = 0
# for y in range(n):
#     for i in range(a[y][0], a[y][2]):
#         for j in range(a[y][1], a[y][3]):
#             if b[i][j] == 0:
#                 b[i][j] = 1
#                 count += 1
# print(h * w - count)
# for i in b:
#     print(*i)

print('\nA. Максимум в таблице')
n = 5
# n = int(input())
a = [[1] * n for i in range(n)]
for i in range(1, n):
    for j in range(1, n):
        a[i][j] = a[i-1][j] + a[i][j-1]
for i in a:
    print(*i)
print(a[n-1][n-1])

print('\nЗадача №362. Треугольник Паскаля')
n, m = 3, 3
# n, m = map(int, input().split())
a = [[1] * m for i in range(n)]
for i in range(1, n):
    for j in range(1, m):
        a[i][j] = a[i-1][j] + a[i][j-1]
for i in a:
    print(*i)
