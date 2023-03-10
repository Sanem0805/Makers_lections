#Полиморфизм
# print(len('makers'))
# print(len([1,2,3,4]))
# print(len({1: 2, 3: 4}))

# +(__add__) - метод полиморфизма
# print(5 + 5)
# print('hello' + 'world')
# print([1,2,3] + [4,5,6])
# полиморфизм способность метода обрабатывать данные разных типов (объектов от класса) обычно реализуеться путем создания базового класса и наличия двух и более подклассов, которые все реализуют (переопределяют) меотоды с одиноковой сигнатурой(названием)
# Широко распрастраненное определение: "Один интерфейс - много релизаций"

# class Animal:
#     def info(self):
#         pass 
#     def make_sound(self):
#         pass
# class Dog(Animal):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print('it\'s a dog. Dogs name is {self.name}, age {self.age}')
     
#     def make_sound(self):
#         print('Bark bark')

# class Cat(Animal):
#     def info(self):
#         print("it's a cat. Cats name is {self.name}, age {self.age}")
     
#     def make_sound(self):
#         print('Meow meow')

# cat = Cat('Garfid', 5)
# dog = Dog('Pluto', 9)

# for obj in (cat, dog):
#     obj.info()
#     obj.make_sound()
#     print()
#------------------------------------------------------------
#Обстракция(Абстракный класс) - его можно рассматривать как набор методов которые должны бать реализованы во всех дочерних классах, котрые будут унаследованы от обстрактного класса
# Абстрактный метод - этто метод у которог есть объявление но нет реализации

# from abc import ABC, abstractclassmethod
# from math import pi
# class Shape(ABC):
#     def __init__(self, name) -> None:
#         self.name = name
    
#     @abstractclassmethod
#     def area(self):
#         pass
    
#     @abstractclassmethod
#     def info(self):
#         pass

# class Square(Shape):
#     def __init__(self, length) -> None:
#         super().__init__('Квадрат')
#         self.length = length

#     def area(self):
#         print(self.length ** 2)

#     def info(self):
#         print(f'Я {self.name}, у меня все углы равны 90 градусам')

# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         super().__init__('Окружность')
#         self.radius = radius

#     def area(self):
#         print(pi * self.radius ** 2)

#     def info(self):
#         print(f'Я {self.name}, и я фигурв в двумерной плоскости')


# a = Square(4)
# b = Circle(4)
# for x in (a, b):
#     x.info()
#     x.area()
#     print()
#=========================================
# from abc import ABC, abstractclassmethod
# class ChessPiece(ABC):
#     #общий метод, который будут использовать все наследники этого класса
#     def take(self):
#         print('Take a chess piece')
    
#     #абстрактный мотод, котрый необходимо преопределить для каждого наследника
#     @abstractclassmethod
#     def move(self):
#         pass

# class Queen(ChessPiece):
#     def move(self):
#         print('Queen moves where she wants diagonally vertically and horizontally')
        
# class Pawn(ChessPiece):
#     def move(self):
#         print('The pawn can move dicectly to one cell')

# q = Queen()
# p = Pawn()
# q.move()
# q.take()
# print()
# p.move()
# p.take()

# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.
# import datetime
# class Phone:
#     def __init__(self, os, imei) -> None:
#         self.__os = os
#         self.__imei = imei
#         self.__batery_level = 100
#     @property
#     def battery_level(self):
#         if self.__batery_level < 0.5:
#             self.__batery_level = 0
#             raise Exception('No charge')
#         self.__batery_level -= 0.5
#         print(self.__batery_level)
#     def get_info(self):
#         if self.__batery_level < 0.5:
#             self.__batery_level = 0
#             raise Exception('No charge')
#         self.__batery_level -= 0.5
#         print(f'OS{self.__os}, EMEI: {self.__imei}')

#     def play_music(self):
        # if self.__batery_level <= 5:
        #     self.__batery_level = 0
        #     raise Exception('No charge')
        # self.__batery_level -= 5
        # print('Slushaem Murbeka Atabekova')

    # def play_video(self):
    #     if self.__batery_level <= 10:
    #         raise Exception('you cant to watch video please recharge!')
    #     self.__batery_level -= 7
    #     print('Watch toples!')

    # def charge_battery(self, sec):
    #     from time import sleep
    #     i = 1
    #     while i <= sec:
    #         sleep(1)
    #         if self.__batery_level < 100:
    #             self.__batery_level += 1
    #             if self.__batery_level > 100:
    #                 self.__batery_level = 100
    #             print(f'Idet zaryadka batarei! Vash uroven zaryada: {self.__batery_level}')

