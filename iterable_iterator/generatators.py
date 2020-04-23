# #Generators are iterators
# # Generators can be created with generator functions
# # Generators can be create iwht generator expressions
#
#
# # def my_fuction(x):
# #     return x
# #
# #
# # print(my_fuction(4))
#
# def count_up_to(x):
#     count = 1
#     while count <= x:
#         yield count
#         count += 1
# #
# # print(count_up_to(4))
# # counter = count_up_to(4)
# # print(counter.__next__())
# # print(counter.__next__())
# # print(counter.__next__())
# # print(next(counter))
# # #print(counter.__next__()) StopIteration
#
# counter = count_up_to(10)
# counter.__next__()
# counter.__next__()
#
# for number in counter:
#     print(number)
#

#Создайте функцию-генератор get_week_day(), которая создаёт генератор, вырабатывающий один день недели за раз, Дни недели должны начинаться с воскресенья и заканчиваться субботой.
# list_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
#
# def  get_week_day():
#     count = 0
#     while count < len(list_days):
#         yield list_days[count]
#         count += 1
#
# current_day = get_week_day()
#
# print(current_day.__next__()) # 'Sunday'
# print(current_day.__next__()) # 'Monday'
# print(current_day.__next__()) # 'Tuesday'
# print(current_day.__next__()) # 'Wednesday'
# print(current_day.__next__()) # 'Thursday'
# print(current_day.__next__()) # 'Friday'
# print(current_day.__next__()) # 'Saturday'
#

#Создайте функцию even_odd(), создающую генератор, который будет попеременно вырабатывать строки 'even' и 'odd'.

def even_odd():
    count = 0
    while True:
        yield ('even' if count % 2 == 0 else 'odd')
        count += 1


even_odd_generator = even_odd()
print(next(even_odd_generator)) # 'even'
print(next(even_odd_generator)) # 'odd'
print(next(even_odd_generator)) # 'even'
print(next(even_odd_generator)) # 'odd'

...