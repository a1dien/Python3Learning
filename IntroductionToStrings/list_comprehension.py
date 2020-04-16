greetings = 'hello!'
letter_list = []
for letter in greetings:
    letter_list.append(letter)
print(letter_list)

letter_list = [letter for letter in greetings]
print(letter_list)

number_list = [number for number in '0123456789']
print(number_list)

number_list_1 = [num for num in range(0,10)]
print(number_list_1)

number_list_2 = [num ** 2 for num in range(0,10)]
print(number_list_2)

number_list_3 = [(-((num -3)/2)**2) for num in range(0,10)]
print(number_list_3)

number_list_4 = [6, 214, -1412, 923, 6925, -41123]
new_list = [number for number in number_list_4 if number > 10]
print(new_list)

new_list = ['+' if num > 0 else '-' for num in number_list_4]
print(new_list)

#Из исходного списка greetings = ['hello', 'hi', 'hey', 'hola'] создайте новый список содержащий вторую букву из каждой строки исходного списка. Выведите новый список на печать.
#Решите задание двумя способами - при помощи List Comprehension и без него.
greetings = ['hello', 'hi', 'hey', 'hola']
second_letter_1 = [let[1] for let in greetings ]
print(second_letter_1)

second_letter_2 = []
for letter in greetings:
    second_letter_2.append(letter[1])
print(second_letter_2)

#Из исходного списка digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] создайте новый список содержащий нечетные числа исходного списка. Выведите новый список на печать.
#Решите задание двумя способами - при помощи List Comprehension и без него.
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_digits_1 = [num for num in digits if num % 2 != 0]
print(odd_digits_1)

odd_digits_2 = []
for num in digits:
    if num % 2 != 0:
        odd_digits_2.append(num)
print(odd_digits_2)
