#  Функции высшнго порядка - это функция которая в качечтве аргумента принимает другую функцию 
# Декаратор это фукция которая позволяет без изменения кода обернуть другую функцию для того чтобы  расширить фукционал 
# обернутой фукции 

# def decorator(func):
#     print(f'Call Func name: {func.__name__}')#2
#     return func()#3:  call func #6 return Hello

# def hello():
#     print('Vsem privet!')
#     return 'Hello'# 5

# def john():
#     print('Hello my name is John Snow!')# vuzov #1
#     return 'John Snow'

# # hello()
# # john()
# decorator(hello)
# decorator(john)

# from typing import Callable

# def benchmark(func: Callable):
#     import time
#     start = time.time()
#     res = func()
#     finish = time. time()
#     print(f'время вызова фукции{func.__name__} заняло {finish - start}')
#     return res

# def loop():
#     i = 1
#     range_number = 100_000
#     while i < range_number:
#         i += 1
#         print(i)
#     return i
# print(benchmark(loop))


#Pythonic way -> @decorator 
#Стнтаксический сахар -> это крастоа кода
# from typing import Callable

# def bechmark(func: Callable):
#     def wrapper():#2
#         import time 
#         start = time.time()
#         res = func()#3
#         finish  = time.time()
#         print(f'время выполнения фукции{func.__name__}: заняло {finish - start}')
#         return res
#     return wrapper

# @bechmark
# def loop():#4
#     i = 0 
#     range_number = 1_000_000
#     while i < range_number:
#         i += 1
#         return i

# @bechmark
# def add():
#     i = 0
#     range_number = 1_000_000
#     ls = []
#     while i < range_number:
#         i += 1
#         ls.append(i)
#     return ls

# print(loop())#1
# add()

# def strong(func):
#     def wrapper(*args, **kwargs):
#         return '<strong>' + func() + '</strong>'
#     return wrapper

# def div(func):
#     def wrapper(*args, **kwargs):
#         return '<div>' + func() + '</div>'
#     return wrapper

# @div
# @strong
# @div 
# def john():
#     return 'John Snow'

# print(john())


# def trace(func):
#     def wrapper(*args, **kwargs):
#         print(f'Trace: вызвана {func.__name__}(),\n{args} {kwargs}')
#         original_result = func(*args, **kwargs)
#         print(f'Trace: вызвана {func.__name__}(),\nвернула{args} {kwargs}')
#         return original_result
#     return wrapper

# @trace   
# def say(name, line):
#     return f'{name}, {line}'

# say('John', 'Snow')

# def repeat(num): # аргументы декоратора
#     def wrapper(func):# функция
#         def wrapper2(name): #аргументы фукции
#             i = 0
#             while i < num:
#                 i += 1
#                 func(name)
#         return wrapper2
#     return wrapper

# @repeat(num=4)
# def function(name):
#     print(f'{name}')

# function('Python')
# warehouse = [['B', 's'], ['e', 'u'], ['O', 'o', 'x'], ['K', 'T'], [], [], [], [], [], []]
# for i in warehouse:
#     if len(warehouse)>10 or len(i)>3: 
#         raise ValueError()
