a = 21
b = 10
c = 0

print("**** Comparison operators ****")
print("a = ", a)
print("b = ", b)
print("c = ", c)
if (a == b):
    print("Line 1 - a is equal to b")
else:
    print("Line 1 - a is not equal to b")

if (a != b):
    print("Line 2 - a is not equal to b")
else:
    print("Line 2 - a is equal to b")

if (a < b):
    print("Line 3 - a is less than b")
else:
    print("Line 3 - a is not less than b")

if (a > b):
    print("Line 4 - a is greater than b")
else:
    print("Line 4 - a is not greater than b")

a = 5;
b = 20;
print("a = ", a)
print("b = ", b)
if (a <= b):
    print("Line 5 - a is either less than or equal to  b")
else:
    print("Line 5 - a is neither less than or equal to  b")

if (b >= a):
    print("Line 6 - b is either greater than  or equal to b")
else:
    print("Line 6 - b is neither greater than  or equal to b")

print("\n")
print("**** Assignment operators ****")
a = 21
b = 10
c = 0

print("a = ", a)
print("b = ", b)
print("c = ", c)
c = a + b
print("Line 1 - Value of c is ", c)

c += a
print("Line 2 - Value of c is ", c)

c *= a
print("Line 3 - Value of c is ", c)

c /= a
print("Line 4 - Value of c is ", c)

c = 2
c %= a
print("Line 5 - Value of c is ", c)

c **= a
print("Line 6 - Value of c is ", c)

c //= a
print("Line 7 - Value of c is ", c)

print("\n")
print("**** Membership operators ****")
list1 = ['hola', 'Bobby', 'arbol', 'futbol', '123']
print("list1 = ",list1)
if 'arbol' in list1: print('"arbol" exists in list1')
if '1234' not in list1: print('"1234" does not exist in list1')

print("\n")
print("**** Identity operators ****")

a = 'hola'
b = 'hola'
c = 'Jalasoft'

print("a = ", a)
print("b = ", b)
print("c = ", c)

if a is b: print ('a is b')
else: print ('a is not b')

if a is c: print('a is c')
else: print ('a is not c')

if b is c: print('b is c')
else: print ('b is not c')

if a is not b: print ('a is not b')
else: print ('a is b')

if a is not c: print ('a is not c')
else: print ('a is c')

if b is not c: print ('b is not c')
else: print ('b is c')