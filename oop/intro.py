#OOП Объектно- ориентированное программирование
# Класс -> это описание того как должен выглядеть объект, тл есть в классе мы описываем какими свойсвами должен обладать объект
# Объект - это сущьность которую мы создаем от класса, у оъекта есть состояние свойств(данных)
# Цель её создание было создать данные(аттрибуты) с функциями которые использоввали их
# Свойсввами(аттрибуты) - называют обычные переменные внутри класса, в которых храныться данные определённого объекта
# Методы - это обычные функции которые описывают поведение объекта, функции внутри класса называют методами
#-------------------------
# john = ['John', 'Snow', 'King of North',5000, 30]

# def show_info(human):
#     print(f'Name: {human[0]} {human[1]},Age: {human[-1]}, Job: {human[2]}, Slary: {human[3]}')

# show_info(john)

# class Human:
#     def __init__(self, name, last_name, age, job, salary):
#         self.name = name + " " + last_name
#         self.age = age
#         self.job = job
#         self.salary = salary

#     def show_info(self):
#         return f'Name: {self.name}, Age: {self.age}, Job: {self.job}, Salary: {self.salary}'
# john = Human('John', 'Snow', 30, 'King of North', 5000)
# sultan = Human('Sultan', 'Kotana', 19, 'Mentor', 100)

# print(dir(john))
# print(john.show_info())
# print(john.name)
# print(john.age)
# print('-----------')
# print(sultan.show_info)
# print(sultan.name)

# #---------------------------------
# class Dog:
#     # аттребуты класса
#     age = 0
#     ushi = True
    
#     def __init__(self, name, color):
#         '''Иництализатор именно здесь создаються аттрибуты объекта'''
#         # в self прилетает ссылка на объекты класса
#         self.name = name # аттрибуты объукта
#         self.color = color

#     def bark(self):
#         print(f'{self.name} лает!')

# bobik = Dog('Bobik', 'brown')
# yumi = Dog(name='Yumi', color='White')
# aktosh = Dog('Aktosh', 'gray')

# print(f'name: {bobik.name}, age: {bobik.age}, color: {bobik.color}, ushi: {bobik.ushi}')
# print(f'name: {yumi.name}, age: {yumi.age}, color: {yumi.color}, ushi: {yumi.ushi}')
# print(f'name: {aktosh.name}, age: {aktosh.age}, color: {aktosh.color}, ushi: {aktosh.ushi}')

# bobik.age = 2
# yumi.age = 1
# aktosh.age = 3
# aktosh.ushi = False

# print('After')
# print(f'name: {bobik.name}, age: {bobik.age}, color: {bobik.color}, ushi: {bobik.ushi}')
# print(f'name: {yumi.name}, age: {yumi.age}, color: {yumi.color}, ushi: {yumi.ushi}')
# print(f'name: {aktosh.name}, age: {aktosh.age}, color: {aktosh.color}, ushi: {aktosh.ushi}')

# yumi.bark()

# class Human():
#     age = 0
#     def __init__(self) -> None:
#         print('int worked')
#         self.raychel = 'raychel'

#     def methon1(self):
#         self.john = 'john'
#         print('method1 worked')
# obj = Human()
# print(obj.raychel)
# obj.methon1()
# print(obj.john)

#1 задания ооп
# class Song:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
    
#     def show_title(self):
#         return f'Название этой песни {self.title}'

#     def show_author(self):
#         return f'Автор этой песни {self.author}'

#     def show_year(self):
#         return f'Эта песня вышла в {self.year} году'

# song = Song(title='Happy', author='Pharrell Williams', year=2013)
# print(song.show_title())
# print(song.show_author())
# print(song.show_year())

#2 S = π × r2,
# from math import pi
# class Circle:
#     color = 'синий'
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
        
#     def get_area(self):
#         s = pi*self.radius**2
#         return round(s, 2) 

# circle = Circle(radius=13)
# circle.color = 'желтый'
# print(f'circle.color, circle.get_area()')
# print(circle.get_area()) 
# правильный ответ
# class Circle:
#     color = 'Синий'
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
        
#     def get_area(self):
#         return self.pi*(self.radius**2)
        

