print('\nEgoroff and Stepik HomeWork')

print('\n"В поисках простой задачи"')
n = 3
a = [0, 0, 1]
# n = int(input())
# a = list(map(int, input().split()))
if 1 in a:
    print('HARD')
else:
    print('EASY')

print('\nA. Новый год: встреча друзей')
x1, x2, x3 = 30, 20, 10
# x1, x2, x3 = map(int, input().split())
print(max(x1, x2, x3) - min(x1, x2, x3))

print('\nДефиснутая фраза (1)')
s = 'Бросай курить'
# s = input()
print(s.upper().replace('', '-')[1:-1].replace('- -', ' '))

print('\nДефиснутая фраза (2)')
a, b = 'Бросай курить'.upper().split()
# a, b = input().upper().split()
a = list(a)
b = list(b)
print('-'.join(a), '-'.join(b))

print('\nСлово с новой строки')
s = 'Буря мглою небо кроет'
# s = input()
for word in s.split():
    print(word)
print()
a = s.split()
print('\n'.join(a))

print('\nИнициалы')
s = 'Марина Денисовна Климова'
# s = input()
print(f'{s.split()[-1]} {s[0]}.{s[s.find(" ") + 1]}.')
a = s.split()
print(f'{a[-1]} {a[0][0]}.{a[1][0]}.')

print('\nЗадача 1')
# a = input().split()
a = [8, 11, 'Привет', True, 45.5]
a.reverse()
print(*a)
# print(*a[::-1])

print('\nЗадача 2')
# a = list(map(int, input().split()))
a = [99, 999, 9, 999]
print(a.count(999))
