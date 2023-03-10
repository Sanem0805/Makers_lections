# Типы Данных
# 'Строки'_- набор последвательных символов коы мы испльзуем для хранения и представления текствой информаци

#name = "John Snow"
'       02345678'
          # J = 0 
          # o = 1
          # h = 2
          # n = 3
          #
#print(name[0])
'============= Срезы ============'
'Срезы по индексам - это когда мы получаем определённую часть строки при помощи индексов'
'Cрезы[start: end: step]'
'start - начало среза начальый индкс п умолчаню стоит 0 индекс'
'end - конец среза конечный идекс который не включителен по умолчанию берет о конца'
'step - ша среза который указывает через склько элеетов прохдься по млчанию'
# name = 'John Snow Man'
# snow_1= name[5:9] #Snow
# snow_2= name[5:]  #Snow Man, end указали поэтому он не возьметокоца
# print(snow_1)
# print(snow_2)

# john_1 = name[0:4]
# john_2 = name[0:]

# name = 'John snow man'
# step_2 = name[0:3:13:2]
# step_3 = name[0:3:13:3]
# print(step_2[0:13:2]) #jOhN SnOwAn -> jh nwmn
# print(step_3[0:13;3]) #jonsnow man -. jnn n

# name = 'John Snow Man'
# reversed_name = name[: :-1] #
# print(reversed_name)#na wonS nhoJ

# name = 'John Snow Man'
# reversed_name_naM = name[12:9:-1] #naM
# reversed_name_wonS = name[8:4:-1] #wonS
# print(reversed_name_naM)
# print(reversed_name_wonS)

# Склеивание сток
# first_name = 'Sultan'
# second_name = 'Talaibekov'
# full_name = first_name + ' ' + second_name
# print(full_name*3)  # 
# print(full_name*2.5) #error
'=====================================Форматироване строк========================'
'''
Способы(3 вида):
1) c помщью %
2) спомщью (.fomat())
3) терполяция строк(f'стока)
'''
# 1)%s
# name = input('Введте свое имя: ')
# print('Привет, меня зовут', name, 'Talaibekov')
# print("Привет, меня зовут" + ' '+ name + ' ' + 'Talaibekov')
# print('Привет, меня зовут %s Talaibekov' %(name))
# age = 25
# print('Привет, мея зовут', name, 'Talaibekov')

# .format
# name = input('Ввдитесвое имя: ')
# age = 25
# result = 'Привет, моё имя {}, мне {} лет' .format(name, age)
# print(result)

#3)f'стоки'

# name = input('Введите своё имя: ')
# age = 31 
# result = f'Привет, моё имя, {name}, мой возрас, {age}, год'
# print(result)

'===================================Экранировае сток=============================='
'''
\n - переос строки
\t - горизтальная табуляция
\v - вертикальная табуляция
'''
#print('hello world\nmy name is Anton\nI\'m Sabina\'s mom')
#print('hello world\n\tmy name is Gustaph')
#print('hello world\vSup')
#print('hello world\n\tSup')

'========================================Методы Строк================================'
#print(dir(str)) #dir список методов
'REPLACE'
#str.replace(старое значение, новое значение, кол-во) - это метод строк, который меняет старое значение на новое,
# если указать колличество, то поменяет столько сколько раз мы указали
# text = 'ha ha ha'
# result = text.replace(' ', ', ')
# print(result)

'STRIP'
#str.strip() - Метод строк, который убирает проблемы к начале и в конце строки

# text = '     hello world'
# result = text.strip()
# print(text)
# print(result)

# print(len(text))
# print(len(result))

#str.rstrip() - убирает пробел справа
# text = '  hello world     '
# result = text.rstrip()# убирает справа все пробелы
# print(result)#'   hello world'
# print(len(result))# 15

# #str.lstrip() - убирает пробел слева
# text = '  hello world     '
# result = text.lstrip()# убирает слева все пробелы
# print(result)#'hello world    '
# print(len(result))# 17

