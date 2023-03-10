#1
# def foo():
#     var = 'переменная foo'
#     print('переменная в foo: ', var)
  
#     def bar():
#         nonlocal var
#         var = 'переменная bar'
#         print('переменная в foo: ', var)
 
#     bar()
# foo()
#2
# x = 'Я глобальная переменная!'
# def my_func():
#     global x
#     print(x)
#     x = 'Я могу изменяться'
   

# my_func()
# print(x)
#
#3
# num = 3
# def mul():
#     global num
#     num = num ** 2
# mul()
# mul()
# mul()
# print(num)

#4
# balance = 0
# def get_salary(amount):
#     global balance
#     balance += amount

# def pay_bills(amount, log_name):
#     global balance
#     balance -= amount
#     print((f'Вы заплатили {amount} сом за {log_name}'))
#     return balance

# def get_balance():
#     global balance
#     print(f'У вас на счету {balance} сом')


# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()

#5
# result = 0
# def pow_first(x, y):
#     global result
#     result = pow(x, y)

# def pow_second(z):
#     global result
#     result = result % z

# pow_first(2, 3)
# pow_second(3)
# print(result)

#6
# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
# for k, v in a.items():
#     if v >= 17:
#         print(f'{k}, Вы можете войти в клуб')
#     else:
#         print(f'{k}, извините, Вы не проходите по age-control')

#7
# a = ['pipi', 'papa', 'mama']
# b = []
# for i in a:
#     b.append(i.capitalize())
# print(a)
# print(b)

# a = ['pipi', 'papa', 'mama']
# b = [ i.capitalize() for i in a]
# print(b)

#8
# def count_symbols(words):
#     glasnue = 0
#     soglasnue = 0
#     symbol = 0
#     for i in words:
#         if i.isalpha():
#             if i.lower() in 'яиюэёоаыуе':
#                 glasnue += 1
#             else:
#                 soglasnue += 1
#         else:
#             symbol += 1
#     return (f'Количество гласных: {glasnue}, согласных: {soglasnue}, остальных символов: {symbol}')
# print(count_symbols('Мурат супер!'))

#9
# a = []
# a = [i for i in range(0, 11)]
# print(a)

#10
# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]
# def lower_7():
#     lower_7 = [i for i in a if i < 7]
#     return lower_7
# print(lower_7())

# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]
# def lower_7():
#     b = []
#     global a
#     for i in a:
#         if i < 7:
#             b.append(i)
#         return b
# print(lower_7())

# 13 fun
# def func12(a1,n):
#     b = []
#     for i in a1:
#         if n == 'lower':
#             b.append(i.lower())
#         elif  n == 'upper':
#             b.append(i.upper())
#     return (b)
# func12(["hEllo", "wORld"], "lower")

# 14
# def add_(a, b, z): return a + b
# def sub_(a, b, z): return a - b
# def div_(a, b, z): return a / b
# def mult_(a, b, z): return a * b

#15
# users = [
#   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
#   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#   { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
# ]   
# def func15(users):
#     r=[]
#     for i in users:
#         if i['work'].startswith('IT'):
#             r.append(f"{i['name']}, скидки в магазине компьютерной техники!\n")
#             h=''.join(i for i in r)
#     return h
# print(func15(users))
#16
# def func16(km, petrol):
#     return f'На 100км было расходовано {round(100*petrol/km)}л горючего'
# print(func16(100,10 ))
#17
# employees = [
#   {'name': 'Jack', 'salary': 10000, 'overTime': 4},
#   {'name': 'Tom', 'salary': 15000, 'overTime': 3},
#   {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
#   {'name': 'Helen', 'salary': 25000, 'overTime': 2},
#   {'name': 'Peter', 'salary': 30000, 'overTime': 7}
# ]
# def func17(list_: list) -> list:
#     for i in list_:
#         i['salary'] += i['overTime']*200
#         i.popitem()
#     return list_
        
