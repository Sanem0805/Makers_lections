# Магические методы - методы у которых два нижних подчеркивания в начале и в конце.
# Магия в том, что мы их не вызываем напрямую, они вызываются в определенный момент,
# либо они вызываются определенными операторами или функциями.

# Магические методы которые срабатывают при помощи оператора:

# eq (self, other) --> "=="
# __ne__(self, other) --> "!="
# __lt__(self, other) --> "<"
# __gt__(self, other) --> ">"
# __ge__(self, other) --> ">="
# __le__(self, other) --> ">="

# __eq__(self, other) -> --:
# __ne__(self, other) ->
# __lt__(self,other) ->
# __gt__(self, other) ->

# __sub__(self, other) -> - __div__ -> /
# __mul__ -> *  __mod__ -> %
# __floordiv__ -> // __add__ -> +
# __pow__ -> **

# class MyClasss:
#     def __init__(self, string) -> None:
#         self.string = string
#     def __add__(self, other):
#         print('add сработал')
#         print(self, '!!!!!!')
#         print(other, '*****')
#         res = self.string + other.string
#         return MyClasss(res)
#     def __str__(self) -> str:
#         return self.string

# obj1 = MyClasss('John')
# obj2 = MyClasss('Jamie')
# obj3 = MyClasss('Lanister')
# res =obj1 + obj2 + obj3
# print(res)
# print(res.string)

# class Word(str):
#     def __init__(self, word) -> None:
#         self.word = word
#     def __gt__(self, other: str) -> bool:
#         print('gt сработал')
#         print(self, '!!!!!')
#         print(other, '****')
#         return len(self) > len(other)

# obj1 = Word('John')
# obj2 = Word('Hello World')
# print(obj1 > obj2)

#===================================
# конструктор -> __new__(cls)
# инициализатор -> __init__(self)
# вызывается, когда создаём объект

# class Conventor(float):
#     def __new__(cls, __x):
#         print('new сработал')
#         print(cls, "!!!!!!")
#         print(__x, 'xxxxxx')
#         if __x < 50:
#             raise ValueError('x меньше 50')
#         return super().__new__(cls, __x)

#     def __init__(self, x) -> None:
#         print('init сработал')
#         print(self, '!!!!!')
#         self.number = x
# obj = Conventor(51)
# print(obj)

# class Word(str):
#     def __new__(cls,word):
#         word = word.replace(' ', '')
#         return super().__new__(cls, word)

#     def __init__(self, word) -> None:
#         self.word = word
#     def __gt__(self, other: str) -> bool:
#         print('gt сработал')
#         print(self, '!!!!!')
#         print(other, '****')
#         return len(self) > len(other)

# obj1 = Word('John')
# obj2 = Word('Hello World')
# print(obj1 > obj2)

# дандер методы строкового отображения объектов
# __str__ -> для отображения строки, которую будут видеть пользователи
# __repr__ -> строковую информацию о том как создать объект 
# __len__ -> len(obj)
# __repr__ -> repr(obj)

# class Base:
#     def __init__(self, string) -> None:
#         self.string = string

#     def __str__(self) -> str:
#         return f'Объект: {self.string}'

#     def __repr__(self) -> str:
#         return f'Base("string")'
#     def __len__(self):
#         return 5
# user = Base('Hello John')
# print(user)
# print(len(user))
# print(repr(user))
# obj1 = eval(repr(user))# Base('string')
# print(obj1)
#----------------------------------------------------------------------
# class Person:
#     def __init__(self, attrs: dict) -> None:
#         # self.name = attrs['name']
#         #self.a = 5 == setattr('a', 5)
#         for key, value in attrs.items():
#             setattr(self, key, value)

