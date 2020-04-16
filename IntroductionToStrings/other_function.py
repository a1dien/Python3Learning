# for x in range(3,10,2):
#     print(x)
# print(range(5))
# print(list(range(5)))
#
# letter_index = 0
# my_string = 'fefwefwefwe'
# for letter in my_string:
#     print(letter + ' is at index ' + str(letter_index))
#     letter_index += 1
#
# my_string = 'fefwefwefwe'
# ###for item in enumerate(my_string): tupple
# for index, item in enumerate(my_string):
#     print(index, item)

print('a' in 'Jack')
print (str(1) in 'Jack')
letter_list = ['a', 'b', 'c']
print ('a' in letter_list)
print ([1] in letter_list)
dict_1 = {1:'a', 2: 'b', 3:'c'}
print (1 in dict_1)
print('c' in dict_1.values())

print (min(15, 3, 56, 4))
print (max(15, 3, 56, 4))

my_list = [15, 3, 56, 4]
print(min(my_list))
print(max('Hello'))

from random import shuffle
my_list = [15, 3, 56, 4]
shuffle(my_list)
print(my_list)

from random import randint
print(randint(11,20))
