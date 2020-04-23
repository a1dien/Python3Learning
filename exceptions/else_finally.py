#if we have an error - except fires and else doesn't fire
#if we havn't an error - except doesn't fires and else Fire
#Finally block fires ANYWAY
#
# while True:
#     try:
#         number = int(input('Enter some number: '))
#         print(number / 2)
#     except:
#         print ("You have to enter a number!")
#     else:
#         print('Good job! This is a number!')
#         break
#     finally:
#         print('Finally block')
#
# print('Code after an error handling')

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('You can\'t divide by zero.')
    except TypeError as e:
        print('x and y must be numbers')
        print(e)
    else:
        print('x has divided by y')
    finally:
        print('finally block')


print(divide(4, 2))
print(divide(4, 0))
print(divide('s', 2))