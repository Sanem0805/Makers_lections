# sentence = input('Enter your name: ')
# print(sentence[-2:])
# if sentence[-1] == '?':
# #     print('voprositel\'noe predlojenie')
# # else:
# #     print('Normal one!')
1
# print('Voprositel\'noe predlojenue!' if sentence[-1] == '?'  or sentence [-2:] == '?!' else 'Normal one!')

#===============================================================================

#Ternary operators(теранрный оператор)- это конструкция, которая аналогично по своему дейсвию if/else, 
# но при этом записывается в одну строчику

# number = 18
# res = 'even number' if number % 2 == 0 else 'odd number'
# print(res)
#<срабатывает это выражение если уловие True> if <условиеЮ else <выражение если условие False>
# num = int(input('Enter your number: '))
# res = num - 100 if num < 100 else num * 2
# print(res)

# ls = [55, 65, 75, 89, 100, 15, 6]
# print(ls)
# choice = input('Enter max/min: ')

# res = max(ls) if choice.lower().strip() == 'max' else min(ls)
# print(res)
# index = ls.index(res)
# ls[index] = min(ls)



# записать с фотографии



#===========================================
# from string import digits
# print(digits)
# print(type(digits))
# num = input('num: ')
# if num.isdigit():
#     num = int(num)
# print('Impotant')
# print(num)
# print(type(num))

# from string import digits

# symbols = digits + '-' + '.' #0123456789-.
# flag = True
# while flag:
#     is_correct_number = True
#     num1 = input('Enter first number: ')
#     for x in num1:
#         if not x in symbols:
#             print('You enter wrong number!')
#             is_correct_number = False
#             break
#     if not is_correct_number:
#         continue

#     num2 = input('Enter second number: ')
#     for x in num2:
#         if not x in symbols:
#             print('You enter wrong number!')
#             is_correct_number = False
#             break
#     if not is_correct_number:
    #     continue
    # num1 = float(num1) if '.' in num1 else int(num1)
    # num2 = float(num2) if '.' in num2 else int(num2)
    # operator = input('Enter operator(+, -, *, /): ')

    # if operator == '+':
    #     print(f'Result: {num1 + num2}')
    # elif operator == '-':
    #      print(f'Result: {num1 - num2}')
    # elif operator == '*':
    #      print(f'Result: {num1 * num2}')
    # elif operator == '/':
    #      print(f'Result: {num1 / num2}')
    # else:
    #     print('You enter wrong number!')

    # choice = input('Do you wont to continue(yes/no)? ')
    # if choice.lower().strip() == 'no':
    #     flag = False
    #     print('Good bye!')