# print(func17(employees))
#18
# def func18(list1):
#     list2 = [i for i in list1 if type(i) == int]
#     list3 = [j for j in list1 if type(j) == str]
#     return list2, list3
# print(func18(['s', 'dv', 1, 3, 4]))
#19
# students = [
#   {'student': 'Jack', 'marks': 43},
#   {'student': 'Tom', 'marks': 92}, 
#   {'student': 'Helen', 'marks': 85}, 
#   {'student': 'Peter', 'marks': 58},
#   {'student': 'Jessica', 'marks': 78}
# ]
# def func19(list1):
#     for i in list1:
#         list1.sort(key=lambda i: i['marks'], reverse=True)
#         return list1
# print(func19(students))
#20
# products = [
#   {
#     'title': 'Samsung S10', 
#     'price': 800, 
#     'count': 6, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 13 Pro', 
#     'price': 1200, 
#     'count': 9, 
#     'category': 'apple'},
#   {
#     'title': 'Xiaomi Mi 10', 
#     'price': 500, 
#     'count': 2, 
#     'category': 'xiaomi'},
#   {
#     'title': 'Samsung S9', 
#     'price': 600, 
#     'count': 4, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 11', 
#     'price': 850, 
#     'count': 1, 
#     'category': 'apple'}
# ]
# def func20(list1, string1):
#     list2 = [i for i in list1 if string1.lower() in i['title'].lower()]
#     return list2
# print(func20(products, 'I'))
#22
# products = [
#   {
#     'title': 'Samsung S10', 
#     'price': 800, 
#     'count': 6, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 13 Pro', 
#     'price': 1200, 
#     'count': 9, 
#     'category': 'apple'},
#   {
#     'title': 'Xiaomi Mi 10', 
#     'price': 500, 
#     'count': 2, 
#     'category': 'xiaomi'},
#   {
#     'title': 'Samsung S9', 
#     'price': 600, 
#     'count': 4, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 11', 
#     'price': 850, 
#     'count': 1, 
#     'category': 'apple'}
# ] 
# def func21(list1: list, string1: str) -> list:
#     list2 = [ i for i in list1 if string1.lower() == i['category'].lower()]
#     return list2
# print(func21(products, 'samsung'))
#22
# balance = 334_000
# def spent(for_what_s, how_much, balance):
#     if balance > how_much:
#         balance -= how_much
#         return ({'target': for_what_s, 'spend': how_much}, balance)
#     else:
#         return ('Недостаточно средств')
# def deposit(summu, balance):
#     balance += summu
#     return balance
# print(spent('for_trip', 500, 7000))
#23
database = []
def create(database, title, price, category):
    dict_ = {'title': title, 'price': price, 'category': category}
    database.append(dict_)
def read(database):
    print(database)
def update(database, index, title, price, category):
    dict1 = {'title': title, 'price': price, 'category': category}
    database[index] = dict1
def delete(database, index):
    database.pop(index)
create(database, 'Тетрадь', 50, 'Канцтовары')
create(database, 'Карандаш', 10, 'Канцтовары')
create(database, 'Молоко', 80, 'Продукты')
create(database, 'Хлеб', 30, 'Продукты')
read(database)
update(database, 2, 'Кефир', 90, 'Продукты')
delete(database, 1)
read(database)
TaskFail: You failed extra tests Test case: create([{'title': 'Coffee', 'price': 50, 'category': 'Grocery'}, {'title': 'Prrrr', 'price': 233, 'category': 'PAPI'}], Prrrr, 233, PAPI) 
Expected: [{'title': 'Coffee', 'price': 50, 'category': 'Grocery'}, {'title': 'Prrrr', 'price': 233, 'category': 'PAPI'}] 
Received: {'title': 'Prrrr', 'price': 233, 'category': 'PAPI'}
# database = []
# def create(database, title, price, category):
#     item = {'title': title, 'price': price, 'category': category}
#     database.append(item)
#     return item

# def read(database):
#     return database

# def update(database, index, title, price, category):
#     if index >= len(database):
#         return None
#     item = {'title': title, 'price': price, 'category': category}
#     database[index] = item
#     return item

# def delete(database, index):
#     if index >= len(database):
#         return None
#     return database.pop(index)
# # Создаем объекты и добавляем их в базу данных
# create(database, 'Тетрадь', 50, 'Канцтовары')
# create(database, 'Карандаш', 10, 'Канцтовары')
# create(database, 'Молоко', 80, 'Продукты')
# create(database, 'Хлеб', 30, 'Продукты')

# # Выводим все объекты из базы данных
# print(read(database))

# # Обновляем объект с индексом 2
# update(database, 2, 'Кефир', 90, 'Продукты')

# # Удаляем объект с индексом 1
# delete(database, 1)

# # Выводим все объекты из базы данных после изменений
# print(read(database))
# [{'title': 'Тетрадь', 'price': 50, 'category': 'Канцтовары'}, {'title': 'Карандаш', 'price': 10, 'category': 'Канцтовары'}, {'title': 'Молоко', 'price': 80, 'category': 'Продукты'}, {'title': 'Хлеб', 'price': 30, 'category': 'Продукты'}]
# [{'title': 'Тетрадь', 'price': 50, 'category': 'Канцтовары'}, {'title': 'Кефир', 'price': 90, 'category': '
'''======================================================================'''
#Задача с долиной
# case 1
# path = 8
# teps = 'DDUUUUDD'
# # result = 1 dolina

# # case2
# path  = 10
# steps = 'DUDDDUUDUU'
# result = 2 dolina

