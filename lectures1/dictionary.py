# obj = ['John', 'Snow', 24, 500, '+996700800900', 'Winterfell']
# obj = {'name': 'John','last name': 'Snow', 'age': 24, 'cash': 500, 'phone number': '+900700800900'}
# print(obj[name])
#print(obj['cash'])

# dic() -Словарь упрядоченная коллекция элементов(pyhton 3.7) Каждый элемент внутри словаря содержиться в паре ключ: значение
#Ключи должны быть не изменяемым типом данных(str, int, tuple ect),  тогда как занчениями могут выступать любые типы данных.

#thisdic = {'brand': 'ford', 'model':'mustang', 'year': 1964}
# print(thisdic)
# print(type(thisdic))

# ассоциативный массив, hash table, object(js), structure == dictionary(py)

#Создание словарей:
# a =dict(c=1, b=2, q=4)
# print(a)
# a = {'c': 1, 'b': 2, 'q': 4}
# print(a)
# как из списка сделать словарь можно также создать из кортежей вместо квадратных 
# любые круглые скобки
# my_list =[['m', 1], ['a', 2], ['k', 3]]
# my_dict = dict(my_list,c=1, b=2, q=4)# сделалт словарь и здесь мы ещё прибавили элементы в словарь
# print(my_dict)
# Получение эемента словаря:
# dict_ = {'Tom': 'balck', 'cat': 'animal'}
# print(dict_['Tom'])
# # поменять значение на другое
# dict_['Tom'] = 'blue'
# print(dict_)
my_dict = {1: 'ass', 2: 'ssd', 3: 'aggah'}
# get(key,None)
print(my_dict.get(2, 'no such key in this dict_'))

# dict_ = {'Tom': 'balck', 'cat': 'animal'}
# print(id(dict_))#4366579776
# dict_.clear()
# print(id(dict_))#4366579776
#===============================================================================
#user_info = {
#     'first-name': 'John',
#     'last_name': 'Snow',
#     'email': 'john73@gmail.com',
#     'role': 'moderator'
#     #[1, 2, 3]: 'list'- ошибка

#     }
# print(user_info)
# print(user_info.get('first_name1'))#NONE
# print(user_info.['first_name'])#error

#======================================================================================================

# user_info = {
#     'first-name': 'John',
#     'last_name': 'Snow',
#     'email': 'john73@gmail.com',
#     'role': 'moderator'
    #[1, 2, 3]: 'list'- ошибка
# }
# #print(dir(dict))
# a = (1, 2)
# print(a, type(a))
# num1, num2 = a
# print(num1)
# print(num2)


# print(user_info.values())
# print(user_info.keys())
# print(user_info.items())
# print()

# for key in value in user_info.items
# print(key,values)
#==================================================================================

# dict_ = {1: 15, 2: 11, 3: 18, 4:5, 5:21}
# print(dict_)
# for key, value in dict_.items():
#     if key % 2 == 0:
#         print(key, ' чётное')
#     else:
#         print(key, 'нечетное')
#         dict_[key] = value ** 2

# print(dict_)


# Изменение словаря
# dict_ = {'name': 'John', 'age': 24}
# print(dict_)
# dict_['age'] = 23
# dict_['adress'] = 'Wninterfell'
# print(dict_)

# dict_ = {'name': 'John', 'age': 24}
# print(dict_)
# dict_.update({'age':18, 'adress': 'Winterfell'})
# print(dict_)

#===============================================================

#fromkeys - быстрое создание из ключей
# keys = ['one', 'two', 'three']

# new_dict = dict.fromkeys(keys, 'value')
# print(new_dict)

# dict_ = {}
# ls = list(range(1, 101))

# new_dict = dict_.fromkeys(ls, 'value')
# print(new_dict)

#=====================================================================
#setdefault - работает также как и метод get(), но если нет такого ключа то он создаст новый

# dict_ = {'name': 'John', 'age': 24}
# print(dict_)
# print(dict_.setdefault('age'))
# print(dict_.setdefault('name'))
# print(dict_.setdefault('adress', 'Moscow str.'))
# print(dict_)

#=====================================================================

# Удаление из словря
#pop(key) - удаляет элемнет по ключу

# dict_ = {'name': 'John', 'last_name': 'Snow', 'adress': 'Winterfell'}
# print(dict_)
# removed = dict_.pop('adress')
# print(removed)
# print(dict_)

#========================================================

#popitem()- удаляет последний элемент
#dict_ = {'name': 'John', 'last_name': 'Snow', 'adress': 'Winterfell'}
# print(dict_)
# removed = dict_.popitem()
# key, value = removed
# print(dict_)
# print(key, value)


# roles = {
#     0: 'Moderator',
#     1: 'Admin',
#     2: 'Customer',
#     3: 'Vendor'
# }

# users = {
#     '1': {'username': 'Johnsnow', 'role': roles[1]},
#     '2': {'username': 'JamieLanister', 'role':roles[2]},
#     '3': {'username': 'Mufasa', 'role':roles[3]}
# }

# product = {
#     'id': 1,
#     'title': 'Iphone 14 Pro max',
#     'description': 'Loren Ipson',
#     'price': 200
# }
# i = '1'
# while i == '1' or 1 == '2':
#     i = (input('Vvedite chto hotite sdelat:\nEsli hotite posmotret tovar to najmite 1\nElsli hotite izmenit tovar to najmite2\n esli hotite vuiti to najmite 3 ili to cho to drugoe\nVash vubor:'))
#         print(product)
#     elif i == '2':
#         id_user = (input('\nВведите ваш id: '))
#         if users.get(id_user) == None:
#             print('Нет такого юзера!')
#         elif users.get(id_user)['role'] == roles[1]:
#             print(users.get(id_user))
#             choice = input('введите что изменить(title, description, price): ')
#             new = input(f'Введите новое значение{choice}: ')
#             product.update({choice: new})
#             print('Updated!')
#         else:
#             print(users.get(id_users))
#             print('sorry just admin can edit!, у тебя нет разрешения!')