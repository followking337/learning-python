print('\nEgoroff HomeWork')

print('\nA. Куплю лопату (1)')
k, r = 15, 2
# k, r = map(int, input().split())
i = 1
last = k % 10
while last != r and last != 0:
    i += 1
    last = (i * k) % 10
    # print(i * k, last)
print(i)

print('\nA. Куплю лопату (2)')
k, r = 15, 2
# k, r = map(int, input().split())
i = 1
last = k % 10
while True:
    if last == r or last == 0:
        break
    i += 1
    last = (i * k) % 10
    # print(i * k, last)
print(i)
