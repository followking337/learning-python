print('\nЗадача 1')


def keanu_reeves():
    print("YOU'RE BREATHTAKING")


keanu_reeves()

print('\nЗадача 2')


def summa_n(t):
    s = 0
    for i in range(1, t + 1):  # s = sum(range(1, t + 1))
        s += i
    print(f'Я знаю, что сумма чисел от 1 до {t} равна {s}')


summa_n(5)

print('\nЗадача 3')


def check_password(password):
    count_digit = 0
    is_capital_letter = False
    symbol = False
    for i in password:
        if i.isdigit():
            count_digit += 1
        if 'A' <= i <= 'Z':  # if i.isupper():
            is_capital_letter = True
        if i in '!@#$%*':
            symbol = True
    if count_digit >= 3 and is_capital_letter and symbol and len(password) >= 10:
        print('Perfect password')
    else:
        print('Easy peasy')


check_password('qwerty')
check_password('Qwerty1357!')

print('\nЗадача 4.1')


def count_letters(frase):
    N = K = 0
    for i in frase:
        if i.isupper():  # if i.isalpha():
            N += 1           # if i.islower():
        if i.islower():      # else:
            K += 1
    print('Количество заглавных символов:', N)
    print('Количество строчных символов:', K)


count_letters('Привет, Старина')

print('\nЗадача 4.2')


def count_letters(frase):
    N = K = 0
    for i in frase:
        N += i.isupper()
        K += i.islower()
    print('Количество заглавных символов:', N)
    print('Количество строчных символов:', K)


count_letters('Привет, Старина')
