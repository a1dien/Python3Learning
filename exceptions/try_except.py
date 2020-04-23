# print ('Some code')
#
# try:
#     print (len(23))
#     print (my_var)
#
# except TypeError:
#     print ('Type error has happened')
# except NameError:
#     print('Name error has happened')
#
# print ('Code after an error')

user_dict = {'first_name' : 'Jack', 'last_name': 'White', 'age' : 24}

# print(user_dict['last_name'])
# print(user_dict['name'])
# print(user_dict.get('last_name'))
# print(user_dict.get('name'))

def get_dict_value(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return None

print(get_dict_value(user_dict, 'age'))
print(get_dict_value(user_dict, 'name'))