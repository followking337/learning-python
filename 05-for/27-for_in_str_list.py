print('\nlist:')
a = [43, 65, 3, 54, 6]
count = 0
for i in a:
    print(i)
    count += 1
print(count, 'обход')
    # input()

print('\ni не меняется:')
a = [43, 65, 3, 54, 6]
for i in a:
    print(i)
    i += 5
print(a)

print('\ni меняется:')
a = [43, 65, 3, 54, 6]
for i in a:
    i += 5  # переменная i находится только в цыкле, это копия элемента из списка (i не может изменить оригинал)
    print(i)
print(a)

print('\n1. Обход по значениям:')
a = [43, 65, 43, 54, 6]  # в случае если элемент дублируется .index() выдает первое найденое
for i in a:
    print(a.index(i), i)
print(a)

print('\n2. Обход по индексам:')
a = [43, 65, 43, 54, 6]
for i in range(len(a)):
    print(i, a[i])
    a[i] += 5
print(a)

print('\nУдаляем дубли:')
a = [1, 2, 3, 4, 32, 4, 5, 3, 5]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(a)
print(b)

print('\nIndices de Par e Impar:')
a = [1, 2, 3, 4, 32, 4, 5, 3, 5]
par = []
impar = []
for i in range(len(a)):
    if a[i] % 2 == 0:
        par.append(i+1)
    else:
        impar.append(i+1)
print(par)
print(impar)

print('\nValores de Par e Impar:')
a = [1, 2, 3, 4, 32, 4, 5, 3, 5]
par = []
impar = []
for i in a:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(par)
print(impar)

print('\nstr:')
print('\nhello world')
s = 'hello world'
for i in s:
    print(i)

print('\nBig or small letters:')
s = 'helLo WOrld'
for i in s:
    if 'a' <= i <= 'z':
        print(i, 'small')
    elif 'A' <= i <= 'Z':
        print(i, 'big')
    else:
        print(i)

print('\nVowels:')
vowels = 'aeoui'
s = 'aertiooikjoaikl'
for i in range(len(s)-1):
    if s[i] in vowels and s[i+1] in vowels:
        print(s[i], s[i+1])
