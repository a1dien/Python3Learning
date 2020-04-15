car_prices = {"Toyota":50000, "Opel":5000, "Volvo":12000}
print(car_prices)
print(car_prices["Toyota"])
car_prices["BWM"] = 75000
print(car_prices)
car_prices["Opel"] = 7500 #update old changes
print(car_prices)
del car_prices["Toyota"]
print(car_prices)
#del car_prices #Full delete Dictionary

car_prices.clear() #clear all data
print(car_prices)

person = {
    'First Name':   'Jack',
    'Last Name' :   'Brown',
    'Age'       :   43,
    'Hobbies'   :   ['footbal', 'photo', 'singing'],
    'Children'  :   {'son': 'Michael', 'daugther' : "Jane"}
}

print(person['Age'])
print(person['Hobbies'])
hobbies = person['Hobbies']
print(hobbies[2])
print(person['Hobbies'][1])
children = person['Children']
print(children)

person["Car"] = "Huyndai"
print(person)
person['Hobbies'][0] = 'basketball'
print(person)
print(person.keys())
print(person.values())
print(person.items())


#Создайте объект dictionary, содержащий пары ключей и значений, выведите на экран одно значение
dict = {'1 key' : '1 value','2 key' : 2}
print(dict['1 key'])

#Создайте объект dictionary, описывающий компьютер
computer = {
    'Type'  :   'Laptop'    ,
    'RAM'   :   '16GB'  ,
    'HD'    :   '500GB' ,
    'SSD'   :   '250GB' ,
    'MotherBoard'   :   "Gigabyte ####",
    'Video' :   ['Nvidia', "GeForce", "4GB"],
    'Other devices' : {
        'Keyboard'  :   'internal',
        'Mouse'     :   'Logitech',
        'Headphones':   'Sony'
    }
}
print(computer)
