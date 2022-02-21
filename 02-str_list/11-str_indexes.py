print('\nstr:')

print('\nИндексы:')
s = 'hello world'
print(s)
for i in range(len(s)):
    if 10 <= i <= 99:
        print(s[i].rjust(2, ' '), end=' ')
    else:
        print(s[i], end=' ')
print()
for i in range(len(s)):
    print(i, end=' ')
print()

print(s[6])
print(s[10])
print('abcd'[1])
# print(s[15])  error: out of range
d = 'privet'
print(d)
print(d[0])
print(d[5])
print(s[len(s) - 1])
print(s[-1])

print('\nСрезы:')
print(s[2:6])
print(s[2:7])
print(s[6:9])
print(s[4:])
print(s[:4])
print(s[:])
print(s[::2])
print(s[::1])
print(s[1::2])
print(s[::-1])
print(s[2:8:3])

print('\nИзменения значений в str:')
# s[1] = 'a' error: str object does not support item assignment
s = s[:4] + 'a' + s[5:]
print(s)
