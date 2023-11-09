# word_list = input('Введи слова через пробел: ').split()
# print(word_list)
# # temp = word_list[-1]
# # word_list[-1] = word_list[2]
# # print(word_list)
# # word_list[2] = temp
# # print(word_list)
# # print(' '.join(word_list))
# word_list[-1], word_list[2] = word_list[2], word_list[-1]
# print(word_list)
# print(' '.join(word_list))


# Generators spiskov
# new_list = [expression for item in sequence]

# new_list = [i * i for i in range(6)]
# print(new_list)
# list_1 = [i + '*' for i in 'example']
# print(list_1)
# list_2 = [i * 5 for i in 'abcdef']
# print(list_2)

# # new_list = [expression for item in sequence if condition]

# list_3 = [i * i for i in range(1, 11) if i % 2 == 0]
# print(list_3)

# customers = ['bob', 'anna', 'joe', 'bob', 'nick']
# list_4 = [i for i in customers if i.lower() != 'bob' and i.lower() !='joe'] #lower позволяет переместить в нижний регистр (грубо говоря проверка)
# print(list_4)

# list_5 = [x * y for x in range(1, 4) for y in range(1, 4)]
# print(list_5)

# list_6 = []
# for y in range(1, 4):
#     for x in range(1, 4):
#         list_6.append(x * y)
# print(list_6)

# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours, ':', minutes, ':', seconds)

# list_7 = [[x * y for x in range(1, 4)] for y in range(1, 4)]
# print(list_7)

# Rabota so spiskami
# my_list = ['user', 12, 200.34, False, True]
# print(my_list[0], my_list[-5])
# print(my_list[1])
# print(my_list[-1])
# print(my_list[len(my_list) - 1])
# print(my_list[-2])

# # srezi spiskov
# print(my_list[1:3])
# print(my_list[-4:-2]) #ot -4 do -2
# print(my_list[1:-1])
# print(my_list[:-1])
# print(my_list[3:])

# print(my_list[::2])
# print(my_list[::-1])
# print(my_list[-4::-1])


# category = ['Drama', 'Camedy', 'Fantasy']
# print(category)
# category[-1] = 'Action'
# print(category)

# user_logs = ['admin', 'student', 'teacher', 'HR', 'user']
# print(user_logs)
# user_logs[::2] = ['new_user_1', 'new_user_2', 'new_user_3']
# print(user_logs)

#function dla spiskov
# len(list) # возращает количество эелементов интерируемого обьекта
# max(list) # возращает максимальный элемент списка
# min(list) # возращает минимальный элемент списка
# sum(list) # возращает сумму значений списка
# sorted(list) #возращает копию списка list, в котором элементы упорядочены по возрастанию (если числа) и по алфовиту

# from random import randint
# new_list = [randint(1, 10) for i in range(10)]
# print(sorted(new_list, reverse=True)) #возращает 
# print(sorted(list('hello'), reverse=True))

# print(new_list)
# print(max(new_list))
# print(min(new_list))
# print(sum(new_list))
# print(sum(new_list) / len(new_list))

# category = ['Drama', 'Camedy']
# category_2 = ['Action', 'Fantasy']
# print(category + category_2)
# print(category * 3)

# methods spiskov
# category = ['Drama', 'Comedy', 'Mystery', 'Romance', 'Horror']
# for film in category:
#     print(film) #  если добавить end=' ' получится в одну строку

# for i in range(len(category)):
#     print(category[i], end=' ')

# # Методы добавления
# category.append('Fantasy') #добавляет новый элемент в свой аргумент в конец списка
# print(category)
# category.append([1, 2, 3]) #итерируемый обьект становится одним элементом списка
# print(category)
# category.extend([1, 2, 3, 4]) # добавляет каждый элемент фргумента-списка как отдельный элемент в целевой список
# print(category)

# category.insert(1, 'ABOBA') #добавляет элементна определенную строку
# print(category)

# методы удаления
# category = ['Drama', 'Comedy', 'Mystery', 'Romance', 'Horror']
# print(category)

# category.remove('Romance') # удаляет первое вхождение указанного значения в списке
# print(category)

# a = category.pop(1) #удаляет элемент списка по индексуи возращает значение удаленного элемента
# print(category)
# print(a)

# category.pop() #удаляет последний элемент списка
# print(category)

# category.clear() #удаляет все элементы из списка
# print(category)

# Другие полезные методы
# category = ['Drama', 'Comedy', 'Mystery', 'Romance', 'Horror']

# print(category.index('Romance')) #Возращает индекс первого вхождения значения в списке
# print(category.count('Romance')) # Возращает количество значений аргумента в списке
# category.sort() # сортирует список по возрастанию
# category.sort(reverse=True) # сортирует список по убыванию
# print(category)
# category.reverse() #меняет порядок сортировки элемента на обратный
# print(category)

# Оператор пренадлежности in
# customers = ['bob', 'anna', 'joe', 'bob', 'nick']
# print('bob' in customers)

# if 'bob' in customers:
#     print('bob is our customer')
# else:
#     print('Sorry')

# Псевдонимы и клонирование
# list_1 = [1, 2, 3, 4, 5]
# print(list_1)

# list_2 = list_1

# print(list_2)

# list_2[1] = 'Hello'

# print(list_1)
# print(list_2)

# list_3 = [6, 7, 8]

# print(list_2 is list_1)
# print(list_3 is list_1)

# Как создать новый список с теми же значениями
list_1 = [1, 2, 3, 4, 5]
print(list_1)

list_2 = list_1.copy() #копировать элементы списка в новый список
list_2[1] = 'Hello'
print(list_1)
print(list_2)

list_3 = list(list_1)
list_3[3] = 'Hello'
print(list_3)
print(list_1)

list_4 = list_1[:]
list_4[2] = 'Hello'
print(list_4)
print(list_1)
