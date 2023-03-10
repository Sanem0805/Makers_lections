# цикл for
#№22
#lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# list = [[]]
# if len(lists) == 1:
#     print(f'max_list{lists[0]}')
#     print(f'min_list{None}')
# else:
# list_of_len = []
# for x in lists:
#     print(len(x))
#     list_of_len.append(len(x))

# min_value = (min(list_of_len))
# max_value = (max(list_of_len))
# if min_value == max_value:
#     max_index == list_of_len.index(max_value)
# min_index = list_of_len.index(min_value)
# max_index = list_of_len.index(max_value)
# print(f'max_lists{lists[min_index]}')
# print(f'min_lists{lists[max_index]}')


#№17 множества
# even_num = {i for i in range(10) if i % 2 == 0}
# odd_num = {i for i in range(10) if i % 2 == 1}
# set1 = set(even_num)
# set2 = set(odd_num)
# if even_num.intersection(odd_num):#sdisjoint
#     print('Множества пересекаются!')
# else:
#     print('Множества не пересекаются!')


#№15
# ingredients = {"cыр чеддар","грибы", "соус","шпинат"}
# ingredients.discard("колбаса")
# ingredients.remove("шпинат")
# ingredients.pop()
# ingredients.add( "сыр моцарелла")
# ingredients.add("помидор")
# ingredients.add("базилик")
# print(ingredients)


# tilek = {"Dodo", "ImperiaPizza","FreshBox"}
# timur = {"OchakKebab", "FreshBox"}
# alexander = {"FreshBox", "KFC"}
# elina = {"Dodo", "ImperiaPizza", "OchakKebab", "FreshBox","KFC"}
# print(tilek & timur & alexander & elina)




#№8 циклы while списки множества
# a = {4, 6, 100, -45, -6} 
# b = {4, 5, -5, -6}
# a.intersection_update(b)
# print(a)

# a = {0, 1, 2}
# b = {0, 1, 2, 3, 34, 5, 8, 13}
# if a.issubset(b):
#     print('Правильно!')


#№13 Множества 
# robert = {5, 7, 11, 10, 28} 
# kail = {1, 5, 14, 8, 22} 
# merri = {19, 20, 3, 11, 10}
# while robert.isdisjoint(kail) or robert.isdisjoint(merri):
#     print('no one')
# else:
#     print('kail merri')
# z = robert.intersection(kail,merri) 
# t = robert.intersection(merri) 
#№13 множества правильное решение
# robert = {5, 7, 11, 10, 28} 
# kail = {1, 5, 14, 8, 22} 
# merri = {19, 20, 3, 11, 10}
# is_kail_find = False
# is_marri_find = False
# for x in robert:
#     #print(x)
#     for kail_num in kail:
#         #print(kail_num)
#         if x == kail_num:
#             is_kail_find = True
#     for merri_num in merri:
#         if x == merri_num:
#             is_marri_find = True
# if is_marri_find and is_kail_find:
#     print('kail merri')
# elif is_kail_find:
#     print('kail')
# elif is_marri_find:
#     print('merri')
# else:
#     print('no one')
    
#Так можно напечатать чтобы посмотреть есть ли у них совпадения
# if is_kail_find:
#     print('Kail nashel chislo Roberta')
# else:
#     print('Kail nashel ')

# if is_marri_find:
#     print('Merri nashla chislo Roberta')
# else:
#     print('Merri ne nashla')


#№1 Списки
#name_of_friends = ['Alina', 'Zarina', ' Vika', 'Tanya', 'Jenya']
#19
#string = 'I love Python'
# string1 = string.startswith('Python')
# print(string1)

#№21
#a = int(input('Enter traingular length: '))
# b = int(input('Enter traingular length: '))
# c = int(input('Enter traingular length: '))

# if ((a*a) + (b*b)) == c*c or ((a*a) + (c*c)) == a*a or ((a*a) + (c*c)) == b*b or ((c*c) + (b*b)) == a*a:
#     print('rectangular')
# elif a + b > c or a + c > b or a + c > b or c + b > a:
#     print('acute')
# elif a + b < c or a + c < b or a + c < b or c + b < a:
#     print('obtuse')
# else:
#     print('impossible')



# №16
# a,b,c = input('Enter number:'), input('Enter number:'), input('Enter number:')
# if a > b:
#     a, b = b, a
# if a > c:
#     a, c = c, a
# if b > c:
#     b, c = c, b
#     print(a, b, c)
#
# count = 0
# number = (input('Enter the number:'))
# if number.isdigit():
#     count = int(number)

