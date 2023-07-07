# Задача №43. 

# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3 2



import random
n = int(input("введи размер списка1: "))
list1 = []
for i in range(n):
    lis1 = random.randint(1, 10)
    list1.append(lis1)
print(list1)
count = 0
for i in range(len(list1)):
    for j in range(i+1, len(list1)):
        if list1[i] == list1[j]:
            count += 1
print(count)




lst = [1, 2, 3, 2, 3, 2, 1, 1]
count = 0
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]==lst[j]:
            count += 1
print(count)