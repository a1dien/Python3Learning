x = 3

if x > 3:
    print('x > 3')
elif x < 3:
    print('x < 3')
else:
    print('x == 3')

day_time = 'afternoon'

if day_time == 'morning':
    print ('Monster wakes up')
elif day_time == 'afternoon':
    print ('Monster is walking')
elif day_time == 'evening':
    print ('Monster is eating')
elif day_time == 'night':
    print ('Monster is sleeping')
else:
    print ('Monster is doing sleeping')

x = 45
if x % 2 == 0:
    print ('x is even')
else:
    print ('x is odd')

# user_input = input('Input something: ')
# if user_input == 'Hello':
#     print ('Hello, Nice to meet you.')

#False 0, emtpy string, None, empty object
if 1:
    print ('something')
if None:
    print ('None')

# lucky_number = input('Enter a number: ')
# if lucky_number:
#     print (lucky_number + ' is your luck number!')
# else:
#     print('You have to enter some number, please try again.')


#Напишите код, который выводит сообщение: 'Enter any number'. Если было введено число 7, должно выводиться сообщение: '7 is a lucky number! Today is your lucky day!',
# если введено что-то другое - должно выводиться сообщение 'Thank you! Have a nice day!'
lucky_number = int(input('Enter any number: '))
if lucky_number == 7:
    print('{} is a luck number! Today is your lucky day!'.format(lucky_number))
else:
    print ('Thank you! Have a nice day')

#Напишите код, который выводит сообщение: 'Enter an integer number'. Если было введено чётное число, должно выводиться сообщение:
# 'The number is even', если было введено нечётное число, должно выводиться сообщение 'The number is odd'
number = int(input('Enter an integer number: '))
if number % 2 == 0:
    print('{} : The number is even'.format(number))
else:
    print('{} : The number is odd'.format(number))