print('\nprint():')
print(1, 2, 3)
print(4, 5)
print(6)

print('\nsep=:')  # по ум sep=' '
print(1, 2, 3, sep=',')
print(4, 5, sep='???')
print(6, sep='???')

print('\nend=:')  # по ум end='\n'
print(1, 2, 3, sep=',', end=' ')
print(4, 5, sep='???', end=',')
print(6, sep='???')

print('\nВарианты вывода print():')
rubles = 10
kop = 99
print('У меня в кармане', rubles, 'рублей и', kop, 'копеек.')
print('У меня в кармане %s рублей и %s копеек.' % (rubles, kop))
print('У меня в кармане ' + str(rubles) + ' рублей и ' + str(kop) + ' копеек.')
print(f'У меня в кармане {rubles} рублей и {kop} копеек.')
