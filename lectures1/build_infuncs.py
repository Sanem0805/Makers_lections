# dict_ ={'John': 50_000, 'Sultan': 5, 'Jamie': 1000000, 'aigerim': 1_000_000}
# res = dict(sorted(dict_.items(), key=lambda x: x[1], reverse=True))
# print(res)

#-------------------------
# map(function, iterable) - применяет функцию к каждоьу элементу из последовательности и возвращает
# mapobject(итератор) с результатом

# ls = ['one', 'two', 'three', 'four']
# for i in range(0, len(ls)):
#     ls[i] = ls[i].upper()
# print(ls)

# ls = ['one', 'two', 'three', 'four']
# res = list(map(str.upper, ls))
# print(res)

# names = ['John', 'Sultan', 'Jamie', 'Raychel']
# #['Hello mer/mrs John', 'Hello mer/mrs Sultan',...]
# res = list(map(lambda name: f'Hello mr/mrs {name}', names))
# print(res)

# dict_ = {1: 2, 3: 4, 5: 6}
#      #{1: '2', 3: '4', 5: '6'}

# for k in dict_:
#     dict_[k] = str(dict_[k])
# print(dict_)

# dict_ = {1: 2, 3: 4, 5: 6}
#      #{1: '2', 3: '4', 5: '6'}
# res = dict(map(lambda x: (x[0], str(x[1])), dict_.items()))

# filter(function, iterable) -> принимает ко всем элементам itereble функции которую мы и возвращаем
#  итератор

# ls = ['one', 'two', 'list', '100', '1', 'john']
# res = []
# for x in ls:
#     if x.isdigit():
#         res.append(x)
# print(res)

# res = list(filter(str.isdigit, res))
# print(res)

# ls = ['john', 'makers', 'ono', 'py.26', 'Kyrgizistan', 'sea']
# res = list(filter(lambda stroka: len(stroka) > 5, ls))
# print(res)

# ls = [
#     {'name': 'Python', 'point': 10},
#     {'name': 'C++', 'point': 6},
#     {'name': 'JS', 'point': 8},
#     {'name': 'JAVA', 'point': 3},
#     {'name': 'C#', 'point': 0}
# ]
# res = list(filter(lambda dict_: dict_['point'] >= 7, ls))
# print(res)

# users = [
#     {'username':'John', 'comments':['I love you', 'Really good']},
#     {'username':'Raychel', 'comments':[]},
#     {'username':'Steven', 'comments':['Bishkek', 'Python']},
#     {'username':'Hello', 'comments':[]},
#     {'username':'Kira', 'comments':['The best post']}
# ]
# inactive_users = list(filter(lambda dict_obj: dict_obj['comments'], users))
# print(inactive_users)
#=====================================================================

# names = ['Raychel', 'Sultan', 'Aigerim', 'John', 'Kira', 'Bob']
# new_names = list(
#     map(
#         lambda name: f'Your name is {name}!',
#         filter(lambda x: len(x) > 4, names))
# )
# print(new_names)
#=====================================================================
# from functools import reduce
# ls = [1,2,3,4,5,6]
# sum = reduce(lambda a, b: a + b, ls)
# res =reduce(lambda a, b: a * b, ls)
# print(sum)
# print(res)

#===================================================================
# ls = ['John', 'Sultan', 'Aigerim']
# for i, obj in enumerate(ls):
#     print(i, obj)

# import string as s
# import random

# def genrate_rand_str():
#     symbols = s.acii_letters + s.digits
#     res = ''.join(random.choice(symbols) for i range(0, 10))
#     return res

# print(genrate_rand_str())
# print(genrate_rand_str())
# print(genrate_rand_str())
# print(genrate_rand_str())
# print(genrate_rand_str())

#===================================
# from random import choices
# from string import ascii_letters, digits
# from itertools import repeat

# symnbols = '_()+-@$#!'
# q_pass = int(input('Vvedite kollichestvo paroley: '))

# result = {
#     f(choices(ascii_letters, k=10), choices(digits, k=5), choices(symnbols, k=2))
#     for f in repeat(lambda x, y, z: ''.join(set(x+y+z)), q_pass)
# }
# print(result)
# print(f'Quantity of paswords: {len(result)}')

# from statistics import mean

# dlina = [len(x) for x in result]
# print(f'Avarage len: {mean(dlina)}')

# zip для создания словарей
# a = dict([(1,2),(3,4)])
# print(a)
# {1:2, 3:4}.items()
# dict_items[(1,2), (3,4)]

# d_keys = ['hostname', 'locate', 'vendor', 'model', 'IOS', 'IP']
# d_value = ['apple_r1', 'winterfell', 'jobs', 'watch', '16.0', '10.255.01']

# i = 0
# res = {}
# for i in d_keys:
#     res[i] = d_value[i]
#     i += 1
# print(res)

# res = dict(zip(d_keys, d_value))
# print(res)

# d_keys = ['hostname', 'locate', 'vendor', 'model', 'IOS', 'IP']
# data = {
#     'r1': ['london_r1', 'New Globe Walk', 'cisco', '4551', '15.4', '10.255.0'],
#     'r2': ['london_r2', 'New Globe Walk', 'cisco', '5551', '16', '10.55.0'],
#     'sw1': ['london_sw1', 'South_west', 'cisco', '3850', '16.4', '10.2.12.0']
# }

# for k in data:
#     data[k] = dict(zip(d_keys,data[k]))
# print(data)

#=============================================
# all(), any()
# all(iterable) - возвращает True  если все элементы внутри объекта истинна иначе возвращает False

# all([1, 2]) -> True
# all([]]) -> False
# all(['False', 'John', 5, 6, 1]) -> True
# all([1,2,3], 5, None) -> False

# print(all([[1,2], 'stroka', True, 1]))
# print(all([], 1))

# ip = '10.10.10.10'
# result = all(i.isdigit() for i in ip.split('.'))
# print(result)

# any -> возвращает True, ели хотябы один элемент истина

# ls = [0, 0, 0, '', False]
# print(any(ls))

# ignore = ['rm -rf', 'reset', 'alias']
# command = input('vvedite comandu: ')
# #sudo nano file
# if any(word in command for word in ignore):
#     raise Exception('Invalid command')
# print('Vse ok!')
