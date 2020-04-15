number_list = [42, 314, 1, 41.33]
print(number_list)
some_list = [12, 'hello', 35.213]
print(some_list)
print(len(some_list))
print(some_list[1])
another_list = some_list[:2]
print(another_list)
some_list[1] = 'hi'
print(some_list)
new_list = some_list + another_list
print ("Check")
print(new_list)

#Adding items
#new_list[5] = 'new item'
new_list.append('new item')
print(new_list)
new_list.insert(0, 'start')
print(new_list)
new_list.insert(3, 13)
print(new_list)

#Removing items
new_list.pop()
print(new_list)
new_list.pop(0)
print(new_list)
new_list.pop(-3)
print(new_list)

deleted_item = new_list.pop(1)
print(deleted_item)

deleted_item = new_list.remove(13)
print(new_list)
print(deleted_item)


number_list = [42, 314, -1, 41.33]
letter_list = ["s", 'w', "a", "k"]
number_list.sort()
letter_list.sort()
print(number_list)
print(letter_list)
x = number_list.sort()
print (x) #NONE return!

number_list.reverse()
print(number_list)
letter_list.reverse()
print(letter_list)

number_list.append(letter_list)
print(number_list)

#Создайте список, содержащий разные типы данных
new_list = [1, 'tst', 1.5, 'bbbb', "w12w"]
#Создайте список, извлеките из него элементы с 1 по 3, поместите их в новый список и распечатайте
another_list = new_list[0:3]
print(another_list)