# phone = Phone('IOS 15', '177009')
# phone.get_info()
# phone.play_music()
# phone.play_music()
# phone.play_music()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.battery_level
# phone.charge_battery(20)
#1
# a = 'move to another country'
# b = [1,2,3,4]
# c = {1: 'I', 2: 'am', 3: 'programmer'}
# for i in [a, b, c]:
#     print(len(i))
#2
# class Dog:
#     def voice(self):
#         print('Гав')
# class Cat:
#     def voice(self):
#         print('Мяу')
# def to_pet(name1, name2):
#     name1.voice()
#     name2.voice()
# barsik = Cat()
# rex = Dog()
# to_pet(barsik, rex)
#3
# class Person:
#     def __init__(self, name, last_name,) -> None:
#         self.name = name
#         self.last_name = last_name
#     def get_info(self):
#         print(f'Привет, меня зовут {self.name} {self.last_name}')
# class Employee(Person):
#     def __init__(self, name, last_name, work, status) -> None:
#         super().__init__(name, last_name)
#         self.work = work
#         self.status = status
#     def get_info(self):
#         print(f'Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}')
# class Student(Person):
#     def __init__(self, name, last_name, university, course) -> None:
#         super().__init__(name, last_name)
#         self.university = university
#         self.course = course
#     def get_info(self):
#         print(f'Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе')
# def get_numan_info(func):
#     return func.get_info()

# person = Person('lolo', 'pticha')
# employee = Employee('lili', 'obilova', 'programmer', 'ready')
# student = Student('vika', 'sheli', 'oxford', 3)
# get_numan_info(person)
# get_numan_info(employee)
# get_numan_info(student)
#4
# from abc import ABC, abstractmethod
# from math import pi

# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass

# class Triangle(Shape):
#     def __init__(self, base, height) -> None:
#         self.base = base
#         self.height = height
        
#     def get_area(self):
#         return 0.5*self.base*self.height

# class  Square(Shape):
#     def __init__(self, length) -> None:
#         self.lenght = length

#     def get_area(self):
#         return self.lenght ** 2

# class   Circle(Shape):
#     def __init__(self, radius) -> None:
#         self.radius = radius

#     def get_area(self):
#         return pi * self.radius ** 2

# triangle = Triangle(10, 6)
# square = Square(12)
# circle = Circle(12)
# print(triangle.get_area()) 
# print(square.get_area()) 
# print(circle.get_area()) 
#5
# class OS:
#     def __init__(self, version) -> None:
#         self.version = version

# class Windows(OS):
#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами CTRL + C'

# class MacOS(OS):
#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами COMMAND + C'

# class Linux(OS):
#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами CTRL + SHIFT + C'
# win = Windows(12)
# mac = MacOS(13)
# lin = Linux(13)
# print(win.copy('Полиморфизм — одна из основных парадигм ООП'))
# print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах')) 
# print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))
#6
# class Language:
#     def __init__(self, level, type) -> None:
#         self.level = level
#         self.type = type
# class Python(Language):
#     def write_function(self, func_name, arg):
#         return f'def {func_name}({arg}):'
#     def create_variable(self, var_name, value):
#         if isinstance(value, str):
#             return f"{var_name} = '{value}'"
#         else:
#             return f"{var_name} = {value}"
# class JavaScript(Language):
#     def write_function(self, func_name, arg):
#         return f'function {func_name}({arg}) {{    }};'
#     def create_variable(self, var_name, value):
#         if isinstance(value, str):
#             return f"let {var_name} = '{value}';"
#         else:
#             return f"let {var_name} = {value};"

# py = Python('high-level', 'interpreted')
# js = JavaScript('high-level', 'interpreted')
# print(py.write_function('get_code', 'a')) 
# print(py.create_variable('name', 'John'))
# print(js.write_function('validate', 'form'))
# print(js.create_variable('password', 'hchjh'))
#7
# class Money:
#     def __init__(self, country, symbol) -> None:
#         self.counry = country
#         self.symbol = symbol

# class Dollar(Money):
#     rate = 84.80
#     def exchange(self, amount):
#         return f'$ {amount} равен {Dollar.rate*amount} сомам'

# class Euro(Money):
#     rate = 98.40
#     def exchange(self, amount):
#         return f'€ {amount} равен {Euro.rate*amount} сомам'
    
# dol = Dollar('Alaska', '$')
# eu = Euro('France', '€')
# print(dol.exchange(100))
# print(eu.exchange(80))
#8
# class Planet:
#     def __init__(self, orbit) -> None:
#         self.orbit = orbit
# class Mercury(Planet):
#     def get_age(self, earth_age):
#         return f'на Меркурии ваш возраст составляет {int(earth_age*365/self.orbit)} лет'
# class Venus(Planet):
#     def get_age(self, earth_age):
#         return f'на Венере ваш возраст составляет {round(earth_age*365/self.orbit*365)} дней'
# class Jupiter(Planet):
#     def get_age(self, earth_age):
#         return f'на Юпитере ваш возраст составляет {earth_age*365//self.orbit*365*24} часов'
# mer = Mercury(88)
# ven = Venus(225)
# jup = Jupiter(12)
# print(mer.get_age(20))
# print(ven.get_age(20))
# print(jup.get_age(20))

