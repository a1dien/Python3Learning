# Immutable
first_name = 'Jake'
print(first_name[2])
#first_name[2] = 'n' dooesn't work
#print(first_name)

first_two_letters = first_name[:2]
print(first_two_letters)
last_letter = first_name[-1:]
print(last_letter)

#concatenable
new_first_name = first_two_letters + 'n' + last_letter
print(new_first_name)

greeting = 'Hello'
greeting = greeting + ' Python!'
print(greeting)

#Multiplication
yummy = 'Yum '
print(yummy*3)

print(yummy.upper())
print(yummy.lower())

long_string = 'This is the long string'
print(long_string.split())
print(long_string.split('s'))

#Создайте новую строку 'Path' из строки 'Hello Python!' путём конкатенации частей строки и отсутствующего символа. Выведите новую строку на печать
print(greeting[6] + 'a' + greeting[8:10])
#Создайте строку 'zzzzzzz' при помощи умножения и выведите её на экран
letter_z = 'z'*7
print(letter_z)
#Сделайте все буквы строки из предыдущего вопроса заглавными и выведите её на экран
print(letter_z.upper())