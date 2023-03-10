"""
1) Напишите программу по следующему описанию. Есть класс "Снайпер". От него создаются два экземпляра.
Каждому устанавливается здоровье в 100 очков. 
В случайном порядке они стреляют друг в друга. Тот, кто стреляет, здоровья не теряет. У того, в кого стреляют,
оно уменьшается на 20 очков от одного выстрела.
После каждого выстрела надо выводить сообщение, какой снайпер атаковал, и сколько у противника осталось здоровья.
Как только у кого-то заканчивается ресурс здоровья, 
программа завершается сообщением о том, кто одержал победу.
"""
# писать код здесь
"""
2) Напишите программу по следующему описанию. Есть класс Hogwarts. В нем определены следующие атрибуты-факультеты: 
Gryffindor, Ravenclaw, Hufflepuff, Slytherin. От класса Hogwarts создаются объекты-студенты.
При создании студентов необходимо указать баллы за их следующие качества: courage (храбрость), intelligence (интеллект), 
justice (справедливость), ambition (амбиции).
У студентов не могут быть качества одинакового уровня. В зависимости от того, какое качество студента преобладает, 
метод sorting_hat будет распределять студента в один из факультетов и выдавать в какой факультет поступил студент.
Примечание: 
Преобладает courage -> Gryffindor
Преобладает intelligence -> Ravenclaw
Преобладает justice -> Hufflepuff
Преобладает ambition -> Slytherin
"""

# import random

# class Sniper:
    
#     def __init__(self, name):
#         self.name = name
#         self.health = 100
        
#     def shoot(self, sniper):
#         self.health -= 20

# sniper1 = Sniper(name='Ben')
# sniper2 = Sniper(name='Tom')

# choices = (sniper1, sniper2)
# while True:
#     shooter = random.choice(choices)
#     if shooter == sniper1:
#         shot = sniper2
#     else:
#         shot = sniper1

#     shooter.shoot(shot)
#     print(f'Shooter {shooter.name} is shooting, {shot.name} has {shot.health} health points')

#     if sniper1.health == 0:
#         print(f'{sniper1.name} is dead.{sniper2.name} won!!!')
#         break
#     elif sniper2.health == 0:
#         print(f'{sniper2.name} is dead. {sniper1.name} won!!!')
#         break
#     else: 
#         continue
# 1. Декараторы lab
# def call_function(func):
#     def wrapper():
#         print(f"Вызываю функцию {func.__name__}")
#         func()
#         print(f"Вызов функции {func.__name__} прошёл успешно")
#         return wrapper
# @call_function
# def first():
#     print("hello world")
#     return 'hello world'
# first()
2. декараторы лаб
import datetime
def func_start_time()