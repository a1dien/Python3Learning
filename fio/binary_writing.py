#with open('C:\Users\Val\Downloads\mest_binary', 'bw') as test_file:
with open('test_binary', 'bw') as test_file:
    # for number in range(21):
    #     test_file.write(bytes([number]))
    test_file.write(bytes(range(21)))


with open('test_binary', 'br') as test_file:
    for number in test_file:
        print(number)
