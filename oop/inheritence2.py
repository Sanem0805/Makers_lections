# множественное наследование - это когда клаа наследуеться от двух или более классов
# class Auto:
#     def play_music_station(self):
#         print('Music is playing')
    
#     def ride(self):
#         print("We're riding on the ground")

# class Plane:
#     def play_music_station(self):
#         print('Listening Jw broadcasting')

#     def fly(self):
#         print('We\'re flying')

# class FutureAuto(Auto, Plane):
#     pass

# obj = FutureAuto()
# obj.ride()
# obj.fly()
# obj.play_music_station()

# class A:
#     def print_a(self):
#         print('A')

# class B:
#     def print_b(self):
#         print('B')

# class C:
#     def print_c(self):
#         print('C')

# class MyClass(A, B, C):
#     pass

# obj = MyClass()
# obj.print_a()
# obj.print_b()
# obj.print_c()

# print(MyClass.mro())

# class Test:
#     pass
# a = Test()
# print(Test.mro())
# print(dir(a))

# b = object()
# print(dir(b))

# # Проблема ромба(решена с помашью mro)
# MRO(Method Resolution Order) - механизм для коректного поиска родительских методов. Был создан для решения проблемы ромба,
# которая появилась после введения класса object в пайтон. Поиск идет таким образом что если у родительских классов один общий предок то идет поиск в ширину



# print(dir(object))
# class Zero:
#     # def say(self):
#     #     print('class Zero')
#     pass
# class First:
#     # def say(self):
#     #     print('class First')
#     pass

# class Second:
#     # def say(self):
#     #     print('class Second')
#     pass

# class Myclass(First, Second):
#     def say(self):
#         super().say()
#         print('My Class')

# obj = Myclass()
# obj.say()
# print(Myclass.mro())

# Проблема перeкрестного наследования 

# class Y:
#     pass

# class X:
#     pass

# class A(X,Y):
#     pass

# class B(Y,X):
#     pass

# class MyMRO(type):
#     def mro(cls) -> list[type]:
#         return [cls, A, B, X, Y, object]

# class Myclass(A,B, metaclass=MyMRO):
#     pass
# obj = Myclass()
# print(Myclass.mro())

#1
# class Auto:
#     def ride(self):
#         print('Riding on a ground')

# class Boat:
#     def swim(self):
#         print('Floating on water')

# class Amphibian(Auto, Boat):
#     pass

# obj = Amphibian() 
# obj.ride() 
# obj.swim() 
#2 
# class RadioMixin:
#     def play_music(self, name):
#         print(f'Песня называется {name}')
        
# class Auto(RadioMixin):
#     pass
# class Boat(RadioMixin):
#     pass
# class Amphibian(Auto, Boat):
#     pass
# auto = Auto()
# boat = Boat()
# obj = Amphibian()
# auto.play_music('...')
# boat.play_music('!!!!')
# obj.play_music('hhhhh')
#3
# import datetime
# class Clock:
#     def current_time(self):
#         time_now = datetime.datetime.now().time().strftime('%H:%M:%S')
#         print(time_now)

# class Alarm:
#     def on(self):
#         print('Будильник включен')

#     def off(self):
#         print('Будильник выключен')

# class AlarmClock(Clock, Alarm):
#     def alarm_on(self):
#         super().on()

# clock = AlarmClock()
# clock.current_time()
# clock.alarm_on() 
#4
# from abc import ABC, abstractmethod
# class Coder(ABC):
#     count_code_time = 0
#     @abstractmethod
#     def get_info(self):
#         pass
#     @abstractmethod
#     def coding(self):
#         pass
# class Backend(Coder):
#     def __init__(self, experience, languages_backend) -> None:
#         self. experience = experience
#         self.languages_backend = languages_backend
#     def get_info(self):
#         return f'{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'
#     def coding(self, hours):
#         self.count_code_time = self.count_code_time + hours
#         return self.count_code_time
# class Frontend(Coder):
#     def __init__(self, experience, languages_frontend) -> None:
#         self. experience = experience
#         self.languages_frontend = languages_frontend
#     def get_info(self):
#         return f'{self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'
#     def coding(self, hours):
#         self.count_code_time = self.count_code_time + hours
#         return self.count_code_time
# class Fullstack(Backend, Frontend):
#     pass
# a = Backend('Junior', 'Python')
# b = Frontend('Middle', 'Javascript')
# c = Fullstack('Senior', 'Python and JS')
# a.coding(12) 
# b.coding(45) 
# c.coding(17) 
# print(a.get_info()) 
# print(b.get_info()) 
# print(c.get_info()) 

#5
# class Square:
#     def __init__(self, side) -> None:
#              self.side = side

#     def get_area(self):
#         return self.side * self.side

# class Triangle:
#     def __init__(self, height, base) -> None:
#           self.height = height
#           self.base = base
#     def get_area(self):
#         return  int(0.5*self.base*self.height)

# class Pyramid(Triangle, Square):
#     def get_volume(self):
#         return int(1/3*self.base**2*self.height)

# obj = Square(3)
# print(obj.get_area())

# obj2 = Triangle(3,5)
# print(obj2.get_area())

# obj3 = Pyramid(10,10)
# print(obj3.get_volume())

#6
# class CreateMixin:
#     def create(self, key, todo):
#         if key in ToDo.todos.keys():
#             return 'Задача под таким ключом уже существует'
#         ToDo.todos[key] = todo
#         return ToDo.todos

# class DeleteMixin:
#     def delete(self, key):
#         delete_ = ToDo.todos.pop(key, 'нет такого ключа')
#         if 'нет такого ключа' == delete_:
#             return delete_
#         return delete_

# class UpdateMixin:
#     def update(self, key, new_value):
#         ToDo.todos[key] = new_value
#         return self.todos