# №16
# a,b,c = input('Enter number:'), input('Enter number:'), input('Enter number:')
# if a > b:
#     a, b = b, a
# if a > c:
#     a, c = c, a
# if b > c:
#     b, c = c, b
#     print(a, b, c)
#
# count = 0
# number = (input('Enter the number:'))
# if number.isdigit():
#     count = int(number)
#11логические выражения
# В этом коде мы сначала преобразуем введенное число в символ, используя функцию chr(). Затем мы проверяем, является ли символ буквой, используя метод isalpha() для строки, которую возвращает функция chr(). Если символ является буквой, мы выводим сообщение "Это буква", в противном случае выводим сообщение "Это не буква, а символ", и используем функцию chr() еще раз, чтобы вывести соответствующий символ.

# num = int(input("Введите число: "))

# if chr(num).isalpha():
#     print(f"Это буква \"{chr(num)}\"")
# else:
#     print(f"Это не буква, а символ \"{chr(num)}\"")
#12 логические выражения
# greeting = input()
# if 'Hi' in greeting:
#     print("Привет!")
# else:
#     print("NO")
#№14
# lang = 'en'
# if 'en' in lang:
#     print('This is english')
# elif 'ru' in lang:
#     print('Это русский')
# elif 'de' in lang:
#     print('Das ist Deutsch')
# elif 'kg' in lang:
#     print('Бул кыргыз тили')
#21логические выражения
# a = float(input())
# b = float(input())
# c = float(input())

# if a >= b + c or b >= a + c or c >= a + b:
#     print("impossible")
# elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
#     print("rectangular")
# elif a**2 < b**2 + c**2 and b**2 < a**2 + c**2 and c**2 < a**2 + b**2:
#     print("acute")
# else:
#     print("obtuse")
# #     Input:
# # 3
# # 4
# # 5
# # Output:
# # rectangular

#23 логические выражения
# На уроке физкультуры тренер говорит «на первый-второй рассчитайтесь». Запросите у пользователя номер человека. Что он скажет, «первый» или «второй»?
# a=int(input('Количество учеников в классе: '))
# if a%2==0: 
#     print('второй')
# else:
#     print('первый')
#№8
# x = int(input('Enter number: '))
# y = int(input('Enter number2: '))
# if x % y == 0:
#      print('x не делится на y')
# else:
#     print('Частное: ', x//y)
#     print('Остаток: ', x%y)

# num = input('Enter code symbol: ')
# if num.isalpha():
#     print(num)


# №8 Логические выражения
# x = int(input('Enter number: '))
# y = int(input('Enter number: '))
# if -  дописать из фото

#23 числа 
# t = 255
# centner = t * 10
# kilogram = t * 1000
# gram = t * 1000000
# print(gram, kilogram, centner)

# Классные работы
# x = 5
# y = 2 
# z = 3
# x, y, z = y, z, x#x, y, z = 2, 3, 1


# name = 'John'
# last_name = 'Snow'
# adress = 'Bishkek'
# name, last_name, adress = adress = last_name, adress, name
# print(name, last_name, adress)

# salary = 2400
# period = 15
# kurs = 84
# result = salary * period * kurs
# print(result)


# negativ = -10
# print(abs(negativ))
# positive = negativ * -1
# print(positive)

# y = 20
# z = y ** 2 % 5
# print(z)
 
# import math
# from math sqrt

# decimal = 6.9
# result = decimal ** 2 
# res2 = decimal **3
# res3 = decimal ** 0.5
# res4 = decimal.sqrt(decimal)
# pritn(roud(result, 2)), round(res2,2), round(res3, 3), round(res4, 4)


# import math
# a = 3
# b = 4
# hyotinuse = a **2 + b ** 2
# print(math.sqrt(hyotinuse))
# print(hyotinuse**0.5)

# inp1 = int(input())
# inp2 = int(input())
# inp3 = int(input())
# print(inp1 * inp2 % inp3)


#№25
# inp1 = input()
# inp2 = int(input())
# res = inp1 * inp2
# print(res)

# list_ = ['sun', 'flowers', 'rumor', 'stranger', 'adventure', 'architect', 'accompany', 'abandon', 'cartoon']
# s = input()
# list1 = []
# for i in list_:
#     if i.startswith(s):
#         list.append()
# print(list1)


# #№35 Списки цикл for - нужно дописать из фотографии
# chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# merge_from = input()  # a
# merge_to = input()  # d
# first_index = chars.index(merge_from)  # 0
# second_index = chars.index(merge_to) + 1  # 4
# chars[first_index : second_index] = [''.join(chars[first_index : second_index])]
# # chars['a', 'b', 'c', 'd'] = 'abcd'
# print(chars)
# # chars[first_index : second_index]  =>  ['a', 'b', 'c', 'd']
# # [''.join(chars[a:b])]  => 'abcd'

