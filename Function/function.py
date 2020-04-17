# def print_greeting():
#     '''
#     Print 'Hello!'
#     :return: None
#     '''
#     print('Hello!')
# #call the function
# print_greeting()
# #receive the description of the function
# help(print_greeting)
#
# def print_greeting_with_name(name = 'Name'):
#     '''
#     :param name
#     :return: None
#     '''
#     print('Hello ' + name + '!')
# print_greeting_with_name('Jack')
# print_greeting_with_name()
#
#
# # noinspection PyMissingOrEmptyDocstring
# def sum_of_two_numbers(a = 0, b = 0):
#     '''
#     Args:
#         a (): The first addend
#         b (): The second addend
#     Returns: Sum of a and b
#     '''
#     return a + b
# x = sum_of_two_numbers(1, 3)
# print(x)
#
# def is_hello_in_text(text):
#     if 'hello' in text:
#         return True
#     else:
#         return False
# print(is_hello_in_text('tst'))
#
# def is_hello_in_text(text):
#     return 'hello' in text.lower()
# print(is_hello_in_text('hi'))
#
# def is_string_in_text(string, text):
#     return string in text
# print(is_string_in_text('he', 'The apple'))

# def greenting_depends_on_gender(name, gender):
#     if gender == 'male':
#         print ('Hello ' + name + '! You look great!')
#         return gender
#     elif gender == 'female':
#         print ('Hello ' + name + '! You are so nice')
#         return gender
#     else:
#         print ('Hello ' + name + '! I\'ve neven seen the creature like you!')
#         return gender
# ret_value = greenting_depends_on_gender('Jack', 'male')
# ret_value = greenting_depends_on_gender('Jane', 'female')
# ret_value = greenting_depends_on_gender('creature', 'unkown')
#
#
# Создайте функции cat_voice() and dog_voice(), которые выводят на экран 'Meow!' и 'Woof!' соответственно. Сделайте по одному вызову каждой из функций
def cat_voice():
    print('Meow!')
    return

def dog_voice():
    print('Woof!')
    return

cat_voice()
dog_voice()

# Создайте функции cat_voice() and dog_voice(), которые возвращают значения 'Meow!' и 'Woof!' соответственно. Выведите на экран 'Meow!' и 'Woof!' по 2 раза
cat_voice()
cat_voice()
dog_voice()
dog_voice()
# Создайте функцию get_voice() которая возвращает передаваемый ей в качестве параметра текст c восклицательным знаком.
def get_voice(text):
    return text + '!'
print(get_voice('Hi'))
# Создайте функцию, которая генерирует последовательность нечетных чисел в диапазоне от a до b (a и b включительно). Значения a и b должны передаваться в качестве параметров.
# Результирующая последовательность должна возвращаться в форме объекта list. Решите задание двумя способами - при помощи List Comprehension  и без него

def calc(a, b):
    odd_list = []
    for num in range(a, b+1):
        if num % 2 != 0:
            odd_list.append(num)
    return odd_list
print(calc(1,10))

def calc2(a, b):
    return  [num for num in range(a, b+1) if num % 2 != 0]
print(calc2(1,15))
