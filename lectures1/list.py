'=========================================Типы данных - list(списки)============================================='

#list - это тип данных который представляет собой коллекцию какой-либо последовательности 

#list_ = [12, 23, True, False, [12, 'str'], 'str', None, [12,[]]]

#index y list

# list_ = [1, 2, 8, 10]
# print(list[2])#8
# print(list_[1::2])#[2, 10]

# list_ = [10, 5, 2, 10, [0, 0, 0, 1, 0]]
# print([list_[4][3]]) #1 лист в листе в первом указываем от первой скопки а во второй скопке указываем втой элемент маленького листа

# str = 'Helloworld'
# list_ = list(str)#list() - фукция
# print(list_)#['H', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']

#list_ = [1, 2, 3, 4, 5, 20, True, False, None, 'str']
# list_len = len(list_)# 10 len - фукция для подсчёта элементов
# print(list_len)# 10

'================================================Тип данных-Tuple(кортеж)======================================'
#tuple - не изменяемый тип данных являяюшихся последовательностью элементов, литералами являются запятые и круглые скобки

#tuple_ = (1, 2, 3, 4)#tuple - круглые скобки
# list_ = [1, 2, 3, 4]#list - квадратные скобки

# print(tuple_)
# print(list_)

'===============================================Range=========================================================='

#range(start, end, step) - это генератор последовательности 
#в новой версии питонв это тип даныых

# range_ = range(0, 11)
# print(list(range_))# [0, 1, 2, 4, 5, 6, 7, 8, 9, 10] list[]
# print(tuple(range_))#(0, 1, 2, 4, 5, 6, 7, 8, 9, 10) tuple()


'====================================================Цыклы(for, while)=================================================='

#for - Это цикл, который работает до концы итерируемый оъекта
#while - Это цикл, который работает пока условие True

# meshok = ['potato', 'tomato', 'onion']
# kastrula = []
# for ovoshi in meshok:
#     print(ovoshi)
#     kastrula.append(ovoshi)

# print(kastrula)

# for i in range(0,11): #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     print(i**2)# 0, 1, 4, 9, .....


# for i in 'makers bootcapmp':
#     print(f'Это буква -{i}')

# 'WHILE'
# i = 0
# while i <= 10:
#     print(f'hello world, это {i} итерация')
#     i+=1#инкремент i = i + 1

'BREAK, CONTINUE'
#break - это оператор циклов, который ломает цикл и выходит из него
#continue - это оператор циклов, который пропускает итерацию

'WHILE'
#i = 0
# while  True:
#     if i == 5:
#         break
#     print(f'hello world, это {i} итерация')
#     i+=1

# i = 0
# while i > 5:
#     i = i + 1
#     if i == 2:
#         continue
#     print(f'hello world, это {i} итерация')

'--------------------------------------------------------------------------------------------------------'

# for i  in range(11):
#    if i == 5:
#         break #ломает полностью цикл и заканчивает его когда i == 5
#    print(f'Это {i} итерация')

# for i in range(11):
#     if i == 5:
#         continue# пропускает итерацию когда i == 5  и продолжает работу цикла
#     print(f'Это {i} итерация')
   

'===========================================Методы list(список)==========================================='
#print(dir(list)) # dir(list )-  функция для просмотров метода листа

'APPEND()'
#list.append(element) - это метод листов который добавляет указанный элемент в конец листа


# list_ = []
# for i in range(1, 11, 2):
#     list_.append(i)

# print(list_)

'----------------------------------------------------------------------------------------------------'

# list_ = []
# for i in range(11):# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     if i %  2 == 0:
#         list_.append(True)
#     else:
#         list_.append(False)

# print(list_)#[True, False, True, False, True, False, True, False, True, False, True]


# list_ = [1, 2, 3, True, False, 'Rem']
# list_.append('Anton')
# print(list_)


'--------------------------------------------------------------------------------------------------------'

'EXTEND()'

#list_1.extend(list_2) - это метод листов который расширяет первый лист за счет второго листа


# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]

# list_1.append(list_2)#[1, 2, 3, [4, 5, 6]]
# print(len(list_1))

# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]

# list_1.extend(list_2)#[1, 2, 3, 4, 5, 6]
# print(len(list_1))