#№3 Списки 
# name_of_list  = ['Helloworld!']
# list2 = list(name_of_list[0])
# length = len(list2) + 1
# part1 = list2[0:length//2]
# part2 = list2[length//2:]
# part2.extend(part1)
# print(part2)

#№4 списки
# list_ = ['world', 'hello']
# new_list = list(list_)
# new_list.reverse()
# print(new_list)

#№5
# suitcase = []
# suitcase.append('футболка')
# suitcase.append('шорты')
# suitcase.append('сланцы')
# suitcase.append('очки')
# suitcase.append('кепка')
# suitcase.pop()
# suitcase.insert(0,'крем')
# print(suitcase)

# str_list = ['abc', 'xyz', 'aba', '1221']
# for sov in str_list:
#     if sov[0] == sov[-1]:
#         index = list(str_list)
#         print(index)


# КАК МЕНЯТЬ КЛЮЧИ И ДОБАВЛЯТЬ ДРУГИЕ ЗНАЧЕНИЯ!!!!!!!!!!!!!!!!!!!!
# a = {'qww': 1, 'ass': 2}
# b = {}
# for k, v in list(a.items()):
#     b[v] = k


# b = a.keys()
# print(b)
# list(b)
# print(list(b)[0])
# print(a)
# print(b)


# a = {'qww': 1, 'ass': 2}
# b = {}
# for k,v in list(a.items()):
#     b[v]=k

# print(b)

# a = {'qww': 1, 'ass': 2, 'asdas':3, 'asaasa':4}
# b = {}
# for k,v in list(a.items()):
#     if v % 2 == 0:
#         b[v]='четные'
#     else:
#         b[v]='нечетные'
# print(b)



# a = 3
# b = 3
# M = []
# for i in range(a):
#     M.append([0]*b)
# print(M)

# list_1 = [5, 10, 15, 20, 25, 30]
# list_2 = [10, 20, 30, 40, 50, 60]

# difference_1 = set(list_1).difference(set(list_2))
# difference_2 = set(list_2).difference(set(list_1))

# list_difference = list(difference_1.union(difference_2))
# print(list_difference)


# [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
# #№23
# step = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# list1 = []
# list1 = [list_[i::step]for i in range(len(list_))] [:step]
# одно и тоже решение
# list1 = [list_[i::step]for i in range(len(list_))if i < step]
# print(list1)
# тоже самое только циклом
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# step = 3
# list1  = []
# for i in range(len(list_)):
#     if i < step:
#         list1.append(list_[i::step])
# print(list1)
'======================='

# colors1 = ["red", "orange", "green", "blue", "white"]
# colors2 = ["black", "yellow", "green", "blue"]
# list1 = list(set(colors1)- set(colors2))
# print(list1)

#№1 Словари
# a = {'x': 1, 'y': 2, 'z': 1}
# b = a.keys()
# print(list(b)[0])

#№3 Словари
# a = {'a': 1, 'b': 2, 'c': 1}
# b = {'f': 55}
# a.update({'f': 55})
# print(a)

#№8 словари
# a = {'a': 1, 'b': 2, 'c': 1}
# a.items()
# for x, y in a.items():
#     print(y)

# №9 Словари
# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# b = {}
# for x, v in a.items():
#     if v % 2 == 0:
#         b[x] = 2
#     else: 
#         b[x] = v
# print(b)
#
# 6) Дан словарь, значениями в котором являются другие словари. Замените внутренние словари их значениями.
# Например: my_dict = {'first': {'a': 1}, 'second': {'b': 2}} -> {'first': 1, 'second': 2}


# newlist = [выражение for каждый_элемент in старый_список if условие]  
# new_list = [item for item in range(33, 44)] print(new_list) 
#36 словари
# Создайте словарь с числовыми значениями. Например:
# a = {'a': 10, 'b': 9, 'c': 3}
# Необходимо перемножить все значения между собой и записать в переменную result. Ответ вывести в терминал: 270 

