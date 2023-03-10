# существуют 3 вида методов
# class methods, isinstance methods, static methods
# instance methods - обычные методы которые принимают первым аргументом self(ссылка на оъект). Нужны они для того чтобы внутри метода мы смогли работать с аттрубутами оъекта

# class A:
#     def instance_method(self, a):
#         print('метод объекта')
#         print('первый аргумент:', self)
# obj_a = A()
# obj_a.instance_method() #ели вызываем у объекта, то self передаеться автооматически
# A.instance_method(obj_a, 5)# если вызываем у класса, то у self нужно прописыввать в ручную

# class method -методы которые принимают первым аргументом cls (ссылка на класс). Нужны они для создания оъектов или изменения аттрибутов класса. Для того чттобы создать классс метод нужно воспользоваться декаратором @classmethod

# class B:
#     @classmethod
#     def class_method(cls, a):
#         print('класс метод')
#         print('первый аргумент:', cls)
# obj_b = B()
# obj_b.class_method()
# B.class_method(5)

# class C:
#     counter = 0
#     def __init__(self) -> None:
#         self._inc_counter()

#     @classmethod
#     def _inc_counter(cls):
#         cls.counter += 1

# obj1 = C()
# obj2 = C()
# obj3 = C()
# obj4 = C()
# obj3.counter = 3
# print(obj3.counter())
# print(C.counter)

# class Pizza:
#     def __init__(self, radius, *ingredients) -> None:
#         self.r = radius
#         self.ingredients = ingredients
#     def cook(self):
#         print(f'готовиться пицца размером {self.r * 2 } cm')
    
#     @classmethod
#     def four_cheese(cls, r):
#         pizza = cls(r,'моцарелла', 'чедер', 'голандский', 'брынза')
#         return pizza

# pizza1 = Pizza(17, 'пепрони', 'эмоцарелла', 'грибы')
# # pizza2 = Pizza(15, 'моцарелла', 'чедер', 'голандский', 'брынза')
# # pizza3 = Pizza(20, 'моцарелла', 'чедер', 'голандский', 'брынза')
# pizza2 = Pizza.four_cheese(15)
# pizza3 = Pizza(20)

# class Person:
#     surname = 'Stark'
#     def __init__(self, name, age) -> None:
#         self.name = name 
#         self.age = age

#     @classmethod
#     def from_birth_date(cls, name, date_birth):
#         from datetime import date
#         age = date.today().year - date_birth
#         return cls(name, age)

# # obj = Person('John', 24)
# print(obj.name, obj.surname, obj.age)

# # obj2 = Person('Sansa', 1961)   #1 метод создания оъекта
# # print(obj2.name, obj2.surname, obj2.age)

# obj2 = Person.from_birth_date('Sansa', 1961)  # 2 метод
# print(obj2.name, obj2.surname, obj2.age)

#============================================
# staticmethod - просто функция внутри класса, которые не взаимодействуют ни с классом, ни с оъектом. НАходятся они внутри класса лишь потому что их используют только внутри класса, так как они вне бесполезны 
# @staticmethod - декаратор

# class C:
#     @staticmethod
#     def static_method():
#         print('статический метод')
# obj = C()
# obj.static_method()
# C.static_method()

# class Cylinder:
#     def __init__(self, diameter, height) -> None:
#         self.di = diameter
#         self.h = height
#         self.area = self. get_area(self.di, self.h)

#     @staticmethod
#     def get_area(diameter, h):
#         from math import pi
#         circle = pi * (diameter / 2) ** 2
#         side = pi * h * diameter
#         area = circle * 2 + side
#         return round(area, 2)

# obj = Cylinder(10, 7)
# print(f'Area: {obj.area}')

# obj1 = Cylinder(4, 10)
# print(f'Area: {obj1.area}')

# class Plant: 
#      season = 'зима' 

#      @classmethod 
#      def change_season(cls, value): 
#          cls.season = value 

# Plant.change_season('весна') 
# kaktus = Plant() 
# ficus = Plant() 
# print(kaktus.season, ficus.season) #весна весна 
#1
# class Product:
#     base_price = 20_000
#     def __init__(self, model, year, color) -> None:
#         self.model = model 
#         self.year = year
#         self.color = color
#     def  has_garantiya(self, year):
#         varanty = year - self.year
#         if varanty > 2:
#             return 'Ваша гарантия истекла'
#         else:
#             return 'Гарантия действительна'
#     @classmethod
#     def change_price(cls, rate):
#         cls.base_price = cls.base_price + int(cls.base_price * rate/100)
#         print(cls.base_price)

