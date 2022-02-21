print('\nYouTube and Egoroff HomeWork')

print('\nПриветствие')
name = 'Daniel'
surname = 'Folomkin'
# name = str(input('Введите имя'))
# surname = input('Введите фамилию')
print('Здравствуйте,', surname, name + '!')

print('\nСравнение с соседними числами')
n = 15
# number = int(input())
print(n - 1, '<', n, '<', n + 1)

print('\nУмножение над двумя числами')
a = 2
b = 3
# a = int(input())
# b = int(input())
print(a, '*', b, '=', a * b)

print('\nЗадача №3456. Hello, Harry!')
name = 'Harry'
# name = input()
print('Hello, ' + name + '!')

print('\nЗадача №3457. Следующее и предыдущее')
number = 179
# number = int(input())
print('The next number for the number', number, 'is', str(number + 1) + '.')
print('The previous number for the number', number, 'is', str(number - 1) + '.')

print('\n77 Лет')
name = 'Daniel'
year_of_birth = 1990
# name = input()
# year_of_birth = int(input())
print(name + ', вам исполнится 77 лет в', year_of_birth + 77)
print(f'{name}, вам исполнится 77 лет в {year_of_birth + 77}')

print('\nЗадача 5')
s = '$'
# s = input()
print(1, 2, 3, 4, 5, sep=s)
