print('\nStepik HomeWork')

print('\nЗадача 1')
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
print([j for i in vector for j in i])

print('\nСвоя Задача')
vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
print([[vector[i] for j in range(3)] for i in range(6)])
a = []
count = 0
for i in range(6):
    temp = []
    for j in range(3):
        temp.append(vector[count])
        count += 1
    a.append(temp)
print(a)
