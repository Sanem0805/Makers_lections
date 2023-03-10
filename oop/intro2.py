# class Human:
#     age = 0
#     def __init__(self, name, last_name, weight, nationality):
#         self.name = name + ' ' + last_name
#         self.weight = weight
#         self.nation = nationality
#     def birthday(self):
#         import random
#         print(f'\nHappy birthday, {self.name}!!!')
#         self.age += 1 #self.age = self.age + 1
#         self.weight += random.randint(3, 6)

# human1 = Human('John', 'Snow', 3.300, 'American')
# human2 = Human('Abu', 'Bakr', 3.8, 'Arabic')

# print(human1.name, human1.age, human1.weight, human1.nation)
# print(human2.name, human2.age, human2.weight, human2.nation)

# print('After 1 year')
# human1.birthday()
# human2.birthday()
# print(human1.name, human1.age, human1.weight, human1.nation)
# print(human2.name, human2.age, human2.weight, human2.nation)

# human1.birthday()
# human2.birthday()
# print(human1.name, human1.age, human1.weight, human1.nation)
# print(human2.name, human2.age, human2.weight, human2.nation)

# human1.birthday()
# human2.birthday()
# print(human1.name, human1.age, human1.weight, human1.nation)
# print(human2.name, human2.age, human2.weight, human2.nation)

# class Student:
#     univer = 'MIT'
#     def __init__(self, name, last):
#         self.name = f'{name} + {last}'
#         self.books = []
#         self.languages = {}
#         self.knowledge = 0
#         self.is_ready_to_work = False

#     def add_ponts(self, points):
#         self.knowledge += points
#         if self.knowledge > 500:
#             self.is_ready_to_work = True
#             print(f'{self.name} is ready to work!!')

#     def read_book(self, book):
#         self.books.append(book)
#         self.add_ponts(50)
    
#     def do_lab_work(self):
#         self.add_ponts(50)

#     def do_project(self):
#         self.add_ponts(50)

#     def learn_new_language(self, language, points):
#         if not points in range(70, 101):
#             raise Exception('Invalid points')
#         self.languages[language] = points
#         self.add_ponts(points)

# st1 = Student('John', 'Snow')
# st2 = Student('Jamie', 'Lanister')
# print(st1.name)
# print(st2.name)
# print(f'Befor study {st1.name}', st1.books, st1.languages, st1.knowledge)
# print(f'Ready to work: {st1.is_ready_to_work}')

# st1. read_book('Game of thrones')
# st1.read_book('Martin Iden')
# st1.read_book('Algorizm and data structures')
# st1.read_book('Eugene Onegin')

# st1.do_lab_work()
# st1.do_lab_work()
# st1.do_project()
# st1.learn_new_language('Python', 90)
# st1.learn_new_language('C++', 75)

# print(f'After study {st1.name}', st1.books, st1.languages, st1.knowledge)
# print(f'Ready to work: {st1.is_ready_to_work}')

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def __str__(self) -> str:
#         return f'{self.brand} -> {self.model}'


# obj = Car('BMW', '7 series')
# obj2 = Car('Mercedez-Benz', 'w140')
# obj3 = Car('Kia', 'K8')

# print(obj, '!')
# print(obj2, '!!')
# print(obj3, '!!!')


# class Soda:
#     def __init__(self, ingredient=None):
#         if isinstance(self.ingredient, str):# type(ingredient == str)
#             self.ingredient = ingredient
#         else:
#             self.ingredient = None

#     def show_my_drink(self):
#         if self.ingredient:
#             print(f'Gazirovka iz {self.ingredient}')
#         else:
#             print(f'Normal gazirovka')
# a = Soda('Malina')
# a.show_my_drink()

# b = Soda()
# b.show_my_drink()

# class A:
#     pass

# a = A()
# b = 5
# print(isinstance(a, A))
# print(isinstance(b, A))
# print(isinstance(a, int))
# print(isinstance('123', int))


#-------------------------
# [5, 4, 8]
# class TriangleChecker:
#     def __init__(self, sides: list):
#         self.sides = sides

#     def __str__(self) -> str:
#         if not all(isinstance(x, (int, float)) for x in self.sides):
#             return 'нельзя построить треугольник! Так как все стороны должны быть числами' 
#         if any(x<=0 for x in self.sides):
#             return 'Нельзя построить треугольник! Так как все стороны должны быть больше нуля!'
#         self.sides.sort()
#         if self.sides[0] + self.sides[1] <= self.sides[-1]:
#             return 'Нельзя построить треугольник! Taк как сумма двух сторон должна быть больше самой длинной стороны!'
#         return 'Мы можем посроить троеугольник'

        

# t1 = TriangleChecker([4, 5, 6])
# print(t1)
