from functools import wraps

# def print_function_data(function):
#     '''
#     This is decorator function
#     :param function:
#     :type function:
#     :return:
#     :rtype:
#     '''
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         print(f'You\'re using {function.__name__}')
#         print(f'Function documentation {function.__doc__}')
#         return function(*args, **kwargs)
#     return wrapper
#
# @print_function_data
# def square_sums(a, b):
#     '''
#
#     :param a: first_number
#     :type a:
#     :param b: second number
#     :type b:
#     :return: sum of squares first and second numbers: (a * a + b * b)
#     :rtype:
#     '''
#     return a * a + b * b
#
# print(square_sums(2, 3))
# print(square_sums.__doc__)
# print(square_sums.__name__)
# help(square_sums)

#Создайте функцию-декоратор print_args, которая распечатывает аргументы *args и **kwargs функции, которую она декорирует

def dec_print_args_kwargs(function):
    def wrapper(*args, **kwargs):
        print(*args)
        print(**kwargs)
        return function(*args, **kwargs)
    return wrapper


@dec_print_args_kwargs
def print_args(*args, **kwargs):
    pass

print_args('tst', [1, 2, 3])