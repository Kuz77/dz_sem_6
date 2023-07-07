# Задача №25. 
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()



# s = input("Введите строку: ")
# words = s.split()
# word_count = {}
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
# result = []
# for word in words:
#     if word_count[word] > 1:
#         result.append(word + "_" + str(word_count[word]))
#         word_count[word] -= 1
#     else:
#         result.append(word)
# output = " ".join(result)
# print(output)


# text = 'a a a b c a a d c d d'
# a = text.split()
# b = []
# for i in range (len(a)):
#     if a[i] in b:
#         b.append(a[i] + '_' + str(a[:i].count(a[i])))
#     else:
#         b.append(a[i])
# print(*b)

# my_str = 'a a a b c a a d c d d'
# final_str = ''
# count = {}

# for i in my_str.split(' '):
#     if i in final_str:
#         final_str += f'{i}_{count[i]} '
#         count[i] += 1
#     else:
#         count[i] = 1
#         final_str += f'{i} '


#25Напишите программу, которая принимает на вход строку,

lst_1 = input().split()
result = {}
for i in lst_1:
    if i in result:
        result[i] += 1
        print(f"{i}_{result[i]}",end = " ")
    else:
        result[i] = 0
        print(i,end = " ")