# a = {'a': 10, 'b': 9, 'c': 3}
# result = 1
# res = a.values()
# for i in res:
#     result = result*i
# print(result)
#37 словари
# Тип данных. Словари. Extra Task 2
# Экстра задание 2
# Напишите код, который создает словарь следующим образом, вам дана строка, например:
# string = "pythonist" 
# нужно создать новый словарь, ключами которого будут буквы строки, а значениями числа, соответствующие количеству повторений данной буквы в строке.
# dict_ = {"p":1, "y":1, "t":2, "h":1, "o":1, "n":1, "i":1, "s":1} 
# string = "pythonist"
# dict_={}
# for i in list(string):
#     dict_.setdefault(i, list(string).count(i))
# print(dict_)
#37 словари другое решение
# string = "pythonist" 
# list1 = list(string)
# dict_ = {}.fromkeys(list1, 0)
# for a in list1:
#     dict_[a] += 1
# print(dict_)
#37
# string = "pythonist"
# dict_ = {}
# for letter in string:
#     if letter in dict_:
#         dict_[letter] += 1
#     else:
#         dict_[letter] = 1
# print(dict_)

#№2comprehension list
# list_ = [item for item in range(1, 51) if item % 2 !=0]
# print(list_)

#№3comprehetion list
# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [x  for x in list_ if x % 2 == 0 and x > 0]
# print(int_list)

#№4comprehetion list
# list_ = [x ** 2 for x in range(1, 26)]
# print(list_)

#№5 comprehetion list
# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = [ int(x) for x in str_list]
# print(int_list)

 #№6 comprehention list
# Создайте список list_ из чисел от 1 до 10 (включительно), заменяя четные числа - квадратом числа(число умноженное само на себя), 
# нечетные добавьте без изменений.
# В результате должны получить:
# [1, 4, 3, 16, 5, 36, 7, 64, 9, 100] 
#№6
# list_ = [x * x if x % 2 == 0 else x for x in range(1, 11)]
# print((list_))

# №7 comprehention list
# list_ = [True if i % 2 == 0 else False for i in range(1,11)]
# print(list_)

#№8 comprehetion list
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list = []

# new_list = ['shorter' if len(i) <= 4 else  'longer' for i in list_name]
# print(new_list)

# # # ['shorter', 'shorter', 'longer', 'longer', 'shorter', 'longer', 'shorter', 'longer', 'longer', 'shorter'] 

# for i in len(list_name):
#     if i <= 4:
#         i = 'shorter'
# else:
#     'longer'
#     print(list_name)

#№9 comprehetion dict
#dict_ = {i: i * i for i in range(1,11)}
# print(dict_)

#№7Списки циклы for
# a = input('Enter numbers: ').split(',')
# list_ = a
# tuple_ = tuple(a)
# print(list_)
# print(tuple_)

#№8Списки  циклы for
# list_ = [1, 2, 3, 4, 5]
# new_list = []
# for i in list_:
#     i = str(i)
#     new_list.append(i)
# print(new_list)

#№9Списки и циклы
# list_ = [1, 2, 3, 4, 5]
# new_list = []
# for i in list_:
#     if i % 2 == 0:
#         new_list.append('нечетное')
#     else:
#         new_list.append('четное')
# print(new_list)

#№10 Списки и цикры
# list_= list(range(20))
# print(list_)

#№11 Списки и циклы
# list_ = list(range(0,101,2))
# print(list_)

# list_a = [1, 2, 3, 4]
# list_b = [5, 6, 7, 8]
# for i in list_b:
#     list_a.append(i)
# print(list_a)

#№12 Списки и циклы
# list1 = [11, 23, 45, 7, 9] 
# list2 = [21, 4, 16, 8, 10] 
# for i in list2:
#     list1.append(i)
#     b = sum(list1)
# print(b)


# list_a = [1, 2, 3, 4]
# list_b = [5, 6, 7, 8]
# for i in list_b:
#     list_a.append(i)
# print(list_a)


# №13 списки неправильно решила
# num = input('enter num: ').split(',')
# list_ = []
# for i in num:
#     list_.append(i)
#     list_.sort()
# print(list_)
# list_ = [i for i in input('ent num: ').split(',')]
# print(list_)
# list_ = list(map(str, input('ent num: ').split(',')))
# print(sorted(list_))
#14 списки 
# list_ = [1,1,3]
# set_ = set(list_)
# if len(set_) != len(list_):
#     print('yes')
# else: print('ERROR')

#№15 списки циклы
# list_ = []
# for x in range(54,9185):
#     if x % 5 == 0:
#         list_.append(x)
# print(list_)

# lst = [1, 0, 3, 6, -5, 7]
# mins = lst[0]
# for i in range(len(lst)):
#     if mins >= lst[i]:
#         mins = lst[i]
# print(mins)

#№16 списки и циклы
# list_ = [20, 10, 20, 1, 100]
# min_num = list_[0]
# for i in range(len(list_)):
#     if min_num >= list_[i]:
#        min_num = list_[i]
# print(min_num)