'------------------------------------------------------------------------------------------------------'

'INSERT()'

#list.insert(index, element) - это метод листов который на место Index добавляет element
# list_ = [0,0,0,0,0,0,0]

# list_.insert(5, True)
# print(list_)#[0, 0, 0, 0, 0, True, 0, 0]
 
'------------------------------------------------------------------------------------------------------'

# list_ = [25, 12, 1, 'makers', None, [1, 2, 3, 0, 5, 10]]

# list_[5].insert(5, True)

# print(list_)#[25, 12, 1, 'makers', None, [1, 2, 3, 0, 5, True, 10]]

'-------------------------------------------------------------------------------------------------------'

'INDEX'

#list.index(element, start, end) - это метод листов, который находит индекс указанного эломента

# list_ = ['NYC', 'Moscow', 'SP', 'Bishkek', 'Osh']

# for city in list_:
# #     print(f'Город - {city} под индексом {list_.index(city)}')#Город - Moscow под индексом 1
#                                                               Город - SP под индексом 2
#                                                               Город - Bishkek под индексом 3
#                                                               Город - Osh под индексом 4



'--------------------------------------------------------------------------------------------------'
'POP'

#list.pop()- это метод листов, который удаляет  и возвращает элемент по указанному 
# индексу, если индекс не указать он удалит последний элемент.  

# list_ = [1, 2, 3, 12, 123, 43, 12, 4, 5]

# pop_element = list_.pop(3)


# print(list_)
# print(pop_element)#[1, 2, 3, 123, 43, 12, 4, 5]
#                  # 12( удоляет элемент , insert()- возвращает элемент)

'-------------------------------------------------------------------------------'

# list_ = [1, 2, 3, 12, 123, 43, 12, 4, 5]

# pop_element = list_.pop(25)- индекс указываемб если не задавать то вернет последний элемент
# print(list_)
# print(pop_element)

'-------------------------------------------------------------------------------'

'REMOVE()'

#list.remove(element)- Это метод листов, для удаления какого либо элемента, если такого элемента нету выйдет ошибка

'-------------------------------------------------------------------------------------------------------'

# list_ = [1, 2, 3, 4, 5, 6, 7]

# list_.remove(6)#[1, 2, 3, 4, 5, 7] - прописываем элемент а не индекс
# print(list_)

#list_ = [1, 2, 3, 4, 5, 6, 7, 'Hello']


'----------------------------------------------------------------------------------------------------------'

'SORT()'

#list.sort(key=len, reverse) - Это метод листов , для сортировки его элементов

# list_ = ['Sultan', 'Sanjar', 'Aigerim', 'Erkaim']

# list_.sort(key=len, reverse=True)

# print(list_)
'-------------------------------------------------------------------------------------------------------------'

#list_ = [1, 2, 3, 7, 5, 6]

# list_.sort(reverse=True)

# print(list_)#[7, 6, 5, 3, 2, 1]

'------------------------------------------------------------------------------------------------------------'
'COUNT'
#list.count()- это метод листов который считает сколько element усть в листе 

# list_ = [1, 123, 31, 34, 'hello', '1', '1', 0]

# count_list = list_.count('1')# 2 раза встречаеться строка '1' в этом листе

# print(count_list)#2

'------------------------------------------------------------------------------------------------------------'
'COPY(), DEEPCOPY()'

#list.copy()- это метод листов который копирует лист поверхностно
#copy.deepcopy() - это метод листов который копирует лист углубленно


# list_ = [1, 2, 3, 4, 5, [1, 2, 3]]

# copy_list = list_.copy()
# list_[-1].append(0)

# print(list_)
# print(copy_list)
'------------------------------------------------------------------------------------------------------------'
#import copy 

# list_1 = [1, 2, 3, 4, 5,[1, 2, 3]]

# copy_list  = copy.deepcopy(list_1)

# list_1[-1].append(0)
 
# print(list_1)
# print(copy_list)

'---------------------------------------------------------------------------------------------------------'

'REVERSE'

#list.reverse() - это метод листов котрый переварачивает лист

# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list_.reverse()

# print(list_)
 
#print(dir(list)) - все методы посмотреть