# alice = Person({'name': 'Alice Rose', 'income': 180000, 'eyes': 'brown'})
# john = Person({'email': 'JohnSnow@gmail.com', 'last_name': 'Snow'})
# print(f'{alice.name} --{alice.income} --{alice.eyes}')
# print(f'{john.email} -- {john.last_name}')
#------------------------------------------------
# class MyList(list):
#     def __init__(self, ls) -> None:
#         self.ls =ls
#     def __getitem__(self, index):
#         print(self.ls[index -1])

# x = MyList(['123','Hello', 2,3,4,5])
# x[1]
# x[3]
#__iter__ - вызываеться, когда мы итерируем объект
# class A:
#     def __iter__(self):
#         for i in range(1, 10):
#             print('iter method')
#             yield i
# x = A('Human')
# for i in x:
#     print(i)

# class A:
#     def __init__(self, word) -> None:
#         self.word = word
#     def __iter__(self):
#         for i in self.word:
#             print('iter method')
#             yield i
# x = A('Human')
# for i in x:
#     print(i)
# a = range(1, 10)
# print(a)
# for x in a:
#     print(x)

# def generator(num):
#     for i in range(num):
#         yield i
# a = generator(5)
# for x in a:
#     print(x)
#===========================================
# class User:
#     def __init__(self, name) -> None:
#         self.name = name
    
#     def __call__(self, name, reverse=None):
#         if reverse:
#             print(f'User object: {name[::-1]}')
#             return
#         print(f'User object: {name}')
# user1 = User('John Snow')
# user1('lanister', reverse=True)
#1
# class Account:
#     def __init__(self, name, balance, city) -> None:
#         self.name = name
#         self.balance = balance
#         self.city = city
#         print('Счет создан')
#     def __repr__(self) -> str:
#         return f'{self.name} {self.balance}' 
#     def __str__(self) -> str:
#         return f'Hello {self.name} {self.balance} {self.city}'
#     def __del__(self):
#         print('Пока')
# obj_account = Account("Rick", 2013, 'Bishkek')  
# print(obj_account)  
# print(repr(obj_account))
#2
# class MyNumber(int):
#     def __init__(self, value) -> int:
#         self.value = value
#     def __add__(self, other: int) -> int:
#         return f'Это сложение и результат равен: {self.value + other}'
#     def __sub__(self, other: int) -> int:
#         return f'Это вычитание и результат равен: {self.value - other}'
#     def __mul__(self, other: int) -> int:
#         return f'Это умножение и результат равен: {self.value * other}'
#     def __truediv__(self, other: int) -> float:
#         return f'Это деление и результат равен: {self.value / other}'
# obj_int = MyNumber(5)
# print(obj_int + 2)
# print(obj_int - 5)
# print(obj_int * 5)
# print(obj_int / 5)
#2 переопределение от класса int все функции
# class MyNumber(int):
#     def __new__(cls, value):
#         obj = super().__new__(cls, value)
#         obj.value = value
#         return obj
#     def __add__(self, other):
#         result = super().__add__(other)
#         return f"Это сложение и результат равен: {result}"  
#     def __sub__(self, other):
#         result = super().__sub__(other)
#         return f"Это вычитание и результат равен: {result}"
#     def __mul__(self, other):
#         result = super().__mul__(other)
#         return f"Это умножение и результат равен: {result}"
#     def __truediv__(self, other):
#         result = super().__truediv__(other)
#         return f"Это деление и результат равен: {result}"
# obj_int = MyNumber(5)
# print(obj_int + 5)
# print(obj_int - 5)
# print(obj_int * 5)
# print(obj_int / 5)
#3
# class MyList(list):
#     def __init__(self, list1):
#         self.list1 = list1
#     def __getitem__(self, index):
#         return self.list1[index -1]
# obj_list = MyList([1,2,3,4,5])
# print(obj_list[2])
#4 
# class Student:
#     def __init__(self, name, class_name, ball) -> None:
#         self.name = name
#         self.class_name = class_name
#         self.ball = ball
#     def srednee_znach(self):
#         srednee = sum(self.ball.values())/len(self.ball)
#         return srednee