#№17 списки 
# это платформа не приняла
# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# tup1 = []
# for i in tuples:
#     if i:
#        tup1.append(i)
# print(tup1)
# это система приняла
# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# cleared_tuples = [c for c in tuples if c]
# print(cleared_tuples)
# это тоже приняла
# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# cleared_tuples = list(filter(None, tuples))
# print(cleared_tuples)

#18
# inp1 = input()
# inp2 = input()
# inp3 = input()
# inp4 = input()
# inp5 = input()
# list0 = []
# list0.append(inp1)
# list0.append(inp2)
# list0.append(inp3)
# list0.append(inp4)
# list0.append(inp5)
# list1 = []
# target = ' '
# for i in list0:
#     t = i.find(target)
#     r = i.rfind(target)
#     if i.count(target) > 1:
#         list1.append(i[r+1:])
#     else: 
#         list1.append(i[t+1:])
# print(sorted(list1))

#№26 Списки платформа не принимает
# colors1 = ["red", "orange", "green", "blue", "white"]
# colors2 = ["black", "yellow", "green", "blue"]
# diff1 = list(set(colors1).difference(set(colors2)))
# diff2 = list(set(colors2).difference(set(colors1)))
# print(diff1)
# print(diff2)

# colors1 = ["red", "orange", "green", "blue", "white"]
# colors2 = ["black", "yellow", "green", "blue"]
# resc1=[]
# resc2=[]
# for i in colors1:
#     if not i in colors2:
#         resc1.append(i)
# for k in colors2:
#     if not k in colors1:
#         resc2.append(k)
# print(resc1,resc2)

#№19 списки циклы
# list_ = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# number = 8
# s = list_.count(number)
# print(s)

#№20 списки и циклы 
# list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]
# list2 = []
# list3 = []
# res = 0
# for x in list_:
#     if type(x) != int:
#         list2.append(x)
# for i in list2:
#     if i.isnumeric():
#         list3.append(int(i))
# for y in list_:
#     if type(y) == int:
#         list3.append(y)
# for j in list3:
#     if type(j) == int:
#         res += j
# print(res)

#№24 списки цикл
# size = 3
# m = []
# m1 = []
# for i in range(1,size+1):
#     m.append(i)
#     m1.append(m)
# print(m1)

# size = 3
# m = []
# for i in range(size):
#     m.inser(i,list(range(1, size+1)))
# print(m)


# [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
#№23 списки циклы платформа не принимает
# step = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# list1 = []
# list1.append(list_[::step])
# list1.append(list_[1::step])
# list1.append(list_[2::step])
# print(list1)

#№34 списки циклы
# list_ = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# repeated = [x for i, x in enumerate(list_) if i != list_.index(x)]
# print(repeated) 

#№33 списки и циклы не решила немогу  вывести список
# lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# maxim = 0
# for x in lists:
#     sum = 0
#     for i in x:
#         sum += i
#         print(sum)
#         maxim = max(sum, maxim)
# print()
#№27 списки есть еще решение перепиши из фоток
# list1 = [1,2,3,4,5]
# list2 = [5,6,7,8,9]
# if set(list1).intersection(set(list2)):
#     print(True)
# else:
#     print(False)
# №28
# list_ = [4, 6, 4, 3, 3, 8, 4, 3, 4, 3, 8, 8]
# repeats = 3
# res = []
# for i in list_:
#     if list_.count(i) >= repeats and i not in res:
#         res.append(i)
# print(res)
#
#29 Использование итертоолс
# from itertools import permutations
# list_ = [1, 2, 3]
# comb = permutations(list_)
# for i in comb:
#     print(i)

#№30 СПИСКИ циклы
# K = 3 
# a = [0] * K
# for i in range(K):
#     a[i] = [0] * K
# print(a)
#№30 списки циклы другая версия решения тоже правильная
# K = 3
# li = []
# for i in range(K):
#     print(i)
#     li.append([1]*K)
# print(li)

#№31 списки и циклы платформа не принемает
# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
# colors.sort(key=len)
# m = [i[::-1]for i in colors]
# b = ','.join(m).split(',')    
# print(b)

# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
# ls = []
# for i in colors:
#     ls.append(i[::-1])
# ls = sorted(ls,key=len)
# print(ls)

#№32 списки и циклы 
# переписать с фотки
# list_ = [1,2,3,4,5,6,7,8,9,0]
# step = 2
# i = step
# element = 'A'
# while i < len(list_) + 1:
#     list_.insert(i, element)
#     i += step + 1
# print(list_)
# oба решения правильные!!

