#args kwargs
#args
# def ten_percent_of_product(x, y):
#     return (x*y)*0.1
# print(ten_percent_of_product(10, 20))

# def ten_percent_of_product_with_args(*args):
#     product = 1
#     for num in args:
#         product = product * num
#     return product * 0.1
# print(ten_percent_of_product_with_args(10,1,5132,2,333,10))

# def ten_percent_of_product_with_args(percent, *args):
#     product = 1
#     for num in args:
#         product = product * num
#     return product / 100 * percent
# print(ten_percent_of_product_with_args(20,1,5132,2,333,10))
#
#kwargs
# def func_with_kwargs(**kwargs):
#     print(kwargs)
#
# func_with_kwargs(first=1, second=2, third=3)
#
# def hello_with_kwargs(**kwargs):
#     if 'name' in kwargs:
#         print('Hello! Nice to meet you, {}'.format(kwargs['name']))
#     else:
#         print('Hello, What is your name?')
# hello_with_kwargs(gender='male', age=24, name='Jack')
# hello_with_kwargs(gender='male', age=24)

# def hello_with_kwargs(greeting, **kwargs):
#     if 'name' in kwargs:
#         print('{}! Nice to meet you, {}'.format(greeting,kwargs['name']))
#     else:
#         print('{}, What is your name?'.format(greeting))
# hello_with_kwargs('Hello',gender='male', age=24, name='Jack')
# hello_with_kwargs('Good Morning',gender='male', age=24)

# def func_with_args_and_kwargs(*args, **kwargs):
#     print('I would like {} {}'.format(args[0],kwargs['food']))
#     print(args)
#     print(kwargs)
# func_with_args_and_kwargs('one','two','three',drink='coffee', food='sandwich')


#Создайте функцию is_cat_here(), которая принимает любое количество аргументов и проверяет есть ли строка 'cat' среди них.
# Функция должна возвращать True, если такой параметр есть и False в обратном случае. Буквы в строке 'cat' могут быть как большие, так и маленькие
def is_cat_here(*args):
    for text in args:
        if 'cat' == text.lower():
            return True
    return False

#Создайте функцию is_item_here(item, *args), которая проверяет есть ли  item среди args. Функция должна возвращать True, если такой параметр есть и False в обратном случае.
def is_item_here(item, *args):
    for value in args:
        if value == item:
            return True
    return False

#Создайте функцию your_favorite_color() с позиционным параметром my_color и параметрами **kwargs, которая будет выводить на экран
# 'My favorite color is (значение my_color), what is your favorite color?', если в параметрах kwargs нет ключа color, и 'My favorite color is (значение my_color),
# but (значение по ключу color) is also pretty good!', если в параметрах kwargs ключ color присутствует
def your_favorite_color(my_color, **kwargs):
    if 'color' in kwargs:
        print('My favorite color is {}, but {} is also pretty good!'.format(my_color, kwargs['color']))
    else:
        print('My favorite color is {}, what is your favorite color?'.format(my_color))

your_favorite_color('red', color='yellow', key1='tst', key2='tst')
your_favorite_color('red', key1='tst', key2='tst')