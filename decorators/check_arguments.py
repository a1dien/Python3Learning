from functools import wraps


def prohibit_kwargs(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError ('Keyword arguments are prohibited')
        return function(*args, **kwargs)
    return wrapper

def prohibit_integer(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        for val in args:
            if type(val) == int:
                raise ValueError('Integer arguments are prohibited')
        for key, val in kwargs:
            if type(val) == int:
                raise ValueError ('Integer arguments are prohibited')
        return function(*args, **kwargs)
    return wrapper

@prohibit_kwargs
@prohibit_integer
def print_hello(name):
    print('Hello {}'.format(name))

#print_hello(name = 'Jack')
print_hello('Jack')
#print_hello(1)

#Создайте функцию-декоратор prohibit_more_than_2_args, которая выполняет функцию, которую она декорирует, если в этой функции не больше двух аргументов.
#В противном случае должна вызываться ошибка ValueError с сообщением "Function must have less than 3 arguments!"



def prohibit_more_than_2_args(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if len(args) > 2 or len(kwargs) > 2:
            raise ValueError('To much arguments! Reduce arguments to 2 or less.')
        # if len(kwargs) > 2:
        #     raise ValueError('To much arguments! Reduce arguments to 2 or less.')
        return function(*args, **kwargs)
    return wrapper

@prohibit_more_than_2_args
def some_func(*args, **kwargs):
    print ('Hi')

#some_func(f=1, s=2, t=3)
#some_func(1, 2, 3)
some_func(1, 2)