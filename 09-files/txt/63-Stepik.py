from string import punctuation

print('\nЗадача 1.1')


def file_read(file_name):
    file = open(file_name, encoding='utf-8')
    print(file.read())
    file.close()


file_read('333.txt')

print('\nЗадача 1.2')


def file_read(file_name):
    with open(file_name, "r", encoding='utf-8') as f:  # with закрывает файл автоматически
        print(f.read())


file_read('333.txt')

print('\nЗадача 2.1')


def create_file_with_numbers(n):
    file = open(f'range_{n}.txt', 'w')
    for i in range(1, n + 1):
        file.write(f'{i}\n')
    file.close()


create_file_with_numbers(5)

print('\nЗадача 2.2')


def create_file_with_numbers(n):
    with open(f'range_{n}.txt', 'w') as f:
        print(*[i for i in range(1, n + 1)], sep='\n', end='', file=f)


create_file_with_numbers(5)

print('\nЗадача 3.1')


def longest_word_in_file(file_name):
    file = open(file_name, 'r', encoding='utf=8')
    a = []
    b = []
    for row in file:
        for word in row.split():
            temp = word.strip(punctuation)
            a.append(temp)
            b.append(len(temp))
    file.close()
    return a[::-1][b[::-1].index(max(b))]


print(longest_word_in_file('444.txt'))

print('\nЗадача 3.2')


def longest_word_in_file(file_name):
    file = open(file_name, 'r', encoding='utf=8')
    m = ''
    for word in file.read().split():
        new_word = remove_punctuation(word)
        if len(new_word) >= len(m):
            m = new_word
    file.close()
    return m


def remove_punctuation(word):
    for i in punctuation:
        if i in word:
            word = word.replace(i, '')
    return word


# print(remove_punctuation('!<>hello,'))
print(longest_word_in_file('444.txt'))

print('\nЗадача 4.1')
file = open('numbers.txt')
accumulative = 0
count = 0
for row in file:
    if len(row) - 1 == 2:
        accumulative += int(row)
    if len(row) - 1 == 3:
        count += 1
file.close()
print(f'{count},{accumulative}')

print('\nЗадача 4.2')
with open('numbers.txt', 'r') as f:
    a = [int(i) for i in f.read().split() if 9 < int(i) < 1000]
count = len([i for i in a if 99 < i < 1000])
accumulative = sum([i for i in a if 9 < i < 100])
print(f'{count},{accumulative}')
