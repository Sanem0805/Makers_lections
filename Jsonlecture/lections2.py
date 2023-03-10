


#-- наша адача научиться переводить данные json d python dictionary

#!!!1
# JS object == {key: value}
# PY dict == {key: value}
# JSON == {key: value}

# Процессы Сериализации и  Десирталтзации данных

# Сериалихзация (Запись данных в JSON) - это перевод из python объектов в JSON формат

# josn.dump - метод записывает python данные в файл в формате JSON, парвлельно сделав сериализацию
# json.dumps - метод записывает python данные в файл в формате JSON, парвлельно сделав сериализацию

# Десириализация (чтение данных из Json) - это процесс перевода из JSONa в PY dict

# json.load - метод кторый считывает файл в формате JSON и переводит его в PY object
# json.loads - метод кторый считывает текст в формате JSON и переводит его в PY object

#==================================================================
# Процесс сериализации
# import json

# dict_ = {
#     'name': 'John', 
#     'last name': 'Snow',
#     'status': True,
#     'age': 24,
#     'wife': False,
#     'chldren': None
# }
# print(dict_)
# print(type(dict_))

# json_text = json.dumps(dict_)
# print('--------------')
# print(json_text)
# print(type(json_text))


# import json
# dict_ = {
#     'name': 'John', 
#     'last name': 'Snow',
#     'status': True,
#     'age': 24,
#     'wife': False,
#     'chldren': None
# }
# print(dict_)

# with open('new.json', 'w') as file:
#     json.dump(dict_,file)

# with open('new.json', 'r') as file:
#     data = file.read()
#     print(data)

# import json 
# with open('new.json', 'r') as file:
#     json_data = file.read()

# print(json_data)
# print(type(json_data))

# dict_ = json.load(json_data)
# print(dict_, type(dict_))

# import json
# with open('new.json') as file:
#     dict_ = json.load(file)
#     print(dict_)
#     print(type(dict_))


# from urllib.request import urlopen
# import json
# url = 'https://randomuser.me/api/'
# json_data = urlopen(url)

# print(json_data)
# # print(type(json_data))
# # print(json_data.read())

# dict_ = json.load(json_data)# .loads(json_data.read())
# print(dict_)
# print(type(dict_))

#1json tasks
# import json
# with open('task1.json', 'r') as f:
#     python_obj = json.loads(f.read())

# with open('task1.py', 'w') as f1:
#     f1.write(str(python_obj))
# другая версия решения
# import json
# file1 = open('task1.json')
# python_obj = json.loads(file1.read())
# file1.close()
# with open('task1.py', 'w') as file2:
#   file2.write(str(python_obj))

#2
# import json
# with open('task2.json', 'r') as f:
#   json_obj = f.read()
#   python_obj = json.loads(json_obj)
#3
# import json
# python_obj = None 
# json_obj = json.dumps(python_obj)
# print(json_obj)
#4
# import json
# json_obj = "null" 
# python_obj = json.loads(json_obj)
# print(python_obj)
#5
# import json
# users = [
#     {
#         'name': 'John',
#         'last_name': 'Snow',
#         'age': 26,
#         'has_car': True,
#     },
#     {
#         'name': 'Sam',
#         'last_name': 'Bolt',
#         'age': 4,
#         'has_car': False,
#     }
# ]
# json_users = json.dumps(users)
# print(json_users)
#6
# import json
# json_products = '[{"title":"iphone","price":700,"rating":4.8},{"title":"asus","price":1300,"rating":3.9},{"title":"macbook pro","price":1500,"rating":4.9},{"title":"samsung","price":150,"rating":5.0}]'
# python_product = json.loads(json_products)
# for i in python_product:
#     if i['rating'] > 4:
#         print(i['title'])
    
#7
# import json
# with open('/Users/sanem0805/Desktop/pykers/Jsonlecture/new.json') as file:
#     list_ = json.load(file)
#     for dict1 in list_:
#         dict1["description"] = "..."
#     js_dict = json.dumps(list_)
        
# with open('new_db.json', 'w') as f1:
#     f1.write(js_dict)

#8
# import json
# with open('/Users/sanem0805/Desktop/pykers/Jsonlecture/new.json') as file:
#     list_ = json.load(file)
#     for product in list_:
#         if product['id'] == 3: 
#             list_.remove(product)
#     js_dict = json.dumps(list_)
   
# with open('new_db.json', 'w') as f1:
#     f1.write(js_dict)

#9
# import json
# def create_new(id: int, title: str, description: str, price: int, rating:float) -> None:
#     ls = [id, title, description, price, rating]
#     with open('db.json', 'r') as file:
#         python_list = json.load(file)
#         python_k_list = ['id', 'title', 'description', 'price', 'rating']
#         python_dict = dict(zip(python_k_list, ls))
#         python_list.append(python_dict)
#         js_obj = json.dumps(python_list)
#     with open('new_db.json', 'w') as f1:
#         f1.write(js_obj)
# create_new(id=100, title='iphone', description='...', price=20, rating='5.5')
# другое решение
# import json
# def create_new(id: int, title: str, description: str, price: int, rating:float) -> None:
#     dict_={'id':id, 'title':title, 'description':description, 'price':price, 'rating':rating}
#     with open('db.json') as file:
#         res = json.load(file)
#         res.append(dict_)
#         with open('new_db.json', 'w') as f:
#             f.write(json.dumps(res))
# create_new(10, 'assa', 'asd', 12, 25.0)
#10
# import json
# def get_sorted(json_filename: str):
#     # list1 = []
#     with open('/Users/sanem0805/Desktop/pykers/Jsonlecture/new.json') as file:
#         python_list = json.load(file)
#         for dict1 in python_list:
#             sorted_dict = sorted(dict1['rating'].values(), reversed=False)
#             return python_list
    #     sorted(python_list, key=lambda x: x['rating'], reverse=True)
    #     return python_list
    #     for x in python_list:
    #         list1.append(x['title'])
    # print(list1)
    
# print(get_sorted('/Users/sanem0805/Desktop/pykers/Jsonlecture/new.json'))

#13
# import json
# def filter_by_price(price: int):
#     with open('/Users/sanem0805/Desktop/pykers/Jsonlecture/new.json') as file:
#         python_list = json.load(file)
#         list_ = []
#         for k in python_list:
#             if k["price"] >= price:
#                 list_.append(k)
#         return list_

# print(filter_by_price(1000))

#12
# import json
# def search(name: str):
#     with open('/Users/sanem0805/Desktop/pykers/Jsonlecture/new.json') as file:
#         python_list = json.load(file)
#         list_ = []
#         for k in python_list:
#             if name in k['title']:
#                 list_.append(k)
#         return list_
# print(search('sus'))

#11
# import json
# def searchupdate(id: int, title: str=None, price: int=None, rating: float=None):
#     with open('/Users/sanem0805/Desktop/pykers/Jsonlecture/new.json') as file:
#         python_list = json.load(file)
#         # list_ = []
#         for k in python_list:
#             if k['id'] not in python_list:
#                 print('ValueError') 
#             else:
#                 k['title'].update()
#                 k['price'].update()
#     with open('new_db.json', 'w') as f:
#             f.write(json.dumps(python_list))
# searchupdate(4, 'sas', 12, 25.0)

#14
import json
def bulk_create(products: List[dict]) -> None:
    with open('/Users/sanem0805/Desktop/pykers/Jsonlecture/new.json') as file:
        python_list = json.load(file)
        for k in python_list:
            if k['id'] != products['id']:
                python_list.update(products)

