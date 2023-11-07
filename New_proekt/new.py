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