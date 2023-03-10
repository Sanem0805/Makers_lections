#Принципы ООП
# 1. наследование
# 2. Инкапсуляция
# 3. Полиморфизм

# 4. Абстрация
# 5. Композиция
# 6. Агрегация
#---------------------------
# Наследование в ООП позволяет принимать родительские методы и атрибуты для дочернего класса

# Родительский класс
# Дочерний класс
#------------------------------
# class Animal:
#     def print_info(self):
#         print("I'm an animal!")


# class Croco:
#     def print_info(self):
#         print('I\'m an animal!')

#--------------------
# class Animal:
#     name = None
#     golos = None
#     meal = None

#     def say(self):
#         print(f'This animal is {self.name}: {self.golos}')

#     def eat(self):
#         print(f'This animal is {self.name}: {self.meal}')

# class Lion(Animal):
#     name = 'loin'
#     golos = 'roar'
#     meal = 'meat'
#     griva = True
#     def info(self):
#         print(f'{self.name} griva: {self.griva}')
#     def say(self):
#         print(f'King of animal!')

# class Dog(Animal):
#     name = 'dog'
#     golos = 'bark'
#     meal = 'meat'


# class Koala(Animal):
#     name = 'koala'
#     golos = 'roar'
#     meal = 'efkalipt'

# rex = Dog()
# simba = Lion()
# julian = Koala()

# rex.say()
# rex.eat()

# julian.say()
# julian.eat()

# simba.say()
# simba.eat()
# simba.info()
#============================
# class Person:
#     def info(self):
#         print('I\'m peson from Bishkek')

# class Student(Person):
#     def info(self):
#         super().info()
#         print('I\'m study at Manas University')

# obj = Student()
# obj.info()

# obj2 = Person()
# obj2.info()

# class Laptop:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
    
#     def get_info(self):
#         return {'brand': self.brand, 'model': self.model, 'price': self.price}


# class MackBook(Laptop):
#     def __init__(self, brand, model, price, year, display):
#         super().__init__(brand, model, price)
#         self.year = year
#         self.display = display

#     def get_info(self):
#         repr = super().get_info()
#         print(repr)
#         repr['year'] = self.year
#         repr['display'] = self.display
#         return repr

# class Acer(Laptop):
#     def __init__(self, brand, model, price, videocard, display):
#         super().__init__(brand, model, price)
#         self.videocard = videocard
#         self.display = display
    
#     def get_info(self):
#         repr = super().get_info()
#         repr['videocard'] = self.videocard
#         repr['display'] = self.display
#         return repr
    



# mac = MackBook('Apple', 'Air', 1000, 2022, 13)
# print(mac.get_info())

# acer = Acer('Acer', 'Swift', 600, 'ge force 3040', 'xRGB14')
# print(acer.get_info())
#================================================

# class Employee:
#     bonus = 1.5

#     def __init__(self, firs_name, last_name, salary):
#         self.name = f'{firs_name} {last_name}'
#         self.salary = salary
    
#     def get_info(self):
#         return f'FIO: {self.name}, Salary: {self.salary}'
    
#     def give_increase(self):
#         self.salary = self.salary * self.bonus

# class Developer(Employee):
#     def __init__(self, firs_name, last_name, salary, language):
#         super().__init__(firs_name, last_name, salary)
#         self.prog_lang =language

#     def get_info(self):
#         info = super().get_info()
#         info += f' Prog Language: {self.prog_lang}'
#         return info

#     def __str__(self):
#         return self.get_info()

# class Maneger(Employee):
#     def __init__(self, firs_name, last_name, salary, devs=[]):
#         super().__init__(firs_name, last_name, salary)
#         self.devs = devs

#     def add_devs(self, developer):
#         self.devs.append(developer)

#     def show_devs(self):
#         return [x.get_info() for x in self.devs]

#     def __str__(self):
#         return self.get_info()

