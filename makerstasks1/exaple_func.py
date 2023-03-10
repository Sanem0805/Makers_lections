#1
# def func(list_: list) -> list:
#      res = ''.join (list(map(str, list_)))
#      res = int(res) + 1
#      res1 = list(str(res))
#      res1 = list(map(int, res1))
    
#      return res1
# print(func([1, 2, 3]))

#2
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.  

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used: 

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""
"""
Input: s = "III"
Output: 3
Explanation: III = 3.

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""
# def romanToInt(s: str) -> int:
#     dict_ = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#     s = list(s)
#     newlist=[]
#     for i in s:
#         num = dict_[i]
#         newlist.append(num)
#     list1 = newlist[::-1]
    
# #[5, 1, 100, 10, 1000, 100, 1000]
#     res = 0
#     last = list1[0]
#     for x in list1:
#         if x < last:  
#             res -= x
#         else:
#             res += x
#         last = x
#     return res
    
# print(romanToInt("III"))
# print(romanToInt("LVIII"))
# print(romanToInt("MCMXCIV"))
# print(romanToInt("MMXCV"))

# dict_1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':'I'*4,'IX':'I'*9,'XL':'I'*40,'XC':'I'*90,'CD':'I'*400,'CM':'I'*900}
# list_2=['IV','IX','XL','XC','CD','CM']



# def usingReplaceMethod(input_1:str):
#     global dict1,list2
#     result=0
#     for x in list_2:
#         if x in input_1:
#             input_1=input_1.replace(x,dict_1[x])
#     for x in input_1:
#         var=dict_1[x]
#         result+=var
#     return result

# print(usingReplaceMethod('MCMXCIV'))
# print(usingReplaceMethod('CLXXXIX'))

# def usingMoreLogicalMethod(inp:str):
#     global dict1
#     result=0
#     d=0
#     for x in inp[::-1]:
#         var=dict_1[x]
#         if var>=d:
#             result+=var
#         else:
#             result-=d
#             result+=d-var
#         d=var
#     return result


# print(usingMoreLogicalMethod('MCMXCIV'))
# print(usingMoreLogicalMethod('CLXXXIX'))

#3
"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string."""
"""
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
"""

"""
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
"""
"""
Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
"""
# def comparation(list1, list2: list):
#     stroka1 = ''.join (list(map(str, list1)))
#     stroka2 = ''.join (list(map(str, list2)))
#     if stroka1 == stroka2:
#         print(True)
#     else:
#         print(False)

#     return
# comparation(["ab", "c"],["a", "bc"])
# comparation(["a", "cb"],["ab", "c"])
# comparation(["abc", "d", "defg"],["abcddefg"])

# def comparation(list1, list2: list):
#     from functools import reduce
#     stroka1 = reduce(lambda x, y: (x + y), list1)
#     stroka2 = reduce(lambda x, y: (x + y), list2)
#     if stroka1 == stroka2:
#         print(True)
#     else:
#         print(False)

#     return
# comparation(["ab", "c"],["a", "bc"])
# comparation(["a", "cb"],["ab", "c"])
# comparation(["abc", "d", "defg"],["abcddefg"])

# def brackets(skobka: str) -> bool:
#     if skobka == '()':
#         print(True)
#     elif skobka == '{}':
#         print(True)
#     elif skobka == '[]':
#         print(True)
#     else:
#         print(False)
#         return 

# brackets('()[]{}')

# def brackets(skobka: str) -> bool:
#     if skobka == '()':
#         return True
#     elif skobka == '{}':
#         return True
#     elif skobka == '[]':
#         return True
#     else:
#        return False
       

# print(brackets('()[]{}'))    
#4
"""
Создайте функцию sum_range(start, end), которая суммирует все целые числа от значения start до величины end включительно. Если пользователь задаст первое число больше чем второе, просто поменяйте их местами.
"""
# def sum_range(start, end):
#     if start > end:
#         list_ = list(range(end, start+1))
#         sum_ = sum(list_)
#         return sum_
#     else:
#         list_ = list(range(start, end+1))
#         sum_ = sum(list_)
#         return sum_

# print(sum_range(6, 1))

# 5
"""На входе имеем список строк разной длины. 
Необходимо написать функцию all_eq(lst), которая вернет новый список из строк одинаковой длины. 
Длину итоговой строки определяем исходя из самой большой из них. 
Если конкретная строка короче самой длинной, дополнить ее нижними подчеркиваниями с правого края до требуемого количества символов.
Расположение элементов начального списка не менять.

Input: ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
Output: ['a____', 'aa___', 'aaa__', 'aaaa_', 'aaaaa']  """

# def all_eq(lst):
#     max1 = len(max(lst))
#     list1 = []
#     for i in lst:
#         if len(i) != max1:
#             len_of_i = max1 -len(i)
#             un = '_' * len_of_i + i
#             list1.append(un)
#     list1.append(max(lst))
#     return list1

# print(all_eq(['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))

# Sultan task
# str1 = 'Hello world'
    # def len_word(str1: str) -> int:
    #     list1 = str1.split()
    #     print(list1)
    #     w = len(list1[])
        
    #     return w
    # print(len_word('Hell world'))

"""
Дано предложение "Это короткое предложение", оно может быть перетасовано как "предложение3 короткое2 Это1" или "короткое2 предложение3 Это1".
Учитывая перетасованные предложения, содержащие не более 9 слов, восстановите и верните исходное предложение, удалив цифры в конце слов.

Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
"""
# def sorted_sens(sens1: str) -> str:
#     list1 = sens1.split()
#     list1.sort(key=lambda x: x[-1])
#     sens2 = ''
#     for i in list1:
#         sens2 = sens2 + i[:-1] + ' '
#     return sens2.strip()
# print(sorted_sens('is2 sentence4 This1 a3'))

# text = "is2 sentence4 This1 a3"
# def func(text):
#     list_ = text.split()
#     list_.sort(key = lambda x: x[-1])
#     new_string=""
#     for i in list_:
#         new_string = new_string+i[:-1]+" "
#     return new_string.strip()

# print(func(text))

# def func4(string:str):
#     var=string.split()
#     var1=list(map(lambda x:x[:-1],sorted(var,key=lambda x:x[-1])))
#     return ' '.join(x for x in var1)
# print(func4('is2 sentence4 This1 a3'))