# circle = Circle(radius=13)
# circle.color = 'желтый'
# print(circle.color)

# print(circle.get_area())
# 
# 3

# class BankAccount:
#     def __init__(self):
#         self.balance = 0
#     def withdraw(self, amount):
#         self.balance -= amount
#         print(f'Ваш баланс: {self.balance} сом')
#     def deposit(self, amount):
#         self.balance += amount
#         print(f'Ваш баланс: {self.balance} сом')

# account = BankAccount()
# account.deposit(1000)
# account.withdraw(500)

#4
# class Taxi:
#     def __init__(self, name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km
#     def get_total_cost(self, km):
#         self.cost = self.cost_km * km + self.cost
#         return f'Такси {self.name}, стоимость поездки: {self.cost} сом'


# taxi1 = Taxi(name='Namba',cost=29, cost_km=15)
# taxi2 = Taxi(name='Yandex',cost=25, cost_km=17)
# taxi3 = Taxi(name='Jorgo',cost=28, cost_km=15)
# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14))
#5
# class Phone:
#     def __init__(self, name,last_name, phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone
#     def get_info(self):
#         print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')

# contact = Phone('John', 'Snow', '+996707707707')
# contact.get_info()
#6
# class Salary:
#     percent = 8
#     def __init__(self, salary, experience):
#         self.salary = salary
#         self.experience = experience
#     def count_percent(self):
#         res = (self.salary*self.percent)/100*self.experience
#         return res
# obj = Salary(10000, 10)
# print(obj.count_percent())
        
#7
# import datetime
# class Nobel:
#     def __init__(self, category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner
#     def get_year(self):
#         today = datetime.date.today()
#         res = today.year - self.year
#         return f'выиграл {res} лет назад'


# winner1 = Nobel('Литература', 1971, 'Пабло Неруда')
# print(winner1.category, winner1.year, winner1.winner)
# print(winner1.get_year())

# winner2 = Nobel('Литература', 1994, 'Кэндзабуро Оэ')
# print(winner2.category, winner2.year, winner2.winner) 
# print(winner2.get_year())

#8
# class Password:
#     def __init__(self, password):
#         self.password = password

#     def __str__(self) -> str:#fcfghjk
#         return '*' * len(self.password)

#     def validate(self):
#         if  not len(self.password) == 8 and len(self.password) < 15:
#             return f'Password should be longer than 8, and less than 15'
#         if not any(map(lambda i: i.isdigit(), self.password)):
#             return f'Password should contain numbers too'
#         if not any(map(lambda i: i.isalpha(), self.password)):
#             return f'Password should contain letters as well'
#         if not any(map(lambda i: i in ['@', '#', '&', '$', '%', '!', '~', '*'], self.password)):
#             return f'Your password should have some symbols'
#         return f'Ваш пароль сохранен.'
# password = Password('sanem23@')
# print(password.validate())
# print(password)
#9
# class Math:
#     def __init__(self, number):
#         self.number = number

#     def get_factorial(self):
#         self.factorial = 1
#         for i in range(2, self.number+1):
#             self.factorial = self.factorial*i
#         return self.factorial

#     def get_sum(self):
#         number = [int(x)for x in str(self.number)]
#         suma = sum(number)
#         return suma

#     def get_mul_table(self):
#         s  = ''
#         for i in range(10):
#             s += f'{self.number}x{i+1}={self.number * (i+1)}' + '\n'
#         return s

# number1 = Math(0) 
# print(number1.get_factorial()) 
# print(number1.get_sum())
# print(number1.get_mul_table())
#10
# class ToDo:
#     instances = {}
#     def __init__(self, task) -> None:
#         self.task = task
#     def give_priority(self,priority):
#         ToDo.instances[priority] = self.task
#     def list_of_tasks(self):
#         return sorted(self.instances.items())
# a = ToDo('сходить в кино')
# a.give_priority(3)
# b = ToDo('сделать домашку')
# b.give_priority(1)
# c = ToDo('выгулять собаку')  
# c.give_priority(2)  
# print(ToDo.instances)  
# print(a.list_of_tasks())    
with open("test2.txt", "w") as f:
    f.write("python is the best")