'ISDIGIT, ISNUMERIC, ISDECIMAL'
#str.isdigit()
#str.isnumeric() - эти методы проверяют состоит ли наша строка полностью из чисел
#str.isdecimal()

# text = '25'
# print(text.isdigit()) #True
# print(text.isnumeric()) #True
# print(text.isdecimal()) #True

# age = input('Введите свой возраст: ')
# print(age.isdigit())

'ISALPHA'
#str.alpha() - этот метод строк, кторый проверяет состоит ли наша строка только из латиницы 
# или кирилицы

# text  = 'hello world'
# print(text.isalpha()) #False,  так как пробел это не кирилица или латиница

# text_2 = 'helloworld'
# print(text_2.isalpha())#True, так как вся строка состоит из латиницы


'ISALNUM'
#str.isalnum() - это метод, который прверяет на то что состоит ли наша  строка из чисел символов 
#латинского или кирильского алфавита

# text = 'adafsg25'
# print(text.isalnum())# True, так как строка состооит из латиницы и чисел

# text_2 = 'abdnn  25'
# print(text_2.isalnum())#False,  так как есть символы(пробелы, плюс, равно и т. д)

# text_3 = ''
# print(text_3.isalnum())# True

'ISLOWER, ISUPPER'
#str.islower() - метод строк, который проверяет на нижний регистр (с маленькие буквы)
#str.isupper() - метод строк, который проверяет на верхний регистр (с большой буквы)
 
# text = 'MaKers'
# print(text.islower())# False
# print(text.isupper())# False

'ISTITLE'
#str.istitle -  это метод строк, который проверяет начинаеться ли каждое слово в строке с верхнего регистра( с большой буквы)


# name = 'sultan talantbekov'
# name_2 = 'Sultan Talantbekov'
# print(name.istitle()) #False
# print(name_2.istitle()) #True

# name = 'sultan Talantbekov'
# name_2 = 'Sultan talantbekov'
# print(name.istitle()) #False
# print(name_2.istitle()) #False

'INDEX'
#str.index(values, start, end) -  это метод строк, который возвращает индекс заданного значения(value)

# text = 'makers bootcamp'
# print(text.index('a', 7)) #12,  ищет в слове bootcamp

'COUNT'
#str.count(value,start, end) - метод строк который считает сколько у нас значений(value)  есть в строке

# text = 'codingiseasy'
# print(text.count('i'))#2

# text = 'codingiseasy'
# print(text.count('i', 5))#1,  начинает искать с 5го индекса до конца

# text = 'codiniseasy'
# print(text.count('i', 5, 9)) #1, начинает искать с 5го индекса до 9го

'FIND'
#str.find(value, start, end) - это метод строк такой же и метод str.index(смотрите выше), но он не выведет ошибку, 
#если значения(value) нету в строке, jy ghjcnj dthytn byltrc -1

# text = 'makers bootcamp'string = 'Hello lady and gentlman \n'
#print(string*3)

# print(text.find('z')) -  распечатает -1

# text = 'makers bootcamp'
# print(text.index('z')) - распечатает ValueError(NotFound)

'SWAPCASE'
#str.swapcase()- это метод строк который меняет на противоположный регистр(а->A), (A->a) (makers->MAKERS)(mAkErs->MaKeRS)

# text = 'codingiseasy'
# print(text.swapcase())#CODINGISEASY

# text2 = 'CODINGISEASY'
# print(text2.swapcase())#codingiseasy

# text3 = 'CodingiIsEasy'
# print(text3.swapcase())#cODINGiSeASY


# text4 = input('Enter your text: ')
# print(text4.swapcase())

'CAPITALIZE'
#str.capitalize() - это метод строк который меняет первую букву строки на верхний регистр

# text = 'hi my Name is Anton' # Hi my name is anton
# print(text.capitalize()) 

'TITLE'
#str.title() - это метод котрый пререводит начало каждого слова в строке в верхний регистр

# text = 'hi my name is gustaph'
# print(text.title())

'SPLIT'
#str.split(разделитель) -это метод строк, который строку преводит в лист при помощи разделителя


#text = input('Введите числа через запятую: ')
# print(text.split(','))

