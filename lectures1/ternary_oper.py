# Обработка исключений 
# Оператор try except

# Ошибки -> 
# Исключения -> Invalid values
# ZeroDivisionError
# ArithmeticError
# NameError
# KeyError
# IndexError
# ValueError
# ImportError
# BaseException #прородитель всех иключений

# num = int(input('Enter number: '))
# print(type(num), num)

# try except

# try:
#     <body try>
# except<Exception>
#     <body>
# <else>:
#     <body>Только если все ок
# <finally>
#     <body> в любом случае в конце

# num = int(input('Enter number: '))
# print(num)
# print('Impotant!')

# try:
#     num = int(input('Enter number: '))
# except ValueError:
#     print('InvalidError')
# else:
#     print(num)
# finally:
#     print('Impotant!')

# try:
#     num1 = int(input('Enter first number: '))
#     num2 = int(input('Enter second number: '))
#     print(num1 / num2)
# except(ValueError, ZeroDivisionError) as error:
#     print('You enter wrong number!')
#     print(error)

# try:
#     num1 = int(input('Enter first number: '))
#     num2 = int(input('Enter second number: '))
#     print(num1 / num2)
# except Exception as error:
#     print('You enter wrong number!')
#     print(error)

# list_ = [1,2,3,4,5]
# try:
#     index = int(input('Enter your number: '))
#     res = list_(index)
#     print(res)
# except ValueError:
#     print('Value error!')
# except IndexError:
#     print('Index error!')

# try:
#     num1 = int(input('Enter first number: '))
#     num2 = int(input('Enter second number: '))
#     result = num1 / num2
# except ZeroDivisionError:
#     print('na 0 delit\' nel\'zya')
# except ValueError:
#     print('Invalid symbol for int()')
# else:
#     print(result)
# finally:
#     print('The End!')


# try:
#   age = int(input('enter your age: '))
#   if age == 0:
#     raise Exception('Ваш возраст должен быть больше 0')
# except ValueError:
#   print('Ваш возраст должен быть больше 0')