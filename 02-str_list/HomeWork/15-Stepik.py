print('\nStepik HomeWork')

print('\nЗадача 1')
a = [8, 11, 19, 200]
# a = list(map(int, input().split()))
print(a[1])

print('\nЗадача 2')
a = [7, 8, 9, 10, 11, 12, 13]
# a = list(map(int, input().split()))
print(a[2:5])

print('\nЗадача 3')
a = [89, 45, 7, 33, 65, 12]
# a = list(map(int, input().split()))
print(a[-3:])

print('\nЗадача 4')
a = [8, 32, 5, 87, 2, 43, 53, 23, 5]
# a = list(map(int, input().split()))
print(a[1::3])

print('\nЗадача 5')
a = [1, 2, 3]
# a = list(map(int, input().split()))
print(a[::-1])

print('\nЗадача 6 (1)')
top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']
top.pop()
top.append('Сверхъестественное')
top.insert(top.index('Друзья'), 'Настоящий детектив')
top.remove('Друзья')
print(top)

print('\nЗадача 6 (2)')
top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']
top[top.index('Бригада')] = 'Сверхъестественное'
top[top.index('Друзья')] = 'Настоящий детектив'
print(top)

print('\nЗадача 6 (3)')
top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']
top = ','.join(top).replace('Друзья', 'Настоящий детектив').replace('Бригада', 'Сверхъестественное').split(',')
print(top)
