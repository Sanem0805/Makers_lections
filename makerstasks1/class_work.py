"""
1) Есть глобальная переменная, которая обозначает размер самой главной первой матрешки. Напишите функцию, в которой к размеру главной матрешки прибавляется размер второй матрешки, который определен в этой функции. То же самое сделайте и с третьей функцией внутри второй. Верните результат сложения.
"""
# mat1 = 30   # mat1 = 50
# def size_mat1():
#   global mat1
#   mat2 = 20
#   mat1 += mat2
#   def size_mat2():
#     global mat1
#     mat3 = 5
#     mat1 += mat3
#   size_mat2()
# size_mat1()  
# print(mat1)
"""
2) Есть глобальная переменная, которая содержит пустой список. Вам необходимо написать функции, одна из которых add() - добавляет в этот список имена, которые вводит пользователь. А другая функция remove() - удаляет эти имена из списка по индексу, который вводит пользователь. Вызовите функции в рандомном порядке 10 раз и в конце выведите список.
"""
# from random import choice
# list_ = []
# def add():
#   global list_
#   list_ = (input('Enter your name: ')).split(',')
#   return 1
#   def remove():
#     global list_
#     if not len(list_): return
#     list_.pop(0)
#     return 1
#   remove()
  
# i = 0
# while i < 10:
#   add()
#   i += 1
#   break
# print(list_)


  