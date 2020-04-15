#Indexing
greeting = "Hello Python!"
greeting_length = len(greeting)
print(greeting_length)
print(greeting[0] + ' ' + greeting[1])
print(greeting[-1] + ' ' + greeting[12])

#Slicing
print(greeting[2:5])
print(greeting[6:10])
print(greeting[-5:-2])
print(greeting[2:])
print(greeting[-2:])
print(greeting[:5])
print(greeting[:])
print(greeting[::2])
print(greeting[1:8:3])
print(greeting[::-1])

#Выведите на печать вторую букву l из строки 'Hello Python!'
#Присвойте строку переменной, затем выведите на печать букву
letter = greeting[3]
print(letter)
#Выведите на печать вторую букву l из строки 'Hello Python!'
#Сделайте это без присваивания строки переменной, в одной строке кода. Если не знаете, как это сделать, попробуйте погуглить
print(greeting[3])
print('Hello Python'[3])
#Выведите на печать 'He' из строки 'Hello Python!' минимум двумя способами
print(greeting[:2])
print(greeting[-13:-11])
#Создайте новую строку 'Path' из строки 'Hello Python!' путём конкатенации части строки и отсутствующего символа. Выведите новую строку на печать
new_string = greeting[6] + 'a' + greeting[8:10]
print(new_string)