# list_ = [1,2,3,4,5,6,7,8,9,0]
# step = 2
# element = 'A'
# stepsdone = 1
# res1 = []
# for i in list_:
#     helper = list_.index(i) + 1
#     if helper % step == 0:
#         res1.append(i)
#         res1.append(element)
#     else:
#         res1.append(i)
# print(res1)

#33 cписки
# lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# max_ = max([x for x in lists], key = sum)
# print(max_)

#№10 словари 
# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# for k, v in list(a.items()):
#     if a[k] == None:
#         a.pop(k, None)
# print(a)
#  представление словарей c низу пример такого же кода но сциклом
# d = {i: i**2 for i in range(5)}#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# цикл for
# d = {}
# for i in range(5):
#     d[i] = i**2
# print(d)#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#№11 словари
# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 
# for i, j in list(a.items()):
#     a[i] = j / 5
# print(a)

#№12 словари
# a = {'apple': 2, 'orange': 5, 'banana': 10} 
# for i, j in list(a.items()):
#     if j % 2 == 0:
#         a.pop(i,j)
# print(a)

#№13 словари
# a = {'a': 1, 'b': 2, 'c': 3} 
# z = {}
# for k, v in list(a.items()):
#     z[v] = k
# print(z)
#14 словари

# a = {'a': 3, 'b': 2}
# res = sum(a.values())
# print(res)

#№15 словари 
# a1 = dict([('a','1'), ('c', '2')])
# c = [1,2,3]
# v = ['a','v', 'm']
# a2 = dict(zip(c, v))
# a3 = dict.fromkeys(['a', 'b'])
# print(a1)
# print(a2)
# print(a3)

#№16 словари
# dict_ = {'x': 1, 'y': 2, 'z': 1}
# a = dict_.get('x')
# print(a)
#№17 словари

# dict_ = {'a': 1, 'b': 2, 'c': 1}
# del dict_['a']
# print(dict_)
#№18 словари
# dict_ = {'a': 1, 'b': 2, 'c': 1}
# dict_items = dict_.items()
# print(dict_items)
#№19 словари
# dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# print(max(dict_.values()))
#№20 словари
# dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# print(min(dict_.values()))
#№21 словари
# dict1 = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6} 
# dict2 = {}
# for i, j in list(dict1.items()):
#     if j % 2 != 0:
#         dict1[i] = 1
#         dict2 = dict1
# print(dict2)

#№22словари
# dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# for x, y in list(dict_.items()):
#     if dict_[x] != None:
#         dict_.pop(x, None)
# print(dict_)

#№23словари
# dict1 = {25: 'apple', 26: 'orange', 27: 'banana'} 
# dict2 = {}
# for i, j in list(dict1.items()):
#     dict2[i * i] = j
# print(dict2)

#24 словари
# list_ = ['Bootcamp', 'Makers', 'coding', 'hello']
# dict_ = {i: len(i) for i in list_}
# print(dict_)

#26словари
# dict1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
# dict2 = {k: v ** 3 for k, v in dict1.items()}
# print(dict2)

# #27словари
# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# for k,v in list(dict_.items()):
#     for v2 in v.values():
#         dict_[k] = v2
# print(dict_)
# # comprehension  не получилось
# dict_ = {k: v for v2 in v.values() for k,v in list(dict_.items())}
# print(dict_)

#28словари
# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}
# for k,v in list(dict1.items()):
#     res = 1
#     for j in v.values():
#        res = res * j
#        dict2[k] = res
# print(dict2)
'СПРОСИ КАК СДЕСЬ СДЕЛАТЬ COMPREHENSION????????????????????29'
#29словари 
# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
# list2 = []
# list3 = []
# for i in list_:
#     if type(i) == str:
#         list2.append(i)
#     else:
#         list3.append(i)
# dict_ = dict(zip(list2,list3))
# print(dict_)

'===============LOOOOK=DO==================30,31'
#30словари 'YOU MUST DO BY YOURSELF'
# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_values = sorted(dict_.values())
# sorted_dict = {}
# for i in sorted_values:
#     for k in dict_.keys():
#         if dict_[k] == i:
#             sorted_dict[k] = dict_[k]
#             break
# print(sorted_dict)
#31 словари отсортировать по значению
# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = {}
# sorted_value = sorted(dict_.values(), reverse=True)
# for v in sorted_value:
#     for k in dict_.keys():
#         if dict_[k] == v:
#             sorted_dict[k] = dict_[k]
#             break
# print(sorted_dict)

#32словари
# dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key = input()
# if key in dict_:
#     print("Key is present in the dictionary")
# else:
#     print("Key is not present in the dictionary")

