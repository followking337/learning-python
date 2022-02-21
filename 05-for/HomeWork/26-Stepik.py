print('\nStepik HomeWork')

print('\nЗадача 1')
n = 3
# n = int(input())
for i in range(1, n + 1):
    print(i)

print('\nЗадача 2')
n = 3
# n = int(input())
for i in range(n, 0, -1):
    print(i)

print('\nМинутка сожаления')
for i in range(3):
    print('Надо было брать биткоин в 2012!')
print()
print('Надо было брать биткоин в 2012!\n' * 3)

[print('Надо было брать биткоин в 2012!') for i in range(3)]

print('\nПовторение - мать учения')
s = 'I am not smarter than the president'
n = 3
# s = input()
# n = int(input())
for i in range(n):
    print(s)
print()
print((s + '\n') * n)

[print(s) for i in range(n)]

print('\nFizzBuzz')
a, b = 9, 15
# a = int(input())
# b = int(input())
for i in range(a, b+1):
    print([i, 'Fizz', 'Buzz', 'FizzBuzz'][(not i % 3) + 2 * (not i % 5)])

print('\nКвадрат и куб')
a, b = 1, 5
# a, b = [int(input()) for i in range(2)]
for i in range(a, b + 1):
    print(f'Число {i}; его квадрат = {i ** 2}; его куб = {i ** 3}')

print('\nA. Мишка и игра (1)')
# n = int(input())
# wins_mishka = 0
# wins_cris = 0
# for i in range(1, n+1):
#     m, c = map(int, input().split())
#     if m > c:
#         wins_mishka += 1
#     elif m < c:
#         wins_cris += 1
# print(wins_mishka, wins_cris)
# print('Mishka' if wins_mishka > wins_cris else 'Chris' if wins_mishka < wins_cris else 'Friendship is magic!^^')

print('\nA. Мишка и игра (2)')
# x = y = 0
# for _ in range(int(input())):
#     a, b = input().split()
#     x += int(a > b)
#     y += int(a < b)
# print(x, y)

print('\nA. Мишка и игра (3)')
# x = y = 0
# for _ in range(int(input())):
#     a = list(map(int, input().split()))
#     if a[0] > a[1]:
#         x += 1
#     elif a[1] > a[0]:
#         y += 1
# print(x, y)

print('\nСудьба и рок (1)')
# n = int(input())
# for i in range(1, n + 1):
#     s = input().lower()
#     if 'рок' in s:
#         print(i, s.index('рок')+1)

print('\nСудьба и рок (2)')
# n = int(input())
# t = ''
# r = 'рок'
# for i in range(1, n + 1):
#     s = input().lower()
#     if r in s:
#         t += f'{i} {s.index(r) + 1}\n'
# print(t[:-1])

print('\nРецепт без соли (1)')
# n = int(input())
# a = []
# for i in range(n):
#     s = input()
#     a.append(s)
#     if 'соль' in s:  # if 'соль' not in s:
#         a.pop()         # a.append(s)
# print(', '.join(a))

print('\nРецепт без соли (2)')
# a = list(map(input, range(int(input()))))  # печатает помимо 01234
# a = [input() for i in range(int(input()))]
# print(*[i for i in a if 'соль' not in i], sep=', ')

print('\nКратные 3 или 5')
n = 9
# n = int(input())
s = 0
for i in range(1, n):
    if i % 3 == 0 or i % 5 == 0:
        s += i
print(s)

print('\nЗадача 7')
s = 0
for i in range(50, 101):
    s += i**3
print(s)
print(sum([i**3 for i in range(50, 101)]))

print('\nA. Слишком длинные слова (1)')
# n = int(input())
# t = ''
# for i in range(n):
#     s = input()
#     if len(s) > 10:
#         t += s[0] + str(len(s)-2) + s[-1] + '\n'
#     else:
#         t += s + '\n'
# print(t[:-1])

print('\nA. Слишком длинные слова (2)')
# a = [input() for i in range(int(input()))]
# print(*[i[0] + str(len(i)-2) + i[-1] if len(i) > 10 else i for i in a], sep='\n')

print('\nA. Слишком длинные слова (3)')
# [print(f'{i[0]}{len(i) - 2}{i[-1]}' if len(i) > 10 else i) for i in [input() for i in range(int(input()))]]
