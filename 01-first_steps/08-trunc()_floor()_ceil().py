import math

print('\ntrunc() отсекание:')
print(math.trunc(32))
print(math.trunc(32.3))
print(math.trunc(32.9999999999))
print(math.trunc(-32.9999999999))
print(int(89.43))
print(int(-89.43))

print('\nfloor() округление вниз:')
print(math.floor(32.1))
print(math.floor(32.999999999))
print(math.floor(-32.999999999))
print(math.floor(-3.2))

print('\nceil() округление вверх:')
print(math.ceil(4.5))
print(math.ceil(4.99999999))
print(math.ceil(4.00000001))
print(math.ceil(4))
print(math.ceil(-3.4))
print(math.ceil(-3.9999999))
print(math.ceil(-3))
