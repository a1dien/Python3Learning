
#print(pow(10000, 0))
#print(pow(10, 3))


#decimal
x = 127
#pow (10,2) = 100, 2*pow (10, 1) = 20, 7*pow(10,0) = 7
print(pow(10,2) + 2*pow(10, 1) + 7*pow (10,0))
y = 1035
print(1*pow(10,3) + 0*pow(10,2)+ 3*pow(10, 1) + 5*pow (10,0))

#binary
x = 0b101
print(x)
print(1*pow(2,2) + 0*pow(2, 1) + 1*pow (2,0))

y = 0b0110
print(y)
print(0*pow(2,3) + 1*pow(2,2) + 1*pow(2, 1) + 0*pow (2,0))

#hex
z = 0x2af1
print(z)
print(format(z, '0>42b'))
print(0b000000000000000000000000000010101011110001)
print(2*pow(16,3) + 10*pow(16, 2) + 15*pow(16,1) + 1*pow (16,0))