number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in number_list:
#     print (str(number) + ' Hi!')

# for number in number_list:
#     if number % 2 == 0:
#         print(number)
#     else:
#         print("Hey")

# list_numbers_sum = 0
# for number in number_list:
#     list_numbers_sum = list_numbers_sum + number
# print(list_numbers_sum)

# greeting = 'Hello Python!'
# for letter in 'Hello Python!':
#     if letter == 'o':
#         print(letter)
#
# tuple_list = [('a', 'b'), ('c', 'd'),('e','f')]
# for item in tuple_list:
#     print(item)
# for letter1, letter2 in tuple_list:
#     print(letter1, letter2)
#
# tuple_list = [('a', 'b', 1), ('c', 'd', 4),('e','f',5)]
# for item in tuple_list:
#     print(item)
# for letter1, letter2, num in tuple_list:
#     print(letter1, letter2, num)
#
# dictionary = {'key1': 'value1','key2': 'value2','key3': 'value3','key4': 'value4'}
# for item in dictionary.items():
#     print(item)
# for item in dictionary:
#         print(item)
# for item in dictionary.keys():
#     print(item)
# for item in dictionary.values():
#     print(item)
# for key, value in dictionary.items():
#     print(key, value)
#
# for x in range(5):
#     print (x)
# for _ in range(5):
#     print ('something')
#

#Используйте цикл for для вычисления суммы всех чётных чисел в диапазоне от 10 до 30 (включая крайние значения). Выведите результат на печать
sum = 0
for x in range(10,31):
    if x % 2 == 0:
        sum = sum + x
print (sum)

#Получите от пользователя число на вводе и используйте цикл for для вывода на экран текста 'Hello!' столько же раз
number = int(input('Please input your number: '))
for _ in range(number):
    print('Hello!')

