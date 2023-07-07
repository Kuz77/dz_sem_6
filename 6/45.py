# Задача №45.

# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: Вывод:
# 300 220 284


            
    
# def sum_of_divisors(n):
#     # Функция для вычисления суммы делителей числа n
#     sum = 0
#     for i in range(1, n):
#         if n % i == 0:
#             sum += i
#     return sum
# k = int(input("Введите число k: "))
# friendly_numbers = []
# for i in range(1, k+1):
#     # Вычисляем сумму делителей числа i
#     sum_i = sum_of_divisors(i)
#     # Проверяем на дружественность
#     if sum_i > i and sum_of_divisors(sum_i) == i:
#         friendly_numbers.append((i, sum_i))
# # Выводим пары дружественных чисел
# for pair in friendly_numbers:
#     print(pair[0], pair[1])



k = int(input())

array = []



for i in range(k): 
    summ = 0
    for j in range(1, i):
        if i % j == 0:
            summ += j
    array.append([i,summ])
#print(array)
        
for i in range(1,len(array)):
    for j in range(i + 1,len(array)):
        b = array[i]
        c = array[j]
        if b[0] == c[1] and b[1] == c[0]:
            print(b)


