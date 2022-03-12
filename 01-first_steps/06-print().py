print('\nprint():')
print(1, 2, 3)
print(4, 5)
print(6)

print('\nsep=:')  # default: sep=' '
print(1, 2, 3, sep=',')
print(4, 5, sep='???')
print(6, sep='???')

print('\nend=:')  # default: end='\n'
print(1, 2, 3, sep=',', end=' ')
print(4, 5, sep='???', end=',')
print(6, sep='???')

print('\nConcatenation:')
eur = 10
cent = 99
print('I have', eur, 'EUR and', cent, 'cents')
print('I have %s EUR and %s cents' % (eur, cent))
print('I have ' + str(eur) + ' EUR and ' + str(cent) + ' cents')
print(f'I have {eur} EUR and {cent} cents')
