# def func():
#     var = 15
#     return var * 2

# print(func())

# Область видимости и пространчтво имен или scopes оперделяет контекст переменной,
#  в рамках которого мы  можем ее использовать


# a = 5
# print(a)
# def func():
#     print(a)
# func()

# built-in (всторенная ) - print, len, max 
# global (глобальнная)
# enclosed (не локальная , nonlocal)
#local (локальнная)

# x = 200

# def func():
#     print(x, '!')

# func()

# a = 10 # global
# print #built - in
# def hello(): #global
#     a = 'hello world' # local
#     print(a, 'local inside at func')

# hello()
# print(a, 'global')

# LEGB 
# local -> enclosed -> global -> built-in


# x = 'global'
# print(x)

# def enclosed():
#     x = 'enclosed' #enclosed
#     def local():
#         x = 'local' # local
#         print(x)
#     print(x)
#     local()
#     print(x)

# enclosed()
# print(x)


# a = 10
# def func():
#     print(a)
#     a1 = 'local'
#     print(a1)

# func()

# i = 0
# def increment():
#     i = i + 1
# increment()

# global -> позваляет изменить значение глобальной переменной находясь в
#  локальнный или замкнутутой области видимости 

# nonlocal -> позволяет изменить значение не локальный переменной находясь 
# в локальный области видимости

# var = 100
# def icrement():
#     global var
#     var += 1
# print(var)
# icrement()
# icrement()
# icrement()
# icrement()
# icrement()
# print(var)

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1 
#         return num
#     return increment

# c = counter()
# print(c)#<function counter.<locals>.increment at 0x10005e3370>
# print(c())#1
# print(c())
# print(c())
# b = counter()
# print(c())
# print(b())
# print(b())
# print(c())

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1 
#         return num
#     return increment

# i = counter()
# for x in range(0, 100000):
#     if x % 3 == 0 and x % 5 == 0:
#         res = i()
#         print(res)

# print(f'Result: {res}')

# print(dir(__builtins__))
# print(len(dir(__builtins__)))


# #globals(), locals()
# print(globals())

# a = 5
# b = 6
# c = 7
# def func():
#     john = 'Snow'
#     print(locals())


# print(globals(), '\n')
# print()
# func()
#========================================================

