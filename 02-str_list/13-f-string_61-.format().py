name = 'Семен'
surname = 'Семенович'
balance = 32.56

print('\nконкатенация:')
text = 'Дорогой ' + name + ' ' + surname + ', баланс вашего счета составляет ' + str(balance) + ' руб.'
print(text)

print('\n.format(args):')
text = 'Дорогой {0} {1}, баланс вашего счета составляет {2} руб.'.format(name, surname, balance)
print(text)

print('\n.format(kwargs):')
text = 'Дорогой {n} {m}, баланс вашего счета составляет {b} руб.'.format(b=balance, m=surname, n=name)
print(text)

print('\nf-string:')  # PEP 498 -- Literal String Interpolation (from Python 3.6 01-08-2015)
text = f'Дорогой {name} {surname}, баланс вашего счета составляет {balance} руб.'
print(text)

print('\nf-string формулы:')
text = f'Дорогой {name.lower()} {surname.upper()}, баланс вашего счета составляет {-balance * 2} руб.'
print(text)

print('\nf-string in dict:')

d = {
    'name': 'Семен',
    'surname': 'Семенович',
    'balance': 32.56
    }

text = f"""Дорогой {d['name']} {d['surname']}, баланс вашего счета составляет {d.get('balance')} руб."""
print(text)

print('\nРаспокование переменных:')
i = [1, 2, 3]
a, b, c = i
print(a, b, c)

print('\nNames:')
a = [
    ['Семен', 'Семенович', 32.56, 'm'],
    ['Тамара', 'Ивановна', 13.12, 'f'],
    ['Михаил', 'Анатольевич', 238.12, 'm'],
]

for name, surname, balance, g in a:
    print(name, surname, balance)

print('\nText:')
d = {
    'm': 'Дорогой',
    'f': 'Дорогая'
}

for name, surname, balance, gender in a:
    text = f'{d[gender]} {name} {surname}, баланс вашего счета составляет {balance} руб.'
    print(text)
