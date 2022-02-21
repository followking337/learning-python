import smtplib
from string import ascii_uppercase

print('\nStepik HomeWork')

print('\nЗадача 1')
zeroes = [0 for i in range(100)]
print(zeroes)

print('\nЗадача 2')
# a = [i for i in range(1, int(input())+1)]
# print(a)
# print([*range(1, int(input())+1)])  # распаковка

print('\nЗадача 3')
# a = [i for i in ascii_uppercase[:int(input())]]
# print(a)

print('\nЗадача 4')
st = 'Create a list of the first letters of every word in this string'
print([i[0] for i in st.split()])

print('\nЗадача 5')
# a = [ascii_uppercase[i] * (i+1) for i in range(int(input()))]
# print(a)

print('\nЗадача 6')
a, b = list(map(int, input().split()))
print([i ** 2 for i in range(a, b+1)] if a <= b else [i ** 3 for i in range(b, a+1)][::-1])

print('\nЗадача 7')
# n = int(input())
# print([i for i in range(1, n + 1) if n % i == 0])

print('\nЗадача 8')
phrase = 'Take only the words that start with t in this sentence'
print([i for i in phrase.split() if i.lower().startswith('t')])
print([i for i in phrase.split() if i.startswith(('t', 'T'))])
print([i for i in phrase.split() if i[0] in 'tT'])
