# class Salary:
#     tax = 0.15
#     def __init__(self, salary, years) -> None:
#         self.salary = salary
#         self.years = years
#     def count_tax(self):
#         total_tax = self.salary*self.tax*12*self.years
#         return int(total_tax)
# mount = Salary(12000,5)
# print(mount.count_tax())

# class Calc:
#     def add(self, a, b):
#         '''Function of sum'''
#         return a + b
#     def sqrt(self, num):
#         '''функция нахождения квадратного корня'''
#         import math
#         res = math.sqrt(num)
#         return round(res, 2)

#     def percent(self, num, percent):
#         '''функция нахожденияя процента'''
#         return(num*percent)/100

#     def super_func(self, string):
#         '''функция вычиляет строку '1 + 2 + 1' '''
#         try:
#             return eval(string)
#         except:
#             return 'Ivalid Operation'

# calc = Calc()
# print(calc.add(4, 5))#9
# print(calc.sqrt(9))
# print(calc.percent(87, 35))
# print(calc.super_func('(5 - 7) ** 2 -10'))#-6
# print(calc.super_func(input('Enter number: ')))
'''===================SNIPER=================='''
# class Sniper:
#     health = 100
#     def __init__(self, name) -> None:
#         self.name  = name

#     def shoot(self, other):
#         other.health -= 20
#         print(f'Aтаковал {self}')
#         print(f'жертва {other}, осталось здоровья: {other.health}')

#     def __str__(self) -> str:
#         return self.name

# sniper1 = Sniper('John')
# sniper2 = Sniper('Jemie')
# print(sniper1, sniper1.health)
# print(sniper2, sniper2.health)

# import random 
# while sniper1.health and sniper2.health:
#     choice = random.randint(1, 2)
#     if choice == 1:
#         sniper1.shoot(sniper2)
#     else:
#         sniper2.shoot(sniper1)
# if sniper1.health:
#     print(f'{sniper1} победил!!!')
# else:
#     print(f'{sniper2} победил!!!')

# #=====================================
# class CRUD:
#     __products = []
#     __id = 0

#     def _get_id(self):
#         self.__id += 1
#         return self.__id

#     def _get_product(self, id):
#         for x in self.__products:
#             if x['id'] == id: return x
#         return False

#     def create(self):
#         print('CREATE of prodect!')
#         title = input('Enter name of product: ')
#         price = input('Enter price: ')
#         self.__products.append({
#             'id': self._get_id(),
#             'title': title,
#             'price': price
#         })

#     def list_of_products(self):
#         print('All products: ')
#         for x in self.__products:
#             print(x['title'])

#     def detail_product(self):
#         print('Detail')
#         id = int(input('Enter ID product: '))
#         product = self._get_product(id)
#         print(product if product else 'No such a product')

#     def update_product(self):
#         print('Update prodcut')
#         id = int(input('Enter ID of product: '))
#         product = self._get_product(id)
#         if not product:
#             print('No such product!')
#             return
#         choice = input('What need to change(title/price):')
#         index = self.__products.index(product)
#         self.__products[index][choice] = input('Enter new value')
    
#     def delete_product(self):
#         print('Delate!')
#         id = int(input('Enter ID of product: '))
#         product = self._get_product(id)
#         if not product:
#             print('No such product')
#             return
#         self.__products.remove(product)
#         print('Delated already!')
        

# product = CRUD()
# product.create()
# product.create()
# product.list_of_products()
# # product.detail_product()
# # product.detail_product()
# # product.update_product()
# # product.detail_product()

# product.delete_product()
# product.list_of_products()


'''------------------------------CLASS WORK------------------------------'''
# class SmartPhone:
#     def call(self,phone_number):
#         print(f"Calling to {phone_number} number")

# class Watch:
    