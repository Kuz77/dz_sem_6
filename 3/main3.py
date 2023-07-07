

# a = [i if i%2==0 else v for i in range(4) for v in range(4)]
# print(a)

# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6


# import random
# n = int(input("Введите размер списка: "))

# numbers = []

# for i in range(n):
#     number = random.randint(0, 11)
#     numbers.append(number)

# print(numbers)

# numbersset = set(numbers)
# print(numbersset)

# a = len(numbersset)
# print(F"уникальных элементов: {a}")

# numbers = [1, 1, 2, 0, -1, 3, 4, 4, 3, -3, 0, 10, 11, 11]
# unique = []
# for i in numbers:
#     if i not in unique:
#         unique.append(i)
# print(numbers)
# print(len(unique))


# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# numbers = [1, 2, 3, 4, 5]
# k = 2
# import random
# n = int(input("Введите размер списка: "))

# k = int(input("Введите на сколько сдвинуть список список: "))

# numbers = []

# for i in range(n):
#     number = random.randint(0, 11)
#     numbers.append(number)

# print(numbers)

                            
# for i in range(k):
#     numbers.insert(0, numbers[-1])
#     numbers.pop(-1)
# print(numbers)
        
# newnumbers = []
# for j in numbers:
#     if j - k > 0:
#         newnumbers.append(j-k)
#     else:
#         newnumbers.append(j-k+len(numbers))

# print(newnumbers)


# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

#
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#          {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
#
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
#
# Примечание: Список словарей задан изначально. Пользователь его не вводит

# numbers =  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#         {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

# my_set = set()
# for d in numbers:
#         for c in d.values():
#                 my_set.add(c)
#                 print(c)
# print(my_set)

# all_values = set().union(*(d.values() for d in numbers))
# print(all_values)



# list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#           {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

# set_n = set()

# for dct in list_1:
#    set_n.add(str(*dct.values()).strip())
   
# print(set_n)



# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)


# import random
# n = int(input("Введите размер списка: "))
# numbers = []
# for i in range(n):
#     number = random.randint(0, 11)
#     numbers.append(number)
# print(numbers)
# count = 0
# for i in range(len(numbers)-1):
#     if numbers[i] < numbers[i+1]:
#         count += 1
# print(F"количество элементов массива, больших предыдущего: {count}")



# # list,set,dct - изменяемые
# import time

# a = [i for i in range(15000000)]
# start = time.perf_counter()
# if 130000 in a:
#     print("нашел в списке")
# end = time.perf_counter()
# print(end-start)

# dct = {i:1 for i in range(15000000)}
# start = time.perf_counter()
# if 130000 in dct:
#     print("нашел в словаре")
# end = time.perf_counter()
# print(end-start)


# import time
# start = time.perf_counter()
#
#
# end = time.perf_counter()

# print(end-start)

# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

# n = int(input("Введите размер списка: "))
# X = int(input("введите Х: "))

# A = []

# for i in range(n):
#     number = i+1
#     A.append(number)

# print(A)
# count = 0
# for i in range(n):
#     if A[i]==X:
#         count +=1
# print(F"X встречатеся в списке А {count} раз")



# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

# import random
# n = int(input("Введите размер списка: "))
# X = int(input("введите Х который ищем: "))

# numbers = []

# for i in range (n):
#     number = random.randint(0, 100)
#     numbers.append(number)

# print(numbers)
# A = numbers[i]

# for i in numbers:
#     if (i - X)<(A-X):
#         A = i
# print(F"ближайшее число - [{A}]")        


# n = int(input())
# lst = [int(input()) for i in range(n)]
# x = int(input())
# min_range = abs(x-lst[0])
# el = lst[0]
# for i in lst:
#     if abs(x-i)<min_range:
#         min_range = abs(x-i)
#         el = i
# print(el)




# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. 

# В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.

# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод:
# ноутбук
# Вывод:
# 12
# import time

# string = input("Введите строку: ")
# count = 0

# start = time.perf_counter()
# for i in string:
#     if i.lower() == "а" or i.lower() == "в"or i.lower() == "е"or i.lower() == "и"or i.lower() == "н"or i.lower() == "о"or i.lower() == "р"or i.lower() == "с"or i.lower() == "т":
#         count += 1
#     if i.lower() == "д"or i.lower() == "к"or i.lower() == "л"or i.lower() == "м"or i.lower() == "п"or i.lower() == "у":
#         count += 2
#     if i.lower() == "б"or i.lower() == "г"or i.lower() == "ё"or i.lower() == "ь"or i.lower() == "я":
#         count += 3
#     if i.lower() == "й"or i.lower() == "ы":
#         count += 4
#     if i.lower() == "ж"or i.lower() == "з"or i.lower() == "х"or i.lower() == "ц"or i.lower() == "ч":
#         count += 5
#     if i.lower() == "ш"or i.lower() == "э"or i.lower() == "ю":
#         count += 8
#     if i.lower() == "ф"or i.lower() == "щ"or i.lower() == "ъ":
#         count += 10
# print(F"количество очков - [{count}]")
# end = time.perf_counter()

# print(end-start)



# string = input("Введите строку: ")
# count = 0

# start = time.perf_counter()
# points = {'а': 1, 'в': 1, 'е': 1, 'и': 1, 'н': 1, 'о': 1, 'р': 1, 'с': 1, 'т': 1,
#           'д': 2, 'к': 2, 'л': 2, 'м': 2, 'п': 2, 'у': 2,
#           'б': 3, 'г': 3, 'ё': 3, 'ь': 3, 'я': 3,
#           'й': 4, 'ы': 4,
#           'ж': 5, 'з': 5, 'х': 5, 'ц': 5, 'ч': 5,
#           'ш': 8, 'э': 8, 'ю': 8,
#           'ф': 10, 'щ': 10, 'ъ': 10}
# for i in string:
#     if i.lower() in points:
#         count += points[i.lower()]
# print(f"количество очков - [{count}]")

# end = time.perf_counter()

# print(end-start)

# import time
# start = time.perf_counter()
#
#
# end = time.perf_counter()

# print(end-start)

# a = 0.0001613000022189226
# b = 9.169999975711107e-05


# if a > b:
#     print(a)
# else:
#     print(b)

# c = b/a*100
# print(c)


points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JZ', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = input().upper()
count = 0
if word[0] in "QWERTYUIOPASDFGHJKLZXCVBNM":
    for sym in word:
        for key in points_en:
            if sym in points_en[key]:
                count += key
else:
    for sym in word:
        for key in points_ru:
            if sym in points_ru[key]:
                count += key
print(count)