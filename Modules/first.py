# print(1)
# print('string')
#
# #__name__= '__main__'
# print(__name__)
#
# def function_1():
#     pass
#
# def function_2():
#     pass
#
# class MyClass:
#     pass
#
# if __name__ == '__main__':
#     function_1()
#     function_2()

def function_1():
    print('Function_1() from first.py')

print('Top level in first.py')

if __name__ == '__main__':
    print('first.py is being run directly')
else:
    print('first.py has been imported')