# dev1  = Developer('John', 'Snow', 1500, 'Python')
# dev2 = Developer('Stev', 'Jobs', 3000, 'C++')
# dev3 = Developer('Lary', 'Page', 1500, 'JS')
# dev4 = Developer('Tirion', 'Lanister', 1000, 'Python')

# man1 = Maneger('Jamie', 'Lanister', 2000)
# man2 = Maneger('Dastan', 'Kotana', 4000, [dev3, dev2])
# print(f'Manager {man1.get_info()}, has {man1.show_devs()} developers!')
# print(f'Manager {man2.get_info()}, has {man2.show_devs()} developers!')


# man1.add_devs(dev1)
# man1.add_devs(dev4)
# man2.add_devs(dev1)
# print('After!')
# print(f'Manager {man1.get_info()}, has {man1.show_devs()} developers!')
# print(f'Manager {man2.get_info()}, has {man2.show_devs()} developers!')

# dev1.give_increase()
# man2.give_increase()

# print(dev1)
# print(man2)

#1
# class Class1:
#     def first(self):
#         pass
#     def second(self):
#         pass

# class Class2(Class1):
#     def third(self):
#         pass
#     def fourth(self):
#         pass

# obj = Class2()
# obj.first()
# obj.second()
# obj.third()
# obj.fourth()
#2
# class A:
#     def method1(self):
#         print('Основной функционал')

# class B(A):
#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')

# obj = B()
# obj.method1()
#3
# class MyString(str):
#     def __init__(self, stroka1):
#         self.stroka1 = stroka1

#     def append(self, stroka2):
#         self.stroka2 = stroka2
#         self.stroka1 = self.stroka1 + self.stroka2
#         return self.stroka1

#     def pop(self):
#         last_w = self.stroka1[-1]
#         self.stroka1 = self.stroka1[:-1]
#         # print(self.stroka1)
#         return last_w

#     def __str__(self) -> str:
#         return self.stroka1

# example = MyString('String') 
# print(example.append('hello'))
# print(example.pop())
# print(example) 
#4
# class MyDict(dict):
#     def get(self, key):
#         res = ('Are you kidding?')
#         return dict.get(self, key, res)

# obj_dict = MyDict({'some_title': 2}) 
# print(obj_dict.get('some'))
#5

# class Person:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         return f'name:{self.name}, age:{self.age}'
# class Student(Person):
#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty
#     def display_student(self):
#         info = super().display()
#         info += f', faculty:{self.faculty}'
#         return info
# obj_student = Student('Rick', 21, 'science')
# print(obj_student.display())
# print(obj_student.display_student())
#6
# class ContactList(list):
#     def __init__(self, list1):
#         self.list1 = list1
        
#     def search_by_name(self, name):
#         a = []
#         for i in self.list1:
#             if name in i:
#                 a.append(i)
#         return a

# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya'))
#7
# class SmartPhones:
#     def __init__(self, name, color, memory):
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = 0

#     def __str__(self):
#         return f"{self.name} {self.memory}"

#     def charge(self, number):
#         self.battery += number
    
# class Iphone(SmartPhones):
#     def __init__(self, name, color, memory, ios):
#         super().__init__(name, color, memory)
#         self.ios = ios

#     def send_imessage(self, string):
#         return f"sending {string} from {self.name} {self.memory}"


# class Samsung(SmartPhones):
#     def __init__(self, name, color, memory, android):
#         super().__init__(name, color, memory)
#         self.android = android

#     def show_time(self):
#         import datetime
#         return datetime.datetime.now().time()


# phone = SmartPhones('generic', 'blue', '128GB') 
# print(phone) 

# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery) 

# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7)
# print(iphone7.send_imessage('hello'))

# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
# print(samsung21.show_time())
#8
# class CustomError(Exception):
#     def __init__(self, message):
#         self.message = message
    
# capitals_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')

# def check_letters(str_):
#     if str_.islower():
#         raise capitals_error
#     else: return f"ВСЕ ОТЛИЧНО! {str_}"

# print(check_letters("HELLO"))
        