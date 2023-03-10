# tp = ('apple', ' chery', ' banana', 'john')
# # for x in tp:
# #     print(x * 3)
# i = 0
# while i < 50:
#     print(i)
#     i += 1 #инкримент  i = i + 1
#           # дикремент i -= 1
 
# tp = ('apple', ' chery', ' banana', 'john')
# x = 0
# while x < len(tp):
#     print(tp[x], f'index:{x}')
#     x += 1

#+*
# a = (1,2,3)
# b = (4,5,6)
# print(a + b)
# print('123' * 5)

# c = (5, )
# a 
# # c += c
# # print(c)
# for x in (1, 101):
#     a += c
# print(a)

#1)input
# tp = (1,8,3,4,5,8,8,9,0)
# target = 8
# #output: (8,3,4,5,8)

# #2)input
# tp  = (1,2,3,8,5,1,2)
# target = 8 # output: result = (8,5,1,2)
 

# tp = (1,8,3,4,5,8,8,9,0)
# target = 8
# first = tp.index(8)
# # print(first)
# # print(tp[first+1:].index(8) + first + 1)

# if tp. count(8) > 1:
#     first = tp.index(8)
#     second = tp.index(8, first+1)
#     result = tp[first: second]
# else:
#     first = tp.index(8)
#     result = tp[first:]
# print(tp, target)
# print(result)


#nums = [2,7,11,15]
# target = 9
# result = [0,1]----------------2+7 = 9
#                             #9 -2=7
#                             #9-7=2
#2) nums = [4, 11, 2, 5, 1,6]
#target = 8



# nums = [2,7,11,15]
# target = 9

# for x in nums:
#     num = target - x
#     if num in nums:
#       print(nums.index(x), nums.index(num))
#       break

# nums = [4, 11, 2, 5, 1,6]
# target = 8
# for x in nums:
#     num = target - x
#     if num in nums == x:
#         continue
#     print(nums.index(x), nums.index(num))
#     break