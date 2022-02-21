print('\nБесконечный цикл')

print('\nbreak:')
i = 1
while True:
    print('Итерация Nº', i)
    if i == 10:
        break
        print('hi')  # this code is unreachable
    i += 1
print('hello')

print('\ncontinue:')
while True:
    a = input()
    if a == 'exit':
        break  # сразу выходим их цыкла
    if len(a) < 5:
        continue  # пропускает инструкции ниже continue внутри цыкла и перекидывает в начало цыкла
    print(a, len(a))

print('\nelse:')
i = 1
while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1
else:  # выполняется только в том случае если while заканчивается, не принудительно, сам по себе.
    print('good')
    print('job')
print('end')

print('\nПример 1 else:')
a = [54, 32, 65, 765, 32, 543]
while len(a) > 0:
    last = a.pop()
    if last % 2 != 0:
        print('Есть не четное число', last)
        break
else:
    print('Все числа четные')

print('\nПример 2 else:')
a = [54, 32, 2, 6, 32, 52]
while len(a) > 0:
    last = a.pop()
    if last % 2 != 0:
        print('Есть не четное число', last)
        break
else:
    print('Все числа четные')
