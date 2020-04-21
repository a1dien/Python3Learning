#
#
# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def __str__(self):
#         return self.first_name + ' ' + self.last_name
#
#     def __len__(self):
#         return self.age
#
#     def __del__(self):
#         print ('Person object with name {} is deleted from memory'.format(self.first_name))
#
#     def __add__(self, other):
#         return self.age + other.age
#
#
#
# jack = Person('Jack', 'White', 45)
# # print(len([1, 2, 3, 4, 5]))
# # print(jack)
# # print(len(jack))
# # del(jack)
# #print(jack)
#
# jane = Person('Jane', 'Eyer', 23)
# print(jack + jane)
#
# x = 5
# y = 3
#
# a = '5'
# b = '3'
# print (x + y)
# print (x.__add__(y))
# print (a + b)
# print (a.__add__(b))
# print (type(x),type(y), type(a), type(b))
#

#Создайте класс Chain с атрибутом number_of_items.
#Создайте два специальных метода в этом классе.
#Первый должен при вызове встроенной функции print() для объекта этого класса выводить 'Chain with (значение number_of_items) items'
#Второй должен при вызове встроенной функции len() для объекта этого класса возвращать значение number_of_items этого объекта
class Chain:
    def __init__(self, number_of_items):
        self.number_of_items = number_of_items

    def __str__(self):
        return ('Chain with {} items'.format(self.number_of_items))

    def __len__(self):
        return self.number_of_items

chain1 = Chain(10)
print(chain1)
print(len(chain1))