# text2 = 'hi my name is Gustaph'
# print(text2.split(',')) #['hi', 'my', 'name', 'is', 'Gustaph']

'JOIN'
#'соединитель'.join(list) - это метод строк, который соединяет элементы листа 


# list_ = ['12', '23', '54', '25']
# print(''.join(list_))

#№22
#string = input('Enter your name please: ')
#print(f'Hello {string}')


#  Операторы сравнения
# <, >, ==, <=, >=, !=(не равно)


# num1 = 18 
# num2 =18
# print(num1 <= num2)# True

# stroka1 = 'Hello'
# stroka2 = 'World'
# print(stroka1 > stroka2)

# print(ord('H'))#72
# print(ord('W'))#87
# print(chr(90))#z

# text = 'Hello world! My name is John!'
# if text[0] == 72:
#     # H == 72
#     print('Yes!')
# else:
#     print('Nooo!')# Noo!

# text = 'Hello world! My name is John!'
# if text[0] != 72:
#     # H == 72
#     print('Yes!')
# else:
#     print('Nooo!')# Yes!

# if ord(text[5]) != 72:
#     # H == 72
#     print('Yes!')
# else:
#     print('Nooo!')# Yes!

# Уловные оаераторы - они созданы, чтобы программа могла выполнять разные участки кода в зависимиости от условия
# if, elif, else

# if <condition>:
#    <body if>
#    <body if># сработает только если True
# elif<condition>
#     <body elif>
# else:
#     <body else># сработает если только во всех остальных False

#string = input('Enter smt: ')
# if string == 'Hello!':
#     print('Hello stranger!')
# elif  string == 'John':
#     print('Welcome back John Snow')
# elif string == 'Mercedez':
#     print('Mercedez Benz S class!')
# else:
#     print('совпадений не найдено')

# print('The end!')

# email = input('Enter email: ')
# password1 = input('Enter password: ')
# if len(password1) >>8:
#     raise Exception('Password too short!(password need at least 8 chararters!)')# Принудительно останавливает код самостоятельно
# password2 = input('Enter password confirmation: ')

# if password1 != password2:
#     raise Exception('Password didn\'t match')
# else:
#     print('Successfulu signed up!')

# age = input('Enter your age:')

# if age.isdigit():
#     age = int(age)
#     print(f'Your age:{age}!')
# else:
#     raise Exception('Enter the valid age(only digit!)')

# if age > 170:
#     raise Exception('Invalid age!')
# if age < 21:
#     print(f'Chuvak peihodi cherez {18 - age} let/goda!')
# else:
#     print('Tu prohodish\' po vozrastu, Welcome!')
 
# Логические операторы
# end -> логиское и 
# or -> лог или
# not ->  лог отрицание

# # опраторы идентификации
# in -> проверяет наличие элемента внутри массива либо строки
# is ->  сравнение ячейки памяти
# == сравнение значения 
# is not ->  отрицательное сравнение двух ячеек

#my_age = 20
# other_age_= 18
# result = my_age == 20 and other_age_== 18
# print(result)

# my_age = 20
# other_age_= 18
# result = my_age == 21 or other_age_== 19
# print(result)
# result not my_age == 20
#        #TRUE
# print(result)


# cash = int(input('Enter yor cash: '))
# if cash > 1000 and cash < 1000:
#     print('Srednei!')
# elif cash >= 10000 and cash < 100_000:
#     print('Mnogo!')
# elif cash >= 100_000:
#     print('krasavchik!')
# else:
#     print('pechal\'no!')

# is_goole_user = True
# is_github_user = False
# is_age_less_21 = False
# user_coin = 9000

# if (is_goole_user or is_github_user) and (is_age_less_21 or user_coin > 5000):
#     print('You enter the system')
# else:
#     print('Sorry, you coudn\'t enter!')


# str1 = ' Hello woerld!'
# choice = input('Enter the character: ')

# if choice in str1:
#     print(f'Символ {choice} усть в строке: "{str1}"!')
# else:
#     print(f'Символа{choice} нет в строке: "{str1}"!')