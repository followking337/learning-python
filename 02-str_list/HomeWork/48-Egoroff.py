print('\nEgoroff HomeWork')

print('\nКвадраты в списке')
a = [i ** 2 for i in range(int(input()))]
for i in a:
    print(i)

print('\nСписок кубов')
print([int(i) ** 3 for i in input().split()])