# path = 'DDUUUUDD'
# steps = 8

# sea_level = 0
# valleys = 0
#   for i in path:
#         if  i == 'U':
#             sea_level += 1
#             if sea_level == 0:
#                 valleys += 1
#         elif i == 'D':
#             sea_level -= 1
#     return valleys
# print(f'Result:{valleys}count')


# try:
#   age = int(input('enter your age: '))
#   if age == 0:
#     raise Exception('Ваш возраст должен быть больше 0')
# except ValueError:
#   print('Ваш возраст должен быть больше 0')

#1
# try:
#     a = int(input())
#     b = int(input())
#     c = a + b
# except:
#     print('vvedite chislo')
# else:
#     print(c)
# finally:
#     print('Forever!')

#2
# try:
    # b = 10
    # c = 11
#     print(v)
# except:
#     print('Такой переменной не существует!')

#3
# try:
#     num1 = int(input())
#     num2 = int(input())
#     res = num1 / num2
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# else:
#     print(res)

#4
# try:
#     num1 = int(input())
#     num2 = int(input())
#     res = num1 + num2
# except:
#     print('Введите число!')
# else:
#     print(res)
#

#5
# try:
#     dict_ = {'key1': 'value1', 'key2': 'value2'}
#     for k, v in dict_:
#         if k in dict_:
#             raise Exception
# except:
#     print('Нет такого ключа!')

#6
# list_ = [1, 4, 9, 16, 25, 36] 
# try:
#     print(list_[2])
# except:
#     print('Нет такого элемента!')

#7
# try:
#     age = int(input())
#     if age < 18:
#         raise ValueError('Доступ запрещён')
# except:
#     print('Введён некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')
#
#8
# try:
#     num1 = int(input())
#     num2 = int(input())
#     res = num1 / num2
# except (ValueError, ZeroDivisionError):
#     print('Произошла ошибка!')
# else:
#     print(res)
#9
# try:
#     cash = int(input())
#     if cash < 0:
#         raise ValueError
# except:
#     print('Сумма не может быть отрицательной!')
# else:
#     print(cash)
#9 другая версия решения
# try:
#     cash = int(input())
#     if cash < 0:
#         raise Exception ('ValueError')
#         print(cash)
# except:
#     print('Сумма не может быть отрицательной!')
#10
# try:
#     list_ = [1, 2, 3]
#     print(list_.get(1))
# except AttributeError:
#     print(list_[1])

#11
# try:
#     string = 'sdgsg'
#     num = 9
#     sum = string + num
#     print(sum)
# except TypeError:
#     print('Unsupported option')

#12
# try:
#     for i in range(10):
#         list_.append(i)
# except NameError:
#     print([0,1,2,3,4,5,6,7,8,9])

#13
# try:
#     list_ = [1, 2, 3, 4]
#     for i in range(0, len(list_) + 1):
#         print(list_[i])
# except IndexError:
#     print(list_)

#14
# try:
#     password = 'short'
#     if len(password) < 6:
#         raise ValueError()
# except ValueError: raise ValueError 


#16 try
# def to_fahrenheit(k:int) -> float:
#     assert k>=0,'Холоднее абсолютного нуля!'
#     res=(k-273.15)*9/5+32
#     return res
#     print(to_fahrenheit(3))
# 17 try
# try:
#     import lamabimgo
# except ModuleNotFoundError:
#     print('Такого модуля нет')
#18
# def filter_comment(comment: str, banlist=[]) -> None:
#     # Убираем лишние символы и переводим в нижний регистр
#     comment = comment.lower().replace(",", "").replace(".", "").replace("!", "").replace("?", "")
#     # Разбиваем комментарий на отдельные слова
#     words = comment.split()
#     # Проверяем каждое слово
#     for word in words:
#         # Если слово в списке запрещенных, вызываем исключение
#         if word in banlist:
#             raise ValueError("Ваш комментарий отправлен на перепроверку, так как, возможно, содержит неблагоприятный контекст")
# filter_comment('Hello, world', ['hello'])
# filter_comment('HelloWorld', ['hello'])
# filter_comment('ochocientos ochenta y ocho') 
# filter_comment('I love this recipe', ['hate', 'unlike', 'liken\'t'])
# filter_comment('Dis? recipe. is i !!UNLike!?!! really much!', ['hate', 'unlike', 'liken\'t']) 
# Эта функция принимает комментарий в виде строки comment и список запрещенных слов banlist, и проверяет каждое слово в комментарии на наличие в списке запрещенных. Если слово есть в списке, вызывается исключение ValueError с соответствующим сообщением.
# Функция сначала приводит весь текст к нижнему регистру и убирает все знаки препинания. Затем она разбивает комментарий на отдельные слова и проверяет каждое слово на наличие в списке запрещенных слов. Если в комментарии есть запрещенное слово, функция вызывает исключение и заканчивает свою работу. Если запрещенных слов в комментарии нет, функция заканчивает работу без ошибок.
#19
# try:
#     num = 100_000_000 
#     for i in range(0, num):
#         print('Nope')
# except KeyboardInterrupt:
#     print('Nope')
#
#20
# try:
#     inp1 = input('enter1: ')
#     inp2 = input('enter2: ') 
#     print(int(inp1) + int(inp2))
# except:
#     print(inp1+inp2)

