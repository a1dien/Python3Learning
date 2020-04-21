# #input
# x = input ('Input something')
#
# #output
# print('Output something ' + x)
#
#

# lorem_ipsum_text = open('C:/Users/Val/Downloads/original.txt', 'r')
# for line in lorem_ipsum_text:
#     print(line,end='')
# lorem_ipsum_text.close()

# print (1, 2, 3, sep=':', end = '\n')
# print (1, 2, 3, sep=',', end= ' ')
# print (1, 2, 3, sep=';', end= '')


# lorem_ipsum_text = open('C:/Users/Val/Downloads/original.txt', 'r')
# for line in lorem_ipsum_text:
#     if 'let' in line:
#         print(line,end='')
# lorem_ipsum_text.close()

# with open ('C:/Users/Val/Downloads/original.txt', 'r') as lorem_ipsum_text:
#  for line in lorem_ipsum_text:
#      if 'let' in line:
#          print(line,end='')

# with open ('C:/Users/Val/Downloads/original.txt', 'r') as lorem_ipsum_text:
#     line = lorem_ipsum_text.readline()
#     while line:
#         print(line, end = '')
#         line = lorem_ipsum_text.readline()

# with open ('C:/Users/Val/Downloads/original.txt', 'r') as lorem_ipsum_text:
#     lines = lorem_ipsum_text.readlines()
# print(lines)
#
# for line in lines[::-1]:
#     print(line)


with open ('C:/Users/Val/Downloads/original.txt', 'r') as lorem_ipsum_text:
    text = lorem_ipsum_text.read()
print(text)