#Infinite process

def create_patterns():
    max_patterns_number = 100
    patterns = ('First pattern', 'Second pattern', 'Third pattern', 'Fourth pattern')
    i = 0
    result_list = []
    while len(result_list) < max_patterns_number:
        if i >= len(patterns):
            i = 0
        result_list.append(patterns[i])
        i += 1
    return result_list

print(create_patterns())

def get_current_pattern():
    patterns = ('First pattern', 'Second pattern', 'Third pattern', 'Fourth pattern')
    i = 0
    while True:
        if i >= len(patterns):
            i = 0
        yield patterns[i]
        i += 1

current_pattern = get_current_pattern()
print(current_pattern.__next__())
print(current_pattern.__next__())
print(current_pattern.__next__())
print(current_pattern.__next__())
print(current_pattern.__next__())

#Создайте функцию, возвращающую генератор, бесконечно вырабатывающий квадраты целых чисел, начиная с 1.

def get_infinite_square_generator():
    i = 1
    while True:
        yield i**2
        i += 1

infinite_square_generator = get_infinite_square_generator()

print(next(infinite_square_generator)) # 1
print(next(infinite_square_generator)) # 4
print(next(infinite_square_generator)) # 9
print(next(infinite_square_generator)) # 16
