"""
Треугольник Паскаля при помощи двумерных списков.
Коэффициенты для бинома Ньютона (биномиальные коэффициенты).
"""

print('\nPascal Triangle:')
n = 4

print('\nEmpty Triangle:')
triangle = [[1] + [0] * n for i in range(n + 1)]
for i in triangle:
    print(*i)

print('\nFilling Triangle:')
for i in range(1, n + 1):
    for j in range(1, i + 1):
        triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
for i in triangle:
    print(*i)

print('\nFilled Triangle without 0:')
for i in range(n + 1):
    for j in range(i + 1):
        print(triangle[i][j], end=' ')
    print()
