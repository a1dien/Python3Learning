from functools import wraps
#
#
# def check_if_first_arg_is(value):
#     def inner_deck(function):
#         @wraps(function)
#         def wrapper(*args, **kwargs):
#             if args and args[0] != value:
#                 print(f'First argument has to be {value}')
#             return function(*args, **kwargs)
#         return wrapper
#     return inner_deck
#
# @check_if_first_arg_is('red')
# def print_rainbow_colos(*colors):
#     print(colors)
#
# @check_if_first_arg_is(7)
# def multiple_7(a, b):
#     return a * b
#
# print_rainbow_colos('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
# print_rainbow_colos('orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
# print(multiple_7(7, 5))
#

def enforce(*types):
    def inner_dec(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            new_args = []
            for a, t in zip(args, types):
                new_args.append(t(a))
            return function(*new_args, **kwargs)
        return wrapper
    return inner_dec

@enforce(str, int)
def print_text_n_times(text, n):
    for number in range(n):
        print(text)

print_text_n_times('hi', '5')

# * args = ('Hi, '3')
# * types = (str, int)
# zip (args, types) - ('Hi', str) ('3', int)
@enforce (int, int)
def divide (a,b):
    return a/b


print(divide('4','2'))

#Создайте функцию-декоратор wait, которая задерживает выполнение кода функции, которую она декорирует, на n секунд.
# Аргумент n должен передаваться в декоратор. Воспользуйтесь функцией для задержки выполнения кода.
# Найдите информацию об использовании этой функции в интернете самостоятельно. Также после задержки должно выводится сообщение
# "There was a pause {количество секунд} seconds before execution {имя задекорированной функции }"