# obj = Product('a50', 2018, 'red')
# obj.change_price(3)
# print(obj.has_garantiya(2020))
# print(obj.has_garantiya(2021))
#2
# class User:
#     def __init__(self, name, lastname, email):
#         self.name = name
#         self.lastname = lastname
#         self.email = email
    
#     @staticmethod
#     def validate_email(email):
#         return "@" in email
    
#     def __str__(self):
#         if self.validate_email(self.email):
#             return f"{self.name}: {self.email}"
#         else:
#             return "email в неправильном формате"
    
#     @classmethod
#     def create_user(cls, string1):
#         name, lastname, email = string1.split(", ")
#         return cls(name, lastname, email)
# user1 = User.create_user('John, Snow, john@email.com') 
# user2 = User.create_user('John, Snow, johnemail.com') 
# print(user1) 
# print(user2)
#3
# class Makers:
#     student_count = 0
#     def __init__(self, name, language, kpi) -> None:
#         self.name = name 
#         self.language = language
#         self.kpi = self.set_kpi(kpi)
#     @classmethod
#     def new_student(cls, name, language, kpi):
#         cls.student_count += 1
#         return cls(name, language, kpi)
#     def get_info(self):
#         return f"Student name: {self.name}, Language: {self.language}"
#     def set_kpi(self, kpi):
#         self.kpi = kpi
#         return self.kpi
# student1 = Makers.new_student("Vlad", "Python", 9)
# student2 = Makers.new_student("Malik", "JavaScript", 7)
# print(student1.set_kpi(89)) 
# print(student1.get_info()) 
# print(student2.set_kpi(89)) 
# print(student2.get_info()) 
# print(Makers.student_count)
#4
# class Bike:
#     def __init__(self, cost, make, model, year, min_profit):
#         self.cost = cost
#         self.make = make
#         self.model = model
#         self.year = year
#         self._sale_price = None
#         self.sold = False
#         self.min_profit = min_profit
        
#     def set_cost(self, price):
#         if price > self.cost:
#             self._sale_price = price
#         else:
#             self._sale_price = price + self.min_profit
            
#     def service(self, repair_cost):
#         self._sale_price += repair_cost
#         return self._sale_price
        
#     def sell(self):
#         self.sold = True
#         return abs(self._sale_price - self.cost)
    
#     @classmethod
#     def get_default_bike(cls):
#         return cls(10000, "Author", "Basic ASL", 2020, 2000)

# bike = Bike.get_default_bike() 
# bike.set_cost(6000) 
# bike.service(300) 
# print(bike.sell()) 
# print(bike.cost) 
# print(bike.make) 
# print(bike.year) 
# print(bike._sale_price) 
# print(bike.sold) 
# print(bike.min_profit) 
#5
# class  MoneyFmt:
#     def __init__(self, amount) -> None:
#         self.amount = amount

#     @staticmethod
#     def dollarize(float_num): 
#         if float_num >= 0:
#             return "${:,.2f}".format(float_num)
#         else:
#             return "-${:,.2f}".format(-float_num)

#     def update(self, new_amount):
#         self.amount = new_amount
#         return self.amount

#     def __repr__(self) -> str:
#         return str(self.amount)
    
#     def __str__(self) -> str:
#         return self.dollarize(self.amount)

# cash = MoneyFmt(12345678.021) 
# print(cash) 
# cash.update(100000.4567) 
# print(cash) 
# cash.update(-0.3) 
# print(cash) 
# print(repr(cash))
      
      
# class MoneyFmt:
#     def __init__(self, amount):
#         self.amount = amount
        
#     def update(self, amount):
#         self.amount = amount
        
#     def __repr__(self):
#         return str(self.amount)
        
#     @staticmethod
#     def dollarize(float_num):
#         if float_num < 0:
#             sign = "-"
#             float_num = abs(float_num)
#         else:
#             sign = ""
#         dollars = int(float_num)
#         cents = round((float_num - dollars) * 100)
#         dollars_str = "{:,d}".format(dollars)
#         cents_str = "{:02d}".format(cents)
#         return "{}${}.{}".format(sign, dollars_str, cents_str)
    
#     def __str__(self):
#         return MoneyFmt.dollarize(self.amount)
# cash = MoneyFmt(12345678.021) 
# print(cash) 
# cash.update(100000.4567) 
# print(cash) 
# cash.update(-0.3) 
# print(cash) 
# print(repr(cash)) 
'''------------'''
# dict1 = {1: '2', 2: '3', 3: '4'}
# sum1 = sum(dict1.keys())/len(dict1)
# print(sum1)
''''------------'''
word1 = 'H  e  l  l  o          '
string = word1.replace(' ', '')
print(string)
word12 = 'H  e  l  l  o         o'   
string2 = word12.strip()
print(string2)