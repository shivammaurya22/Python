"""Membership, identity, and logical operations Membership operators (in, not in) test for variables in sequences, such as lists or strings do what you would expect, x in y returns True if a variable x is found in y. The is operator compares object identity. For Example:--->"""

x = [1,2,3,4]; y = [1,2,3,4]
print(x==y) # equivalence
print(x is y) #object identity
#print(x = y) # assignment operator
print(x is y) # returns True

z = 3 + 4j
print(int(z.real))
print(int(z.imag))
print(1-0.9)
print(0.09999999999999998 == 0.1)
print(1-0.9 == 0.1)