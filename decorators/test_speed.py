from time import time
from functools import wraps
# # sum([number for number in range(10000)])
# # sum(number for number in range(10000))
# #
# # start_time = time.time()
# # end_time = time.time() -  start_time
#
#
#
# def speed_test(function):
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         start_time = time()
#         result = function(*args, **kwargs)
#         end_time = time()
#         print(f'Time of code function: {function.__name__} execution {end_time - start_time}')
#         return result
#     return wrapper
#
# @speed_test
# def sum_with_list():
#     return sum([number for number in range(100000)])
#
# print(sum_with_list())
#
# @speed_test
# def sum_with_list1():
#     return sum(number for number in range(100000))
# print(sum_with_list1())
#
# @speed_test
# def product(range_value):
#     result = 1
#     for number in range(1, range_value):
#         result *= number
#     return result
#
# print(product(10000))

#Создайте функцию-декоратор hello_from_decorator, которая добавляет к возвращаемому значению функции, которую она декорирует, строку "Hello from decorator!"


def hello_from_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs) + ' | Hello from decorator!'
    return wrapper

@hello_from_decorator
def print_text(*args, **kwargs):
    return 'Some result'

print(print_text('txt'))