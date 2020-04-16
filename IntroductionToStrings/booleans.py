print (1 < 2)
print(type(True))
print(type(False))

#Comparison operators
print (1 == 1)
print (1 == 2)
print ('Hello' == 'Hello')
print ('Hello' == 'hello')
print (1 != 1)
print (1 > 2)
print (1 < 2)
print (1 >= 2)
print (1 <= 2)

print(ord('a'))
print ('a' > 'b')
print ('hia' > 'hello') #TRUE because i > e

age = int(input ("\nInput your age: "))
print ('Access is permitted ' + str(age >= 18))

#Создайте 2 переменных, содержащие числовые значения. Сравните их при помощи всех операторов сравнения и выведите результат на экран
x = 42
y = 36
print (x == y)
print (x > y)
print (x >= y)
print (x < y)
print (x <= y)
print (x != y)

#Сравните две одинаковых буквы, но одна из них должна быть заглавной, при помощи операторов сравнения ">" и выведите результат на экран. Выведите на экран ASCII код каждой из букв
var_a = 'a'
var_A = 'A'
print (ord(var_a))
print (ord(var_A))
print(var_a > var_A)