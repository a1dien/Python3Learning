print (1 + 1)
print ('1' + '1')
print ('Jack is ' + str(23) + ' years old')

name  = 'Jack'
age = 23
name_and_age = 'My name is {0}. I\'m {1} years old'.format(name, age)
print(name_and_age)
name_and_age = 'My name is {0}. I\'m {1} years old'.format('Jack', 23)
print(name_and_age)
name_and_age = 'My name is {}. I\'m {} years old'.format('Jack', 23)
print(name_and_age)

week_days = 'There are 7 days in a week: {}, {}, {}, {}, {}, {}, {}.'\
    .format('Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday', 'Sunday')
print(week_days)

week_days = 'There are 7 days in a week: {1}, {0}, {2}, {3}, {6}, {4}, {5}.' \
    .format('Tuesday', 'Monday', 'Wednesday', 'Thursday','Saturday', 'Sunday','Friday')
print(week_days)

week_days = 'There are 7 days in a week: {mo}, {tu}, {we}, {th}, {fr}, {st}, {su}.' \
    .format(tu = 'Tuesday', mo ='Monday', we ='Wednesday', th = 'Thursday',st = 'Saturday', su ='Sunday', fr ='Friday')
print(week_days)

float_result = 1000/7
print(float_result)
print('The result of division is {0:1.3f}'.format(float_result))
print ('''
{}{}{}
{}{}{}
{}{}{}
'''.format(1.45883, 342.42449, 94.94912, 9592.34003, 120.11200949, 1.400569, 321.321312312, 45985.3210595, 50.40403))

print ('''
 {0:10.2f} {1:10.2f} {2:10.2f}
 {3:10.2f} {4:10.2f} {5:10.2f}
 {6:10.2f} {7:10.2f} {8:10.2f}
'''.format(1.45883, 342.42449, 94.94912, 9592.34003, 120.11200949, 1.400569, 321.321312312, 45985.3210595, 50.40403))


name  = 'Jack'
age = 23
name_and_age = 'My name is {0}. I\'m {1} years old'.format(name, age)
print(name_and_age)
name_and_age = f'My name is {name}. I\'m {age} years old'
print(name_and_age)

print('My name is %s. I\'m %d years old.' % (name, age))
print('My name is %s. %s %d years old.' % (name, "I\'m", age))

#Создайте таблицу из десятичных дробных чисел с дробной частью разного размера. В таблице должно быть 4 столбца и 2 строки.
#При помощи метода format()  выведите числа на экран так, чтобы всё число занимало 15 символов, а дробная часть 4 символа
print ('''
 {0:15.4f} {1:15.4f} {2:15.4f} {3:15.4f} 
 {4:15.4f} {5:15.4f} {6:15.4f} {7:15.4f}
'''.format(1.4, 42.42, 394.949, 9592.3401, 55120.11203, 458351.400569, 9021321.3213123, 45985.3210595))



