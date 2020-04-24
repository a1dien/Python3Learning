# print(sum([number for number in range(10)]))
# print(sum(number for number in range(10)))

import time
start_time = time.time()
print(sum([number for number in range(10000000)]))
processing_time = time.time() - start_time
print(processing_time)

start_time = time.time()
print(sum(number for number in range(10000000)))
processing_time = time.time() - start_time
print(processing_time)