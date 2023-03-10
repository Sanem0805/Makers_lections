# i = 0
# while i < 10:
#     i += 1# i=i+1
#     print(f'цикл выполняеться {i} раз!')

# name1 = ''
# name2 = ''
# i = 0
# while name1.lower() != 'john' and name2.lower() != 'raychel':
#     name1 = input('Enter first name:')
#     name2 = input('Enter second name: ')
#     i += 1
#     if i >= 5:
#         print('цикл остановлен!')
#         break
# else:
#     print('vy vveli pravil\'noe imya')


# user = {'username': 'John', 'password': 'ilovepython123'}
# i = 3
# password = None
# while (password != user['password']):
#     if i == 0:
#         print('vu zablokirovanu na 5 dneu!')
#         break
#     i -= 1
#     password = input(f'{user["username"]} enter password\':')
# else:
#     print(f'{user["username"]} vy uspeshno zashli v sistemy!')

#=======================================================================
# for <variable> in <iterable object>:
#     <body>

# list_ = [0,1,2,3,4,5,6,7,8,9]
# i = iter(list_[::-1])
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# import random
# ls = []
# for x in range(1,101):
#     ls.append(random.randint(1,150))
# print(ls)
# ls = set(ls)
# ls = list(ls)
# ls.sort()
# res = []
# for x in ls:
#     if x % 2 != 0:
#         res.append(x)
# print(res)

# Проверка делителя
# x = 200
# res = []
# for i in range(1, int((x ** 0.5) + 1)):
#     if x % i == 0:
#         res.extend({i, x // i})
# res.sort()
# print(res)
