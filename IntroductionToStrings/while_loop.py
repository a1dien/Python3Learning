x = 5
# while x >= 1:
#     print(x)
#     x -= 1 # x = x -1
# while x < 10:
#     print(x)
#     x += 1 # x = x + 1
# while x > 0:
#     x -=2
#     print(x)
#
# while x < 10:
#     print('x is less than 10')
#     x += 1
# else:
#     print('x not is not less than 10')
#
# for x in range(0,10):
#     print(str(x) + ' x is less than 10')
# else:
#     print(str(x) + ' x is not less than 10')

#break, continue, pass
my_list = [1, 2, 3]
# for item in my_list:
#     pass
# print('Another code')
# for item in my_list:
#     if (item == 2):
#         break
#     print(item)

for item in my_list:
    if item == 2:
        continue
    print(item)

#При помощи функции randint() из модуля  random генерируйте числа в диапазоне от 1 до 10 и помещайте в список, до тех пор пока не будет сгенерировано число 7.
# Распечатайте содержимое списка.
from random import randint
list = []
while True:
    random = randint(1,10)
    if random == 7:
        break
    list.append(random)
print(list)
