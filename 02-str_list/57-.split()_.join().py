print('\n.split():')  # str -> list
# Метод split разбивает строку с помощью указанного спецсимвола-разделителя и возвращает список подстрок.

s = 'Ivanov Ivan Ivanovich'
print(s.split())  # по умолчанию разделитель равен пробелу ' '.
print(s.split('I'))
n = '1,2,3,4,5'
print(n.split(','))
t = 'aaa'
print(t.split('a'))

print('\n.join():')  # list -> str
# Метод join возвращает строку, собранную из элементов указанного объекта, поддерживающего итерирование (состоящих из
# строк).

a = ['43', '54', '32', '65']
print('#'.join(a))
print('???'.join(a))
print(''.join(a))
b = [43, 54, 32, 65]
print('.'.join([str(i) for i in b]))
