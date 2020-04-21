#Method Resolution Order (MRO)

#    A
#   /\
#  B C
#  \/
#  D

class A:
    def some_method(self):
        print ('Method of class A')

class B(A):
    def some_method(self):
        print ('Method of class B')

class C(A):
    def some_method(self):
        print ('Method of class C')

class D(B,C):
    pass
#    def some_method(self):
#        print ('Method of class D')

#___mro___, mro(), help()
some_object = D()
some_object.some_method()

print(D.__mro__)
print(D.mro())
help(D)