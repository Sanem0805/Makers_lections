#Множества в питоне - "контейнер ", который содержит в себе уникальные элементы в не упорядоченном виде
#{} !!! dic
# set()
# a = {'a': 1} - словрь
# a = {1, 2, 3} - множества

# set1 = {8, 1, 1, 1, 1, 1, 3, 4, 11}
# print(set1)
# print(type(set))

# ls = ['Hello', ' hello', ' John', 'snow']
# print(ls)
# res = set(ls)
# print(res)
# res = list(res)
# print(res)
# print(type(res))


# ls = [1, 2, 4, 'a', False, True, 'n', 'b']
# str1 = 'Hello world'
# ls.append(str1)#,[1, 2, 4, 'a', False, True, 'n', 'b', 'H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
# print(ls)
# res = set(ls)
# print(res)#{False, 1, 2, 'Hello world', 4, 'n', 'b', 'a'}

# #FIFO / LIFO
# set1 = {1, 2, 3, 4, 5, 6, 7,8, 9,}
# set1.pop()
# print(set1)

#remove/discard
#remove - error
#discard - None
# set1 ={1,2,3,4,5}
# set1.remove(20)
# set1.discard(25)
# set1.add(15)
# print(set1)

#frozenset




#Задача в классе
# Создайте кортеж из 8-ми кортежей учащихся ВУЗов. В кортеже будут присутствовать следующие поля: имя студента, 
# возраст, оценка за семестр, город проживания. Ваш код будет принимать этот кортеж, вычислять среднюю оценку по 
# всем учащимся и выводить на печать следующее сообщение: “Ученики {список имен студентов через запятую} в этом 
# семестре хорошо учатся!”. В список студентов, которые выводятся по результатам работы функции, попадут лишь те, 
# у которых оценка за семестр равна или выше средней по всем учащимся.

# кортеж(имя, возраст, оценка, город)

#students = (
    # ('Елена', '13', 9, 'Москва'),
    # ('Ольга', '11', 7.9, 'Иваново'),
    # ('Елизавета', '14', 9.1, 'Тверь'),
    # ('Дмитрий', '12', 5.2, 'Челябинск'),
    # ('Максим', '15', 6.1, 'Самара'),
    # ('Николай', '11', 8.7, 'Владивосток'),
    # ('Артур', '13', 5.8, 'Екатеринбург'),
    # ('John', '13', 10, 'WinterFell')
#)

# marks = []# для того чтобы закинуть все оценки учеников все оценки под 2 индексом храняться только оценки
# for x in students:
#     marks.append(x[2]) # вытыщили все оценки

# print(marks)

# avg_mark = sum(marks) / len(marks)# суммируем все их значение
# print(avg_mark)#посчитали среднее значение

# good_students = []
# for student in students:
#     if student[2] > avg_mark:# сравниеваем все оценки
#         good_students.append(student[0])
# print(f"Ученики {', '.join(good_students)}  в этом симестре хорошо учаться") # соединяем строку