# class ReadMixin:
#     def read(self):
#         res = [x for x in self.todos.items()]
#         return sorted(res)
        

# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     todos = {}
#     def set_deadline(self, deadline):
#         import datetime
#         deadline = deadline.split('/')
#         deadline = list(map(int, deadline))
#         deadline = datetime.date(deadline[2], deadline[1], deadline[0])
#         time_ = datetime.date.today()
#         return (deadline - time_).days
        
# task = ToDo() 
# print(task.set_deadline('31/12/2022'))
# print(task.create(1, 'todo'))
# print(task.delete(3))
# print(task.update(1, 'todo'))
# print(task.read())
# print(task.create(1, 'Do housework'))
# print(task.create(1, 'Do housework'))
# print(task.create(2, 'Go for a walk'))
# print(task.update(1, 'Do homework'))
# print(task.delete(2))
# print(task.read())
# print(task.set_deadline('31/12/2021'))
# решение Султана
# class CreateMixin:
#     def create(self, todo, key):
#         if key in self.todos:
#             return 'Задача под таким ключом уже существует'
#         else:
#             self.todos[key] = todo
#             return self.todos

# class DeleteMixin:
#     def delete(self, key):
#         pop_elem = self.todos.pop(key)
#         return pop_elem

# class UpdateMixin:
#     def update(self, key, new_value):
#         self.todos[key] = new_value
#         return self.todos

# class ReadMixin:
#     def read(self):
#         return sorted(self.todos.items())

# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
    # todos = {}
    # def set_deadline(self, deadline):
        # import datetime 
        # time_ = datetime.datetime.now().date().strftime('%d/%m/%Y')
        # current = datetime.datetime.strptime(time_, '%d/%m/%Y')
        # date = datetime.datetime.strptime(deadline, '%d/%m/%Y')
        # res = date - current
        # return res.days

# task = ToDo() 
# print(task.set_deadline('31/12/2022'))
# print(task.create(1, 'todo'))
# print(task.delete(3))
# print(task.update(1, 'todo'))
# print(task.read())
# print(task.create(1, 'Do housework'))
# print(task.create(1, 'Do housework'))
# print(task.create(2, 'Go for a walk'))
# print(task.update(1, 'Do homework'))
# print(task.delete(2))
# print(task.read())
# print(task.set_deadline('31/12/2021'))

#7
# class ExtensionMixin:
#     def add_extension(self, title):
#         self.extension(title)
#         print(f'Добавлено новое расширение{title} для игры {self.name}')

#     def remove_extension(self, title):
#         if title in self.add_extension:
#             self.extension.remove(title)
#             return f'{title} Core был отключен от {self.name}'
#         else:
#             return 'Такого расширения нет в списке.'

# class Game(ExtensionMixin):
#     def __init__(self, type, name) -> None:
#         self.type = type
#         self.name = name
#         self.extension = []

#     def get_description(self, game_name):
#         self.name = game_name
#         return f'{self.name} это инди-игра в жанре песочницы с элементами выживания и открытым миром.'
#     def get_extensions(self):
#         if  len(self.extension) == 0:
#             return 'Нет подключенных расширений'
#         else:
#             return self.extension

# obj = Game('prog','Minecraft')
# print(obj.get_extensions())
# # print(obj.add_extension('Multiverse-Core'))

#8
# class WalkMixin:
#     def walk(self):
#         print("я могу ходить")
# class FlyMixin:
#     def fly(self):
#         print("я могу летать")
# class SwimMixin:
#     def swim(self):
#         print("я могу плавать")
# class Human(WalkMixin, SwimMixin):
#     pass
# class Fish(SwimMixin):
#     pass
# class Exocoetidae(FlyMixin, SwimMixin):
#     pass
# class Duck(WalkMixin, FlyMixin, SwimMixin):
#     pass
# man = Human()
# man.swim()
# man.walk()
# fish = Fish()
# fish.swim()
# dragon = Exocoetidae()
# dragon.swim()
# dragon.fly()
# duck = Duck()
# duck.swim()
# duck.fly()
# duck.walk()
# class CreatMixin:
#     def create(self, key, todo):
#         if key in self.todos.keys():
#             return 'Задача под таким ключём уже существует'
#         self.todos[key] = todo
#         return self.todos
# class DelateMixin:
#     def delate(self, key):
#         delate_ = self.todos.pop(key, 'нет такого ключа')
#         if 'нет такого ключа' == delate_:
#             return delate_
#         return delate_

# class UpdateMixin:
#     def update(self, key, new_value):
#         self.todos[key] = new_value
#         return self.todos

# class ReadMixin:
#     def read(self):
#         res = [i for i in self.todos.items()]
#         return res

# class ToDo(CreatMixin, DelateMixin, UpdateMixin, ReadMixin):
#     todos = {}
#     def set_deadline(self, deadline):
#         import datetime
#         time_ = datetime.datetime.now().strftime('%d/%m/%Y')
#         deadline = deadline.split('/')
#         time_ = list(map(int, deadline))
#         time_ = sum(time_[0], time_[1]*30, time_[2]*365)
#         deadline = datetime.date(deadline[2], deadline[1], deadline[0])
        # time_ = datetime.today()
#         return (deadline - time_).days
# task = ToDo() 
# print(task.set_deadline('31/12/2022'))
# print(task.create(1, 'todo'))
# print(task.delete(3))
# print(task.update(1, 'todo'))
# print(task.read())
# print(task.create(1, 'Do housework'))
# print(task.create(1, 'Do housework'))
# print(task.create(2, 'Go for a walk'))
# print(task.update(1, 'Do homework'))
# print(task.delete(2))
# print(task.read())
# print(task.set_deadline('31/12/2021'))

