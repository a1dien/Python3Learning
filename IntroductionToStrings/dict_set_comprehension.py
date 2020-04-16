#dict comprehension
number_dict = {'first':1, 'second':2, 'third':3}
new_dict = {key:value**3 for key,value in number_dict.items()}
print (new_dict)

number_list2 = [6, 421, -412, 5205, -41441, 1123]
number_dict = {num : num ** 2 for num in number_list2}
print(number_dict)

number_list2 = [6, 421, -412, 5205, -41441, 1123, 0]
number_dict2 = {num : 'positive' if num > 0 else 'negative' if num < 0 else 'zero' for num in number_list2}
print(number_dict2)

#set comprehension
number_list3 = [6, 421, -412, 5205, -41441, 1123, 0]
number_set = {'positive' if num > 0 else 'negative' if num < 0 else 'zero' for num in number_list3}
number_set2 = {num ** 2 for num in number_list3}
print(number_set)
print(number_set2)

number_set3 = {num ** 2 for num in range(3, 11)}
print(number_set3)

letter_set = {letter.upper() for letter in 'hello'}
print(letter_set)