#33словари обединение словарей можно  исп. update(), **kwargs- распаковка и цикл for
#### for key,value in dict_three.items():-for  сначала делаем это с со вторым слов потом с третим
####   merged_dict[key] = value- for
# dict1 = {1:10, 2:20}
# dict2 = {3:30, 4:40}
# dict3 = {5:50, 6:60}
# dict4 = {**dict1, **dict2, **dict3}
# print(dict4)

#34словари
# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
# dict_ = dict(zip(list1, list2))
# print(dict_)
# другое решение 34 словари
# list1 = [1, 2, 3, 4, 5, 6, 7] list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
# dict_ = {}
# for i in range (len (list1)):
#     dict_[list1[i]] = list2[i]
# print(dict_)
'''решить еще раз сделав свой пример!!!!!! обязательно'''
#35 словари
# dict_ = {
#     'math': {
#         'sum': sum
#     },
#     'vars': {
#         'a': 5,
#         'b': 20,
#         'c': 50
#     }
# }
# dict_ = { 'math': { 'sum': sum }, 'vars': { 'a': 5, 'b': 20, 'c': 50 } }
# res = dict_.get('vars')
# for k,v in dict_.items():
#     for j in v.values():
#         if type(j) != int:
#          print(j(res.values()))

#36 словари
# a = {'a': 10, 'b': 9, 'c': 3}
# result = 1
# for v in a.values():
#     result *= v
# print(result)

#37 словари
# string = "pythonist"
# dict_ = {string.fromkeys}


#№10 comprehension 
# n = int(input())
# dict_ = {i: i ** 2 for i in range(n, 501) if  i % n  == 0}
# print(dict_)
#№11 comprehension
# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_= {i: list(range(1,j+1)) for i, j in a.items()}
# print(dict_)

#№12 comprehention
# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# a = {x: 'odd' if y % 2 != 0 else 'even' for x, y in dict_.items()}
# print(a)

# word_list = s.split()
# num_list = []
 
# for word in word_list:
#     if word.isnumeric():
#         num_list.append(int(word))
 
# print(num_list)


#№13 comprehention
# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# a = [int(i) for i in filter(lambda x: x.isnumeric(),string_.split())]
# list_ = list(map(str,a))
# print(list_)

# ls = [[1,2,3], [4,5,6], [7,8,9]]
# # #ls = [1,12,9,14,25,16....]
# result = [x + 10 if x % 2 == 0 else x ** 2 for inner in ls for x in inner]
# print(result)

#  {'Timur': 'math', 'Olga': 'math', 'Nik': 'literature'}
#№14 comprehention
# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
# 'Nik': {'history': 84, 'math': 85, 'literature': 87}}
# for n in dict_:
#     for x, y in dict_.items():
#         maks = max(dict_.values())
#         print(maks)

#15 compr
# dict_ = {k:y for k,v in my_dict.items() for x,y in v.items()} 
# print(dict_)
#16 compr
# list_ = [x for x in range(1,25) if x % 2 == 0]
# print(list_)


#№17 сcompr
# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [x if x >= 0 else 1 for x in list_]
# print(int_list)

#№18 compr
# list1 = [1, 2, 'hello', 3, 'world', 4, 5, 'book', 'code', 6, 'Makers', 7, 8, 9, 10] 
# list2 = [x for x in list1 if type(x) == str]
# print(list2)
 
#№19 compr
# list_ = [0, 3, 9, 7, 5, 2, 18, 4]
# list1 = [x for x in list_ if x > 5]
# print(list1)
#№20 compr
# list_ = [False, True, False, True, False, True, False, True, False, True] 
# list1 = [1 if x == True else 0 for x in list_]
# print(list1)

#№21 compr
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
# new_list = [len(i) for i in list_name]
# print(new_list)

#№22 compr
# a = [i for i in range(1, 1000, 125) if i % 2 == 0]
# print(a)

#№23 compr
# list1 = [44,54,64,74,104]
# list2 = [i + 6 for i in list1]
# print(list2)

#№24 compr
# list1 = [2, 4, 6, 8, 10, 12, 14]
# list2 = [i for i in list1 if i ** 2  > 50]
# print(list2)

#№25 compr
# string = "happy birthday!"
# list_ = [ x for x in string if x != ' ' and x != '!']
# print(list_)

# №26 compr
# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
# dict1 = [y for k,v in dict_.items() for x,y in v.items()]
# print(dict1)

#№27 compr
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# dict1 = {i: len(i) ** 2 for i in list_name if len(i)>4}
# print(dict1)

#№28 compr
# dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# ls = [k.upper() for k,v in dict_.items() if 200 < v < 5000]
# print(ls)

