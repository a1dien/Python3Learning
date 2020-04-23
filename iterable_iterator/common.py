# #iterate
#
# #iterable objects
# number_list = [1, 2, 3, 4, 5]
#
# for number in number_list:
#     print(number)
#
#
#
# for letter in 'my_string':
#     print(letter)
#
#
# #iterators
#
# number_list_iterator = iter(number_list)
# print(type(number_list_iterator))
#
# string_iterator = iter('my_string')
# print(type(string_iterator))
#
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())
# #print(number_list_iterator.__next__()) #exception, StopIteration
#
# print(string_iterator.__next__())
# print(string_iterator.__next__())
# print(string_iterator.__next__())
# print(string_iterator.__next__())
# print(string_iterator.__next__())
# print(string_iterator.__next__())
# print(string_iterator.__next__())
# print(string_iterator.__next__())
# print(string_iterator.__next__())

#iter(1) #TypeError: 'int' object is not iterable

# number_list = [1, 2, 3, 4, 5]
# number_list_iterator = iter(number_list)
# print(next(number_list_iterator))

def my_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator.__next__())
        except StopIteration:
            print('Iteration is finished')
            break



my_for_loop('hello')