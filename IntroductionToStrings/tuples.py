tuple1 = (1, 2, 3)
tuple2 = ('Hello', 'one')
tuple3 = 544, 0.233, 'tst'
print(tuple1)
print(tuple2)
print(tuple3)
print(type(tuple3))
print(tuple1[1])
#tuple1[1] = 1 #not work for tuples
new_tuple = tuple1[0], 22, tuple1[2]
print(new_tuple)

x = y = z = 12
print(x, y, z)
x, y, z = 12, 13, 14
print(x, y, z)
person_tuple = ('John', 'Smith', 1967)
f_name, l_name, year_birth  = person_tuple
print(f_name, l_name, year_birth)

t1 = (1, 2, 3, 1, 5, 1)
print(t1.count(1))
print(t1.count(5))

greetings_tuple = ('hi', 'hey', 'hi', 'hello')
print(greetings_tuple.count('hi'))

print (t1.index(5))
print(greetings_tuple.index('hi'))

#Создайте объект tuple, описывающий компьютер и распакуйте его в соответствующие переменные. Выведите переменные вызвав функцию print() один раз
computer = ('PC', '16GB', '500GB')
type, ram, hd = computer
print(type, ram, hd)

