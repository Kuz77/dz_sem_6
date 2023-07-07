# Задача №39. 

# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)


import random

n = int(input("введи размер списка1: "))
list1 = []

for i in range(n):
    lis1 = random.randint(1, 10)
    list1.append(lis1)
print(list1)

set1 = set(list1) #множество
print(set1)


m = int(input("введи размер списка2: "))
list2 = []

for i in range(m):
    lis2 = random.randint(1, 10)
    list2.append(lis2)
print(list2)

set2 = set(list2) 
print(set2)

set3 = set1.difference(set2)
print(set3)

list3 = list1.difference()




lst1 = [random.randint(1,10) for i in range(10)]
lst2 = [random.randint(1,10) for j in range(5)]
print(lst1)
print(lst2)
ls3 = []
for i in lst1:
    if i not in lst2:
        ls3.append(i)
print(*ls3)
