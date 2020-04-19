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


#Создайте класс BankAccount с атрибутами client_id, client_first_name, client_last_name, balance и
# методами add() и withdraw(), при помощи которых можно пополнять счет и выводить средства со счета соответственно.
# Атрибут balance должен инициализироваться по умолчанию значением 0.0 и меняться при срабатывании
# методов add() и withdraw().
class BankAccount():
    balance = 0.0
    def __init__(self,client_id,client_first_name,client_last_name):
        self.client_id = client_id
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name

    def add(self, summa):
        self.balance = self.balance + summa

    def withdraw(self,summa):
        if self.balance - summa >= 0:
            self.balance = self.balance - summa
        else:
            print("Not enough money on your bank account.")

client1Bank = BankAccount(1, "Jack", "James")
print(client1Bank.balance)
client1Bank.add(100)
print(client1Bank.balance)
client1Bank.withdraw(50)
print(client1Bank.balance)
client1Bank.withdraw(60)
print(client1Bank.balance)