class Car:
    wheels_number = 4;
    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed

    def drive(self, city):
        print(self.name + ' is driving to ' + city + '.')

    def change_color(self, new_color):
        self.color = new_color
opel_car = Car('Opel Tigra', 'grey', '1995', True)
opel_car.drive('London')
opel_car.change_color('gold')
print(opel_car.color)

mazda_car = Car('Mazda CX7', 'red', 2008, False)
mazda_car.drive('Paris')

class Circle:
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius
        self.circumference = 2 * Circle.pi * self.radius

    def get_area(self):
        return self.pi * (self.radius ** 2)

    def get_circumference(self):
        return 2 * self.pi * self.radius

circle1 = Circle()
print(circle1.get_area())
#print(circle1.get_circurference())
print(circle1.circumference)

circle1 = Circle(3)
print(circle1.get_area())
