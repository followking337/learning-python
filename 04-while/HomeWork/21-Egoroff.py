print('\nEgoroff HomeWork')

print('\nЖизнь без нулей (1)')
a = 105
b = 106
# a = int(input())
# b = int(input())
c = a + b
strA = ''
strB = ''
strC = ''
while a > 0 or b > 0 or c > 0:
    lastA = a % 10
    lastB = b % 10
    lastC = c % 10
    if lastA != 0:
        strA += str(lastA)
    if lastB != 0:
        strB += str(lastB)
    if lastC != 0:
        strC += str(lastC)
    a = a // 10
    b = b // 10
    c = c // 10
a = int(strA[::-1])
b = int(strB[::-1])
c = int(strC[::-1])
# print(a)
# print(b)
# print(c)
print('YES' if c == a + b else 'NO')

print('\nЖизнь без нулей (2)')
a = 105
b = 106
# a = int(input())
# b = int(input())
a = str(a)
b = str(b)
c = str(a + b)
a = int(a.replace('0', ''))
b = int(b.replace('0', ''))
c = int(c.replace('0', ''))
# print(a)
# print(b)
# print(c)
print('YES' if c == a + b else 'NO')

print('\nЖизнь без нулей (3)')
a = 105
razryad = 1
new_number = 0
while a > 0:
    last = a % 10
    if last != 0:
        new_number = last * razryad + new_number
        razryad *= 10
    a //= 10
print(new_number)

a = 105
b = 106
# a = int(input())
# b = int(input())
c = a + b
numbers = [a, b, c]
i = 0
while i < 3:
    a = numbers[i]
    razryad = 1
    new_number = 0
    while a > 0:
        last = a % 10
        if last != 0:
            new_number = last * razryad + new_number
            razryad *= 10
        a //= 10
    numbers[i] = new_number
    i += 1
print(numbers)
print('YES' if numbers[0] + numbers[1] == numbers[2] else 'NO')

print('\nВыращиваем бактерии')
x = 536870911
# x = int(input())
i = 0
putted = 1
bacterias = putted
while x - bacterias >= bacterias:
    bacterias *= 2
    i += 1
    print(i, bacterias)
if x > bacterias:
    putted = x - bacterias
    bacterias += (x - bacterias)
print(putted)
print(bacterias)
print(536870911 % 2)
