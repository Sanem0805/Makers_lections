# Инкапсулицая

# 1 Связь данных с методами которые должны управлять этими аттрибутами
# 2 Механизм языка который позволяет ограничить доступ к оперделенымм компонентам класса

# Инкапсуляция  как связь

# class Phone:
#     number = '+996700700700'

#     def print_number(self):
#         print(f'Мой номер: {self.number}')

# my_phone = Phone()
# my_phone.print_number() #Мой номер: +996700700700

#Инкапсуляция как управление доступом
#3 уровня доступа в питоне
# 1 публичный(public) - number, print_number
# 2 Защищенный(_protected,parent/child) - _number
# 3 приватный(__privete, только в текущем) - __number

# class Car:
#     _country = 'Gremany'
#     def __init__(self) -> None:
#         self.marka = 'Mercedes-Benz'# public
#         self._model = 'w140'#protected
#         self.__motor = 'ABC'# private

# obj = Car()
# print(obj.marka)
# print(obj._country)
# print(obj._model)
# print(obj._Car__motor)

# class Phone:
#     username = 'John Snow'
#     _caller = 'Jamie Lanister'
#     __count_of_calls = 15

#     def call(self):
#         print(f'{self._caller} звонит')

#     def __incriment_of_calls(self):
#         self.__count_of_calls += 1

#     def turn_on(self):
#         print(f'{self.username} взял трубку')
#         self.__incriment_of_calls()

#     def get_count(self):
#         print(self.__count_of_calls)

# obj = Phone()
# obj.get_count()
# obj.call()
# obj.turn_on()

#getter & setter
# они используються для получения и установки значений в защищищённые аттрибуты чтобы избежать прямого доступа к защищенному аттрибуту и ещё с помошью сеттеров и геттеров можно добавлять логику проверки при получении дынных

# class Person:
#     def __init__(self, name):
#         self.name = name 
#         self. age = 0

#     def display_info(self):
#         print(f'My name is {self.name}, I\'m {self.age} yers old')

# john = Person('John')
# john.display_info()
# john.name = None
# john.age = -18
# john.display_info()

# class Person:
#     def __init__(self, a):
#         self.__name = a 
#         self. __age = 0

#     def display_info(self):
#         print(f'My name is {self.__name}, I\'m {self.__age} yers old')

#         #getter
#     def get_name(self): return self.__name

#     #setter
#     def set_name(self, name):
#         if not isinstance(name, str):
#             print('Invalid value')
#         else:
#             self.__name = name

#     def get_age(self): return self.age

#     def set_age(self, age):
#         if not isinstance(age, int) or not 0 <= age < 150:
#             print('Invalid value for age')
#         else:
#             self.__age = age

# john = Person('John')
# john.display_info()
# john.set_name(None)
# john.set_age(-18)
# john.display_info()
# john.set_name('Jamie')
# john.set_age(24)
# john.display_info()


# class Russia:
#     __name = 'Russian Federation'
#     __population = 0
#     def get_population(self): return self.__population

#     def set_population(self, num):
#         if not isinstance(num,int) or num < 0:
#             print('Invalid value population')
#         else:
#             self.__population = num

#     def get_name(self): return self.__name

#     def display_info(self):
#         print(f'Population of {self.get_name()}: {self.get_population()}')

# obj = Russia()
# obj.set_population(143_000_000)
# obj.display_info()

#-----------------------------
# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.__age = 0

#     def _age_increement(self):
#         self.__age += 1

#     def birthday(self):
#         print(f'{self.name}s birthday')
#         self._age_increement()

#     def display_info(self):
#         print(self.name, self.__age)

# obj = Person('John')
# obj.display_info()
# obj.birthday()
# obj.display_info()

#1
# class A:
#     def public(self):
#         return'Public method'
#     def _protected(self):
#         return'Protected method'
#     def __private(self):
#         return'Private method'
#     def get_protected(self):
#         self._protected
#     def get_private(self):
#         self.__private
# obj1 = A()
# print(obj1.public())
# print(obj1.get_protected())
# print(obj1.get_private())
#2
# class A:
#     def method1(self):
#         print('Hello World')
# class B(A):
#     pass
# b1 = B()
# b1.method1()
#3
# class Car:
#     __speed = 0
#     def set_speed(self, new):
#         self.__speed = new
#         return self.__speed
#     def show_speed(self):
#         return self.__speed
    
# car1 = Car() 
# print(car1.show_speed()) 
# car1.set_speed(20) 
# print(car1.show_speed()) 
#4
# class Car:
#     __speed=0
#     @property
#     def speed(self):
#         return self.__speed
#     @speed.setter
#     def speed(self,new): 
#         self.__speed=new
#         return self.__speed
# car1 = Car()
# print(car1.speed)
# car1.speed = 20
# print(car1.speed)
#5
# class Person:
#     name = "John"
#     _phone_number = "+996 557 55 17 57"
#     __card_number = "9999 9999 9999 9999"
    
#     @property
#     def number(self):
#         return self.__card_number

# john = Person()
# print(john.name)
# print(john._phone_number)
# print(john.number)
#6
# class Person:
#     def __init__(self, name, phone_number, card_number) -> None:
#         self.name = name
#         self._phone_number = phone_number
#         self.__card_number = card_number
#     @property
#     def number(self):
#         return self.__card_number

# john = Person("John", "+996 557 55 17 57", "9999 9999 9999 9999")
# print(john.name)
# print(john._phone_number)
# print(john.number)
#7
# class Person:
#     name = "John"
#     _phone_number = "+996 557 55 17 57"
#     __card_number = "9999 9999 9999 9999"

#     def get_number(self):
#         return self.__card_number
 
#     def set_number(self):
#         self.__card_number = None
#         return self.__card_number
    
