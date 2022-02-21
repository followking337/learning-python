print('\nStepik HomeWork')

print('\nЗадача 1')
s = 'Конвульсия'
# s = input()
print('Что Вы сказали? {0}? Какое интересное слово'.format(s))
print('Что Вы сказали? {w}? Какое интересное слово'.format(w=s))

print('\nЗадача 2')
name = 'Daniel'
surname = 'Folomkin'
# name = input()
# surname = input()
print("Здравствуйте, {0} {1}!".format(surname, name))
print("Здравствуйте, {s} {n}!".format(n=name, s=surname))

print('\nЗадача 3')
s = 'Джордж'
# s = input()
print(f'Мое имя {s}!')

print('\nЗадача 4')
s = 'Messi'
age = 33
# s = input()
# age = int(input())
print(f"Hello {s.upper()}. You are {age} years old.")

print('\nЗадача 5')
rate = 56.77
buy = 11
# dollar_rat = float(input())
# dollar_buy = int(input())
print(f"Current dollar rate is {rate}. You want buy {buy} dollars\nYou must pay {buy * rate}")

print('\nЗадача 6')
name = 'Геннадий'
year = 1990
# name = input()
# year = int(input())
print(f'{name}, вам исполнится 77 лет в {year + 77}')

print('\nЗадача 7')
a = 11
b = 5
# a = int(input())
# b = int(input())
print(f'{a} / {b} = {a / b}', f'{a} // {b} = {a // b}', f'{a} % {b} = {a % b}', sep='\n')
print(f"""
{a} / {b} = {a / b}
{a} // {b} = {a // b}
{a} % {b} = {a % b}
""")
