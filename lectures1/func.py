'''FUNCTIONS'''
# Задача: найти квадрат, куб, результат деления на 100 определенных чисел. Должен получиться dictionary.
# 5
# 25 125 0.05
# {'2': 25, '3': 125, '100': 0.05}

# 28, 65, 1100, 54, 32
# num1 = 28
# num2 = 65
# num3 = 1100
# num4 = 54
# num5 = 32

# def operations(num):
#     print({'2' : num **2, '3' : num**3, '100' : num/100})

# operations(num1)
# operations(num2)
# operations(num3)
# operations(num4)
# operations(num5)

# dict1 = {'2': num1**2, '3': num1**3, '100': num1/100}
# dict2 = {'2': num2**2, '3': num2**3, '100': num2/100}
# dict3 = {'2': num3**2, '3': num3**3, '100': num3/100}
# dict4 = {'2': num4**2, '3': num4**3, '100': num4/100}
# dict5 = {'2': num5**2, '3': num5**3, '100': num5/100}
# print(dict1)
# print(dict2)
# print(dict3)
# print(dict4)
# print(dict5)

'''Функция - это именованная часть программы, которая содержит в себе определенный набор инструкций, и которая может вызываться в других частях программы столько раз, сколько угодно'''



# def name_of_function(<a, b> #параметры):
    # <body> #код/логика, которая возвращает конечный результат
    # <return> #оператор для возвращения результата

# namen_of_function(<5,6> #аргументы)

# Параметры функции - переменные, которые будут принимать данные, которые мы передаем в функцию
# Аргументы - данные, которые мы передаем в функцию в моменте, когда ее вызываем (с помощью () )
# return - оператор, который нужен для того, чтобы функция возвращала результат. Если не указать return, то функция возвращает None

# ls = [1,2,3,4,5,6,7]
# str1 = 'Hello world s vami Kani'

# def our_len(obj):
#     i = 0
#     print(obj)
#     for x in obj:
#         i += 1
#     print('result:', i)
#     return i

# print(our_len(ls))
# print(our_len(str1))




# res = print('123')
# print(res)




# res = max([1,2,3,4])
# print(res)




# def isEven(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# print(isEven(7))
# print(isEven(9))
# print(isEven(10))




# def isEven(obj: int) -> bool:
#     '''our function returns True or False while checking numbek for even number!'''
#     if obj % 2 == 0:
#         return True
#     return False

# print(isEven(8))



# ls = [1,2,3]
# print(ls.reverse())
# print(ls)



# def my_func(a,b,c):
#     pass

# my_func(1,2,3)



'''Полиндромы''' # слова, читающиеся одинаково в обеих сторон
# tenet, kazak, ded, anna

# from typing import List

# def get_polindrom(words: list[str]) -> list[str]:
#     '''Function return a polindrom list of strings!'''
#     result = []
#     for x in words:
#         if x.lower() == x[::-1].lower():
#             print(f'Polindrom find: {x}!')
#             result.append(x)
#     return result

# ls = ['kazak', 'ded', 'Anna', 'masha', 'tent', 'Tenet', 'John', 'apa']
# print(f'Result: {get_polindrom(ls)}')

'''Напишите функцию которая будет возвращать ваш депозит через определнное время с процентом 10%, возращать финальное количество денег. Мин период вложения 3 года. Мин ставка денек 30 000 сомов'''

# def deposit (money: float, period: int) -> float:
#     if period < 3:
#         raise ValueError('Минимальный срок 3 года')
#     elif money < 30_000:
#         raise ValueError('Минимальная сумма вложения 30 000 сом')
    
#     i = 0 
#     while i < period:
#         money += money * 0.1
#         i += 1
#     return money

# try:
#     money = float(input('Vvedite summu deneg: '))
#     period = int(input('Vvedite srok depozita: '))
# except ValueError:
#     print('Invalid values!')
# else:
#     print(deposit(money, period))