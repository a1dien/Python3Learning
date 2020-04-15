rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'}
print(rainbow_colors)
print(type(rainbow_colors))

empty_set = {}
print(empty_set)
print(type(empty_set)) #it's dictionary!

empty_set = set()
print(empty_set)
print(type(empty_set)) #it's set!

number_list = [1, 2, 544]
text_tuple = ('sfd', 'tvwv', '4k121')
set_from_list = set(number_list)
set_from_tuple = set(text_tuple)
print(set_from_list)
print(set_from_tuple)

set_from_list.add(7777)
set_from_tuple.add('Hello')
set_from_tuple.add('Hello')
print(set_from_list)
print(set_from_tuple) #Hello only once! set for the unique values

list = [1, 1, 1, 1, 2, 3]
set_list = set(list)
print(set_list)

rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'}
rainbow_colors.pop
print(rainbow_colors) #removed red - 1 random element
rainbow_colors.remove('indigo') #removed indigo
#rainbow_colors.remove('indigo') #removed indigo can't remove not existing element
print(rainbow_colors)
rainbow_colors.discard('yellow')
rainbow_colors.discard('yellow') #no probles to try to delete not existsting element
print(rainbow_colors)

rainbow_colors.clear()
print(rainbow_colors)

#Создайте множество при помощи функции set() из текста, чтобы получить уникальные символы, содержащиеся в тексте.
#Присвойте результат переменной. Выведите переменную на экран. Выведите тип значения переменной на экран. При необходимости найдите информацию в интернете
text = '''
#Создайте множество при помощи функции set() из текста, чтобы получить уникальные символы, содержащиеся в тексте. 
#Присвойте результат переменной. Выведите переменную на экран. Выведите тип значения переменной на экран. При необходимости найдите информацию в интернете
'''
unique=set(text)
print(unique)

