smile = '\U0001f600'
list = []
for _ in range(10):
    list.append(smile)
    print (list)

for num in range(10):
    count = 0
    smile = ''
    while count <= num:
        smile += '\U0001f600'
        count += 1
    print(smile)

smile = '\U0001f600'
for num in range(1,11):
    print(smile*num)

