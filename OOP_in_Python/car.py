# class Car:
#     wheels_number = 4;
#     def __init__(self, name, color, year, is_crashed):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#
#
# mazda_car = Car(name = "Mazda CX7", color = 'red', year=2017, is_crashed=True)
# print(mazda_car.name)
# print(mazda_car.is_crashed)
# bmw_car = Car(name = 'BWM Z3', color='black', year=2005,is_crashed=False)
# print(bmw_car.name)
# print(bmw_car.year)
# print(bmw_car.wheels_number)
#
# number_of_wheels_of_3_cars = Car.wheels_number * 3
# print(number_of_wheels_of_3_cars)
#

#Создайте класс BlogPost с атрибутами user_name, text, number_of_likes. Создайте два объекта этого класса.
#После создания измените атрибут number_of_likes одного из объектов. Распечатайте атрибут number_of_likes каждого из объектов
class BlogPost:
    def __init__(self,user_name, text, number_of_likes):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes
blog1 = BlogPost(user_name = 'Jack', text = 'Hello', number_of_likes = 4)
blog2 = BlogPost(user_name = 'Jane', text = 'Hi', number_of_likes = 5)
print(blog1.number_of_likes)
print(blog2.number_of_likes)
blog1.number_of_likes = 10
print(blog1.number_of_likes)
print(blog2.number_of_likes)