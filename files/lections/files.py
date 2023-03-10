# Работа над файлами
# Каретка - Указатель - Курсор
# open(<путь до файла>)

# file = open('/home/sanzhar/Desktop/py.26/files/files.py')# Абсолютный путь
# file = open('files.py')# относительный путь
# ~ working -> Desktop/py.26/files/files.py
# py.26 -> files/files.py

# file = open('files.py')
# data = file.read()
# print(type(data))
# file.close()

#Режим работы с файлами
# 1. r/r+ (read)
# 2. w/w+ (write)
# 3. a/a+ (append)
# b, x

# file = open('test.txt', 'r')
# print(file.read())
# file.close()

# file = open('test.txt', 'r')
# data = file.readlines()#['Hello world!\n', 'My name is John Snow\n', "I'm North King!\n"]
# print(data)
# print(len(data[0]))#13
# file.close()

# file = open('test.txt', 'r')
# print(file.readline())
# print('!!!!!!!!!!!')
# print(file.read())#My name is John Snow
# file.close()      #I'm North King! 

#контекстный менеджер
# with open('test.txt', 'r') as file: # file = open('test.txt)
#     data = file.read()
#     print(data)
#     print(file, 'inside')

# print(file, 'outside')

# with open('test.txt', 'r') as f:
#     print(f.tell())
#     data = f.read(20)
#     print(data)
#     print(f.read())
# file.tell() - возвращает индекс где находиться указатель (курсор)
# file.seek() - перемещает курсор на индекс котрый вы передали

# with open('test.txt', 'r') as file:
    # print(file.readline())
    # file.seek(0)
    # print(file.readline())
    # file.seek(0)
    # a = file.read()
    # print((file.readline()))
    # print(file.readline(-1))

# print(a)

# with open('test.txt', 'w') as file:
    # file.write('Pervaya stroka!\n')
    # file.write('He is bastard of Ned Stark!\n')
    # file.write('This is lesson about files!')
    # file.seek(0)
    # data = ['Pervaya strochka!\n', 'He is bastard of Ned Stark!\n', 'This is lesson about files!']
    # file.writelines(data)

# with open('test.txt', 'a+') as file:
#     file.write('\nJohn Snow is North King!')
#     file.write('\nYou know nothing John snow!')
#     file.seek(0)
#     print(file.read())

#=================================================

# try:
#     from PIL import Image
# except ImportError:
#     import Image
# import pytesseract
# import re

# def get_imei_code(image):
#     string = pytesseract.image_to_string(image)
#     # print(string)
#     list_of_imai = re.findall(r'IMEI\d.\s\d+', string)
#     print(list_of_imai)

#     with open('get_imei_code.txt', 'w') as file:
#         file.writelines(f'{x}\n' for x in list_of_imai)
#         # for x in list_of_imai:
#         #     file.write(f'{x}\n')

# image = 'imei.jpg'
# get_imei_code(image)

# with open('test1.txt', 'w+') as file:
#     for line in file.read(9):
#         print(line)

#1
# file = open('test1.txt')
# for i in file.readlines(9):
#     print(i)
# file.close()

#2
# with open('test1.txt', 'r') as file:
#     for l in file.readlines():
#         print(l)
# 3
# with open('task3.txt', 'a+') as file:
#     file.write('0*1*2*3*4*5*6*7*8*9*') 
#     file.seek(0)
#     print(file.read())
#4
# with open('task4.txt', 'r') as file:
#     print(len(file.readlines()))
 
# with open('output.txt', 'w') as w:
#     print(sorted(hm), file=w)
#5
# with open('test1.txt', 'r') as f:
#     list_ = []
#     ful = f.read()
#     for i in ful.split():
#         list_.append(int(i))
# with open('test2.txt', 'x') as fw:
#     fw.write(f'{min(list_)}-{max(list_)}')
# # оба варианта верны
# with open('/Users/sanem0805/Desktop/pykers/files/lections/test1.txt', 'r') as f:
#     list_ = f.readlines()
#     list_ = [line.replace('\n', '')for line in list_]
#     list1 = []
#     for i in list_:
#        i = int(i)
#        list1.append(i)
#        a = min(list1)
#        b = max(list1)
# with open('/Users/sanem0805/Desktop/pykers/files/lections/test3.txt', 'w') as fw:
#     fw.write(f'{a}-{b}')
  
#6
# def read_last(lines, filename):
#     with open(filename) as file:
#         list_ = file.readlines()
#         if lines < len(list_):
#             i = 0
#             reversed_list_ = list_[::-1]
#             while i<lines:
#                 print(reversed_list_[i].replace('\n', ''))
#                 i+=1
#         else:
#             list_.reverse()
#             for i in list_:
#                 print(i.replace('\n', ''))
           

# read_last(9, 'article.txt')


#7
# def longest_words(filename):
#     with open(filename) as file:
#         long_list = []
#         list_ = file.readlines()

#         for i in list_:
#             if len(i) == 6:
#                 long_list.append(i.replace('\n', ''))

#         if len(long_list) == 1: 
#             return long_list[0]   
            
#         return long_list
        
# print(longest_words('test1.txt'))


# def longest_words(filename:str):
#     with open(filename,'r') as file:
#         listData=file.readlines()
#         listData1=[]
#         for x in listData:
#             if '\n' in x:
#                 x=x.replace('\n','')
#             else:
#                 pass
#             if ' ' in x:
#                 var=x.split()
#                 listData1.extend(var)
#             else:
#                 listData1.append(x)
#         maximum=[]
#         for j in listData1:
#             if len(j)==len(max(listData1,key=len)):
#                 maximum.append(j)
#             else:
#                 pass
#         if len(maximum)==1:
#             print(maximum[0])
#         else:
#             print(maximum)
# longest_words('article.txt')

#class work работа с файлами
# with open('/Users/sanem0805/Desktop/pykers/files/lections/numbers.txt', 'w') as file:
#   list1 = []
#   for i in range(1, 21):
#     file.write(str(i))
#     list1.append(i)
#     print(i)
with open('/Users/sanem0805/Desktop/pykers/files/lections/squares.txt', 'a') as f1:
    list2 = []
    for i in list1:
      i = int(i)
      i = i ** 2
      f1.write(str(i))
      list2.append(i)
      prπint(i)
        


# list1 = [
#     {"id": 1, "title": "iphone", "price": 700, "rating": 4.8},
#     {"id": 2, "title": "asus", "price": 1300, "rating": 3.9}, 
#     {"id": 3, "title": "macbook pro", "price": 1500, "rating": 4.9}, 
# {"id": 4, "title": "samsung", "price": 150, "rating": 5.0}
# # ]