# except ZeroDivisionError:
#     print(list1)
# else:
#     print(list1)
# collect_all_possibles(list_ = [
#     'hello',
#     6, 
#     [1,2,3]
# ], num)

#1bild - in
# from functools import reduce
# list_ = [1, 2, 3, 4] 
# result = reduce(lambda a, b: a + b,list_)
# print(result)

#2
# list_ = [1, 5, -9, 6, -4] 
# result = all(int > 3 for int in list_)
# print(bool(result))

#3
# list_ = [5, 8, 4, 6, 7]
# result = any(int < 0 for int in list_)
# print(result)

#4
# list_ = [1, 2, 3, 4]
# result = list(map(lambda x: x ** 2, list_))
# print(result)

#5
# list_ = [1, 2, 3, 4]
# result = list(filter(lambda x: x % 2 == 0, list_))
# print(result)

#6
# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',]
# result = list(filter(lambda x: len(x) > 7, list_))
# print(result)

#7
# from functools import reduce
# list_ = [5, 6, 7, 8] 
# result = reduce(lambda x, y: x * y, list_)
# print(result)

#8
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 
# list2 = len(list(filter(lambda x: x % 2 == 0, list_)))
# list3 = len(list(filter(lambda x: x % 2 != 0, list_)))
# result = (f'even: {list2}, odd: {list3}')
# print(result)

#9
# list_ = [-1, 2, 3, 5, -3, 7]
# result = list(map(lambda x: True if x > 0 else False, list_))
# print(result)

#10
# from functools import reduce
# list_ = ['Paul', 'George', 'Ringo', 'John']
# result = reduce(lambda x, y: x if len(x) > len(y) else y, list_)
# print(result)
#11
# result = list(map(lambda x:'Fizz' if x % 3 == 0 else 'Buzz', range(1,50)))
# print(result)
#12
# list_ = [1, 2, 3, 4, 5]
# maxim = max(list_)
# print(maxim)
#13
# from functools import reduce
# list_ = [1, 2, 3, 4]
# minim = reduce(lambda x, y: x if not x > y else y, list_)
# print(minim)
#14
# string = 'hello'
# result = tuple(enumerate(string))
# print(result)
#15
# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# list_ = list(map(lambda x: abs(x), list_))
# print(list_)
#16
# list_ = ['hello', 123]
# result = list(map(lambda x: type(x), list_))
# print(result)
#17
# names = ['rauchel','john','peter','jessica','steven123','dandy34','kamest','potter']
# result = list(map(lambda x: f'{x} Python'if len(x)>5 else f'{x} JavaScript', names))
# print(result)
#

#18
# list_ = ['123hello@gmail.com', '123', 'hello']
# result = list(map(lambda x: x if '@gmail.com' in x else 'Not valid email', list_))
# print(result)

#19
# string = 'hello'
# result = tuple(enumerate(string, 1))
# print(result)

#20
# list1 = ['M', 'A', 'K', 'E', 'R', 'S'] 
# list2 = [236, 54, 33, 21, 89, 1]
# result = list(zip(list1, list2))
# print(result)

#21
# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# result1 = list(filter(lambda x: x>0, list_))
# result2 = list(filter(lambda x: not x>0, list_))
# result3 = list(zip(result1, result2))
# print(result3)

#22
# list_ = [0.334, 23.3443, 43.4, -13.44, 22.03, -11.033, 267.993, -3.24]
# list1 = list(map(lambda x: round(x ** 2, 3), list_))
# print(list1)
#
#23
# from functools import reduce
# list_ = ['a', 'n', 'n', 'a']
# res = reduce( lambda x, y: x + y, list_)
# print(res)
# if res == res[::-1]:
#     print('YES')
# else:
#     print('NO')

# word = ["cat", "rewire", "level", "book", "stats", "list"]
# palindromes = list(filter(lambda word: word == word[::-1], word))
# print(palindromes)

# d = {1: 'a', 2: 'b', 3: 'c'}
# d.update({'asd': 'dsa'})
# print(d)

# #1 работа с файлами
# with open('text1.txt', '')