#     def __gt__(self, other):
#         return f'> {self.srednee_znach() > other.srednee_znach()}'
#     def __lt__(self, other):
#         return f'< {self.srednee_znach() < other.srednee_znach()}'
#     def __ge__(self,other):
#         return f'>= {self.srednee_znach() >= other.srednee_znach()}'
#     def __le__(self, other):
#         return f'<= {self.srednee_znach() >= other.srednee_znach()}'

# obj_student1 = Student('a', 'A', {'math': 100, 'history': 50, 'literature': 88})  
# obj_student2 = Student('b', 'Aa', {'math': 100, 'history': 50, 'literature': 88})  
# print(obj_student1 > obj_student2)  
# print(obj_student1 < obj_student2)  
# print(obj_student1 >= obj_student2)  
# print(obj_student1 <= obj_student2) 
#5 платформа не принемает
# class Word:
#     def __new__(cls, string):
#         string = string.replace(' ', '')
#         return super().__new__(cls, string)
#     def __init__(self, string) -> None:
#         self.string = string
#     def __gt__(self, other: str) -> bool:
#         return len(self) > len(other)
#     def __lt__(self, other: str) -> bool:
#         return len(self) < len(other)
#     def __ge__(self, other: str) -> bool:
#         return len(self) >= len(other)
#     def __le__(self, other: str) -> bool:
#         return len(self) <= len(other)
# word1 = Word('H  e  l  l  o')  
# word2 = Word('world!')
# print(word1 > word2)
# print(word1 < word2)  
# print(word1 >= word2)  
# print(word1 <= word2) 
#6
# class Kopilka:
#     def __init__(self):
#         self.__total = 0
#         self.__coins = []
#     def add_moneta(self, moneta):
#         self.__total = self.__total + moneta
#         self.__coins.append(moneta)
#     def __len__(self):
#         mount = len(self.__coins)
#         return mount
#     def __getitem__(self, index):
#         return self.__coins[index]
#     @property
#     def get_coin(self):
#         return self.__coins
# obj = Kopilka()
# obj.add_moneta(25)
# obj.add_moneta(30)
# print(len(obj))
# for i in obj:
#     print(i)

# class Kopilka:
#     def __init__(self):
#         self.__total = 0
#         self.__coins = []

#     def add_moneta(self, moneta):
#         self.__total += moneta
#         self.__coins.append(moneta)

#     def __len__(self):
#         return len(self.__coins)

#     def __getitem__(self, index):
#         return self.__coins[index]

# obj = Kopilka()
# obj.add_moneta(1)
# obj.add_moneta(5)
# obj.add_moneta(10)

# print(obj._Kopilka__total)
# print(obj._Kopilka__coins)

# print(len(obj))
# for coin in obj:
#     print(coin)
#7
# class Anagram(str):
#     def __init__(self,name) -> None:
#         super().__init__(self)
#         self.name = name
#     def __eq__(self, other: object) -> bool:
        


# class Anagram(str):
#     def __init__(self, word):
#         super().__init__()
#         self.word = word
    
#     def __eq__(self, other):
#         if len(self.word) != len(other.word):
#             return False
#         for char in self.word:
#             if self.word.count(char) != other.word.count(char):
#                 return False
#         return True

#     def __mul__(self, num):
#         return self[::-1] * num

# word1 = Anagram('hello') 
# word2 = Anagram('olleh') 
# print(word1 == word2) 
# print(word1 * 3)

# class Anagram(str):
#     def __init__(self, value):
#         self.value = value

#     def eq(self, other):
#         list1 = list(map(lambda x: x, self.value))
#         list1.sort()
#         list2 = list(map(lambda x: x, other.value))
#         list2.sort()
#         return list1 == list2

#     def mul(self, other):
#         return self.value[::-1] * other
    
# word1 = Anagram('hello') 
# word2 = Anagram('olleh') 
# print(word1 == word2)
# print(word1 * 3)
