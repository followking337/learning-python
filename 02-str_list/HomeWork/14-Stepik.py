print('\nStepik HomeWork')

print('\nЗадача 1')
my_list = [-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781,
           759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791,
           631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933,
           -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278,
           867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472,
           -986, -964, -989, 29]
print(min(my_list), max(my_list))

print('\nЗадача 2')
a = [7, 8, 9, 777, 56, 777]
# a = list(map(int, input().split()))
print(777 in a)

print('\nЗадача 3')
a = [8, 11, 17]
# a = list(map(int, input().split()))
# a = [int(i) for i in input().split()]
print(sum(a))

print('\nЗадача 4')
a = [5, 1, 6, 5, 9]
# n = int(input())
# a = list(map(int, input().split()))
print(min(a), max(a))

print('\nЗадача 5')
a = [8, 10]
# a = list(map(int, input().split()))
print(sum(a) / len(a))

print('\nA и B и ошибки компиляции:')
a = [1, 5, 8, 123, 7]
b = [123, 7, 5, 1]
c = [5, 1, 7]
# n = int(input())
# a = [int(i) for i in input().split()]
# b = [int(i) for i in input().split()]
# c = [int(i) for i in input().split()]
print(sum(a) - sum(b))
print(sum(b) - sum(c))