# john = Person()
# john.name = None
# john._phone_number = None
# print(john.name)
# print(john._phone_number)
# print(john.set_number())
#8
# class Person:
#     def __init__(self, name, phone_number, card_number) -> None:
#         self.name = self.__validate_name(name)
#         self._phone_number = phone_number
#         self.__card_number = card_number

#     def __validate_name(self, name):
#         if len(name) < 2:
#             return 'John'
#         else:
#             return name.title()
            
#     def get_number(self):
#         return self.__card_number

# sam = Person("SAM", "+996 557 55 17 57", "9999 9999 9999 9999")
# print(f'{sam.name}\n{sam._phone_number}\n{sam.get_number()}')
#9
# class Person:
#     def __init__(self, name, phone_number, card_number):
#         self.name = name
#         self._phone_number = self._validate_phone_number(phone_number)
#         self.__card_number = self.__validate_card_number(card_number)

#     def _validate_phone_number(self, phone_number):
#         if isinstance(phone_number, int):
#             if str(phone_number).startswith('996'):
#                 return phone_number
#         return None

#     def __validate_card_number(self, card_number):
#         if isinstance(card_number, int):
#             if len(str(card_number)) == 16:
#                 return card_number
#         return None

# tolik = Person('Tolik', '996 777 15 97 14', '9999 9999 9999 9999')

# print(tolik.name)
# print(tolik._phone_number)
# print(tolik._Person__card_number)

#10
# class Game:
#     __level = 0
#     def __init__(self, name) -> None:
#         self.name = name
#     def play(self, hours):
#         if hours > 2:
#             self.__level += 1
#     def get_level(self):
#         return self.__level
# game = Game('Leyla')
# print(game._Game__level)
# game.play(2)
# game.play(3)
# print(game.get_level())
#11
# class Game:
#     __level = 0
#     def __init__(self, name) -> None:
#         self.name = self.__validate_name(name)
#     def set_level(self, level):
#         if self.name == 'Tolik':
#             self.__level = level
#             return self.__level 
#         else:
#             print(f'"{self.name}" ты не Tolik!')
#     def __validate_name(self, name):
#         return name.title()

# game = Game('Raychel')
# game.set_level(5)
# print(game._Game__level)
# game2 = Game('TOLIK')
# game2.set_level(5)
# print(game2._Game__level)
#12
# class Game:
#     __level = 0
#     def __init__(self,name) -> None:
#         self.name = name
#     def get_level(self): return self.__level
#     def set_level(self, num):
#         self.__level = num
#         return num
# game = Game('Lili')
# print(game._Game__level)
# game.set_level(10)
# print(game._Game__level)
#13
# class Game:
#     __level = 0
#     @property
#     def level(self):
#         return self.__level
# game = Game()
# print(game.level)
#14
# class Game:
#     __level = 0
#     @property
#     def level(self):
#         return self.__level
#     @level.setter
#     def level(self, num):
#         self.__level = num
#         return self.__level
# game = Game()
# print(game.level)
# game.level = 10
# print(game.level)
#16
# class Person:
#     def __init__(self) -> None:
#         self.__name = None
#         self.__last_name = None
#         self.__age = None
#         self.__email = None
#     def get_name(self):
#         return self.__name
#     def set_name(self, new_name):
#         self.__name = new_name
#     def get_last_name(self):
#         return self.__last_name
#     def set_last_name(self, new_last_name):
#         self.__last_name = new_last_name
#     def get_age(self):
#         return self.__age
#     def set_age(self, new_age):
#         self.__age = new_age
#     def get_email(self):
#         return self.__email
#     def set_email(self, new_email):
#         self.__email = new_email
# john = Person()
# print(john.get_name())
# print(john.get_last_name())
# print(john.get_age())
# print(john.get_email())
# john.set_name('John')
# john.set_last_name('Snow')
# john.set_age(30)
# john.set_email('johnsnow@gmail.com')
# print(john.get_name())
# print(john.get_last_name())
# print(john.get_age())
# print(john.get_email())
#16
# class Person:
#     def __init__(self):
#         self.__name = None
#         self.__last_name = None
#         self.__age = None
#         self.__email = None

#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, name):
#         self.__name = name

#     @property
#     def last_name(self):
#         return self.__last_name

#     @last_name.setter
#     def last_name(self, last_name):
#         self.__last_name = last_name

#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self, age):
#         self.__age = age

#     @property
#     def email(self):
#         return self.__email

#     @email.setter
#     def email(self, email):
#         self.__email = email
# john = Person()
# print(john.name) # None
# print(john.last_name) # None
# print(john.age) # None
# print(john.email) # None
# john.name = 'John'
# john.last_name = 'Snow'
# john.age = 30
# john.email = 'johnsnow@gmail.com'
# print(john.name) # John
# print(john.last_name) # Snow
# print(john.age) # 30
# print(john.email) # johnsnow@gmail.com

#17
# class Dad:
#     name = 'John'
#     _last_name = 'Snow'
#     __age = 40
# class Me(Dad):
#     name = 'Sam'
#     __age = 10
#     def about_me(self):
#         print(f'My name is {self.name} {Dad._last_name} and I am {self.__age} years old')
#     def about_my_father(self):
#         print(f'My father is {Dad.name} {Dad._last_name}')
# me = Me()
# me.about_me()
# me.about_my_father()

# class Dad:
#     name = 'John'
#     _last_name = 'Snow'
#     __age = 40

# class Me(Dad):
#     name = 'Sam'
#     def about_me(self):
#         print("My name is {} {} and I am {} years old".format(self.name, self._last_name, self._Me__age))
#     __age = 10

#     def about_my_father(self):
#         print("My father is {} {}".format(Dad.name, self._last_name))

# me = Me()
# me.about_me()
# me.about_my_father()
