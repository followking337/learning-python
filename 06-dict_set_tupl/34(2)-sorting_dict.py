print('\nSorting Dict:')

heroes = {
    'SpiderMan': 80,
    'Batman': 65,
    'Superman': 85,
    'Wonder Woman': 70,
    'Flash': 70,
    'Iron Man': 65,
    'Thor': 90,
    'Aquaman': 65,
    'Captain America': 65,
    'Hulk': 87
}
print('\nPrint Heroes:')
for i in heroes:
    print(i, heroes[i])

print('\nPrint Sorted Keys:')
for i in sorted(heroes):
    print(i, heroes[i])

print('\nPrint Sorted Values without Keys:')
for i in sorted(heroes.values()):
    print(i)

print('\nPrint Sorted Keys:')
for i in sorted(heroes.items()):
    print(*i)

print('\nPrint Sorted Values:')
for i in sorted(heroes.items(), key=lambda par: (par[1], par[0])):
    print(*i)

print('\nmax():')
print(*max(heroes.items(), key=lambda x: x[1]))
