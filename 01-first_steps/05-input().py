print('\n input() str:')
a = input()
print(a)
print(type(a))
print(a * 2)

print('\n input() int:')
c = int(input())
print(c)
print(type(c))
print(c * 2)

print('\nTriangle Perimeter:')
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение c: "))
perimeter = a + b + c
print(perimeter)

print('\nmap():')
a, b, c = map(int, input().split())
perimeter = a + b + c
print(perimeter)

print('\nПятью пять - двадцать пять!:')
a = int(input())
print(a ** 2)
