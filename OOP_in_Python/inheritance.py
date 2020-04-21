# class Car:
#     wheels_number = 4;
#
#     def __init__(self, name, color, year, is_crashed):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#         print('Car is created')
#
#     def drive(self, city):
#         print(self.name + ' is driving to ' + city)
#
#     def change_color(self, new_color):
#         self.color = new_color
#         print ('Color changed to ' + new_color)
#
#
# class Truck(Car):
#
#     wheels_number = 6
#
#     def __init__(self, name, color, year, is_crashed):
#         Car.__init__(self, name, color, year, is_crashed)
#         print('Truck is created')
#
#     def drive(self, city):
#         print('Truck ' + self.name + ' is driving to ' + city)
#
#     def load_cargo(self, weight):
#         print ('The cargo is loaded. Weight is ' + str(weight) + ' kg.')
#
#
# man_truck = Truck('Man', 'yellow', 1982, True)
# man_truck.drive('Los Angeles')
# print(man_truck.wheels_number)
# man_truck.change_color('red')
# man_truck.load_cargo(1000)

#Polymorphism

#
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         raise NotImplementedError('Class successor must impletent this method')
#
#
# class Dog(Animal):
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(self.name + ' is saying woof')
#
# class Cat(Animal):
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(self.name + ' is saying meow')
#
# class Mouse(Animal):
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(self.name + ' is saying pee-pee-pee')
#
# class Fish(Animal):
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(self.name + ' is saying nothing.')
#
# spike = Dog('Spike')
# tom = Cat('Tom')
# jerry = Mouse('Jerry')
# freddy = Fish('Freddy')
# pet_list = [spike, tom, jerry,freddy]
# for pet in pet_list:
#     pet.speak()
#
# def pet_voice(pet):
#     pet.speak
#
# pet_voice(spike)
# pet_voice(tom)
# pet_voice(jerry)
#
#Assigment
#Создайте класс GameCharacter с атрибутами name, health, level и методом speak(), который выводит на печать 'Hi, my name is (значение атрибута name)'.

class GameCharacter:

    @classmethod
    def kill(cls):
        cls.health = 0
        print('Bang-bang, now you\'re dead!')
        print(cls.health)

    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def speak(self):
        print('Hi, my name is ' + self.name)

goblin = GameCharacter('Goblin Gugu', 100, 5)
goblin.speak()
#Создайте класс Villain, наследник класса GameCharacter с теми же атрибутами, методом speak(), который выводит на печать 'Hi, my name is (значение атрибута name) and I will kill you',
# методом kill(), который принимает в качестве параметра объект класса GameCharacter, присваивает атрибуту health этого объекта значение 0 и  выводит на печать 'Bang-bang, now you're dead'


class Villain(GameCharacter):
    def __init__(self, name, health, level):
        GameCharacter.__init__(self, name, health, level)

    def speak(self):
        print('Hi, my name is {} and I will kill you'.format(self.name))


troll = Villain('Troll Vasya', 555, 90)
troll.speak()
troll.kill()
print(troll.health)
goblin.kill()
print(goblin.health)
