nested = [[1,2,3],[4,5,6],[7,8,9],[10,11,12,13], ['hello', True], 'end']
print(nested)
print(len(nested))
print(len(nested[3]))
print(nested[1][1])

#get 12
print(nested[3][-2])
print(nested[-1][-2])
print(nested[-1][2])

#print all
for inner_list in nested:
    for num in inner_list:
        print(num)

[print(inner_list) for inner_list in nested]
[[print(num) for num in inner_list] for inner_list in nested] #short
