# Вводится список целых чисел в одну строчку через пробел. 
# Необходимо оставить в нем только двузначные числа. 
# Реализовать программу с использованием функции 
# filter. Результат отобразить на экране в виде последовательности 
# оставшихся чисел в одну строчку через пробел.


# list1 = list(map(int, input().split())) 
# print(list1) 
 
# list2 = [] 
# for i in range(len(list1)): 
#     if 100 > list1[i] > 9: 
#         list2.append(list1[i]) 
# print(list2)



stringMsg = '-8 11 0 -23 140 1'
print(list(filter(lambda x: 9<(abs(int(x)))<100 , stringMsg.split())))


print(list(filter(lambda x: len(str(abs(int(x)))) == 2 , stringMsg.split())))