#№29 compr
# dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110} 
# dict2 = {k.replace('i',''):k.count('i') for k,v in dict1.items()}
# print(dict2)

#№31 compr
# SPL_Patrons = [ ['Kim Tremblay', 134], ['Emily Wilson', 42], ['Jessica Smith', 215], ['Alex Roy', 151], ['Sarah Khan', 105], ['Samuel Lee', 220], ['William Brown', 24], ['Ayesha Qureshi', 199], ['David Martin', 56], ['Ajeet Patel',69] ] 
# readers = [x[0] for x in SPL_Patrons if x[1] > 100] 
# print(readers)

#№30 compr
# list1 = [1, 2, 3, 0, None, 'a', 'abc', [], 23, [1, 2, 3, 4], '', {'a': 1, 'b': 2}, 'drf', []]
# list2 = [i for i in list1 if i]
# print(list2)

#№32 compr
# SPL_Patrons = [ ['Kim Tremblay', 134], ['Emily Wilson', 42], ['Jessica Smith', 215], ['Alex Roy', 151], ['Sarah Khan', 105], ['Samuel Lee', 220], ['William Brown', 24], ['Ayesha Qureshi', 199], ['David Martin', 56], ['Ajeet Patel',69] ] 
# dol = 11.95
# saved_amount =  [round(float(i[1]) * 11.95, 2)for i in SPL_Patrons]
# print(saved_amount)

#№33 compr
# prairie_pirates = [
# ['Tractor Jack', 1000, True],
# ['Plowshare Pete', 950, False],
# ['Prairie Lily', 245, True],
# ['Red River Rosie', 350, True],
# ['Mad Athabasca McArthur', 842, False],
# ['Assiniboine Sally', 620, True],
# ['Thresher Tom', 150, True],
# ['Cranky Canola Carl', 499, False]
# ]
# mid_pr = 42
# p = [[x[0], x[1] * mid_pr] for x in prairie_pirates if x[2] == True]
# print(p)

#36
# list_ = [i / 2 for i in range(0, 11)if i % 2 == 0]
# print(list_)

#34
# dict_ = {'Timur':
#  {'history': 90, 'math': 95, 'literature': 91}, 
#  'Olga':
#   {'history': 92, 'math': 96, 'literature': 81}, 
#   'Nik': 
#   {'history': 84, 'math': 85, 'literature': 87}} 
# new_dict={x:max(y,key=lambda x:y.get(x)) for x,y in dict_.items()}
# print(new_dict)

#35
# dict_ = {
#     'Dasha': {
#         'likes': 15,
#         'comments': [
    #         {'id': 1, 'text': 'some text'},
    #         {'id': 2, 'text': 'some text'},
    #     ],
    #     'rating': 2
    # },
    # 'Luna': {
    #     'likes': 12,
    #     'comments': [
    #         {'id': 1, 'text': 'some text'},
    #         {'id': 2, 'text': 'some text'},
    #         {'id': 3, 'text': 'some text'},
    #     ],
    #     'rating': 1
    # },
    # 'Rena': {
#         'likes': 26,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#             {'id': 4, 'text': 'some text'},
#             {'id': 5, 'text': 'some text'},
#             {'id': 6, 'text': 'some text'},
#         ],
#         'rating': 2
#     }
# }
# list_ = [v2['id']for v in dict_.values() for v2 in v['comments'] if len(v['comments']) > 3]
# print(list_)
# другое решение
# list_ =[]
# for v in dict_.values():
#     for v2 in v['comments']:
#         if len(v['comments']) > 3:
#             list_.append('id')
# print(list_)

#37
# dict_ = {1:'asdd', 2:'hhjjjk', 3:'jshgd'}
# dict_ = {k:len(v) if k % 2 == 0 else len(v) ** 3 for k,v in dict_.items()}
# print(dict_)

#38 надо самой решить
# set1 = {x for x in range(10)}
# set2 = {a for a in range(8,18)}
# full_set = set1.union(set2)
# if len(full_set) < 20:
#     print(f'В этом сете было {20-len(full_set)} повторения, его длина составляет {len(full_set)}')
# elif len(full_set) == 20:
#     print("Ваш объединенный сет полностью уникальный!")

# 13 логические выр
# count = 0
# number = input()
# if number.isdigit():
#     number = int(number)
#     count = number
# print(count)

#15 логические вырвжения
# string = '123456'
# if int(string[0]) + int(string[1]) + int(string[2]) == int(string[3]) + int(string[4]) + int(string[5]):
#     print('да')
# else:
#     print('нет')

