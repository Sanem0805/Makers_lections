# def printParms(a=None, b=None), c=None:
#     print(a, 'is stored in param a')
#     print(b, 'is stored in param a')
#     print(c, 'is stored in param a')
    

# printParams(a=5,c=10)

# def sum_of_args(a, b, c, d):
#     return a + b + c + d

# print(sum_of_args(5, 10, 15, 20))
# print(sum_of_args(a=5, c=15, d=20, b=10))
# print(sum_of_args(5, 10, d=20, c=15))

#=============================================
#оператор * # распаковывает 
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [*a, *b]
# print(c)

# *args **kwargs в функциях

# def printScores(student, *scores):
#     print(f'Student name: {student}')
#     # print(scores)
#     # print(type(scores))
#     # ls = list(scores)
#     for x in scores:
#         print('Score:', x)

# printScores('John Snow', 100, 99, 95, 90)

# def print_pet_names(owner, **pets):
#     print('Owner name: {owner}')
#     print(pets)
#     print(type(pets))
#     for pet, name in pets.items():
#         if type(name) == list:
#             print(f'{pet}:', {*name})
#         else:
#             print(f'{pet}: {name}')

# print_pet_names('John Snow', dog='Rex', cat='Garfild', fish=['Nemo','Dori', 'Alex'], turtle= 'Leonardo')

# def get_some_data(a, b, *args, **kwargs):
#     print('Параметры a и b:', a, b)
#     print('Аргументы:',args)
#     print('Именованые аргументы:', kwargs)
#     print(args[0])
#     print(args[-1])
#     print(kwargs['name'])

# get_some_data(1,2,3,4,5, lang='Python', name='John', car='BMV M8')
#======================================================
# def generate_random_string(len_):
#     import string as s
#     import random
#     random_str = ''.join(
#         random.choice(s.ascii_letters + s.digits)for i in range(0, len_))
#     return random_str

# print(generate_random_string(25))

#===========================================================
# def add(a, b): return a + b
# def subtract(a, b): return a - b
# def multiply(a, b): return a * b
# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return 'На ноль делать нельзя!'
# def calc(num1, num2):
#     operator = input('Введите опрератор(+,-,*,/):')
#     if operator == '+': return add(num1, num2)
#     elif operator == '-': return subtract(num1, num2)
#     elif operator == '*': return multiply(num1, num2)
#     elif operator == '/': return divide(num1, num2)
#     else: return 'Вы ввели неверный оператор!'

# def main():
#     try:
#         num1 = float(input('Введите первое число: '))
#         num2 = float(input('Введите второе число: '))
#     except ValueError:
#         print('Вы ввели не коректные данные')
#         main()
#         return

#     while True:
#         result = calc(num1, num2)
#         if type(result) == float:
#             print(f'Result: {result}')
#             break
#         else:
#             print(f'Result:{result}')

#     question = input('Хотите продолжить(Yes/No)?')
#     if question.lower() == 'yes':
#         main()
#     else:
#         print('Спасибо за использование нашего калькулятора!')

# if __name__ == '__main__':
#     main()
#1
# def add(a,b):
#     a + b
#     return a + b
# print(add(4,6))

#2
# def get_string_length(string1):
#     return len(string1)
# print(get_string_length('knyash'))

#3
# def get_type(a, b):
#     print(f'{type(a)}\n{type(b)}')
# get_type(5, 's')

#4
# def divide(x, y):
#     x / y
#     return x / y
# print(divide(5, 10))

#5
# dict_ = {1: 'adad', 2: 'efwf', 3:'sdfsf'}

# def dictionary(dict_):
#     for k in dict_.keys():
#         print(k)

# dictionary(dict_)

#6
# num = 6
# def check(num):
#     if num % 2 == 0:
#         return('It is even number')
#     else:
#         return('It is odd number')
# check(num)
#
#7
# def is_palindrome(word):
#     if word.lower() == word[::-1].lower():
#         return(True)
#     else:
#         return(False)
# print(is_palindrome('ded'))
# то же задание но другое решение
# def is_palindrome(str):
#     if str.upper() == str.upper()[::-1]:
#         return True
#     else:
#         return False
# print(is_palindrome("Mom"))

#8
# def max_num(a, b):
#     return max(a,b)
# print(max_num(10, 12))

#9
# def multiply_list(numbers):
#     res = 1
#     for i in numbers:
#         i = int(i)
#         res *= i
#     return res
# print(multiply_list([1, 2, 3, 4, 5, 6])) 

#10
# def sum_digits(b):
#     sum = 0
#     for digit in str(b):
#         sum += int(digit)
#     return sum
# print(sum_digits(105)) 
#  то же задание но другое решение
# def sum_digits(num):
#     return(sum([int(x) for x in str(num)]))
# print(sum_digits(105))

#11
# def func11(a, b, c):
#    res1 = 0
#    res2 = 0
#    try:
#     res1 = a + b
#     res2 = res1 / c
#     return res2
#    except ZeroDivisionError:
#     return res1
# func11(4, 5, 6)
#14
# def add_(a, b): return a + b
# def sub_(a, b): return a - b
# def mult_(a, b): return a * b
# def div_(a, b): return a / b
  
# def calc(num1, num2, operator = '+,-,*,/'):
#     if operator == '+': return add_(num1, num2)
#     elif operator == '-': return sub_(num1, num2)
#     elif operator == '*': return mult_(num1, num2)
#     elif operator == '/': return div_(num1, num2)
#     else: return 'Вы ввели неверный оператор!'

#15
users = [ 
    { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer'},
    { 'name': 'Helen', 'age': 35, 'work': 'Nurse'},
    { 'name': 'Bob', 'age': 35, 'work': 'Driver'},
    { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer'},
    { 'name': 'Helga', 'age': 35, 'work': 'IT-HR'} ]
def func(**kwargs):
    list1  = [i for i in users ]
    