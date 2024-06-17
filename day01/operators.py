# arithmetic: +, -, *, /,

print(10-2)
print(10+2)
print(10 * 2)
print(10 / 2) # in python, you will get always float or double number in division op
print(10 % 3)

print(100 / 2 ) # will get float
print(int(100 / 2) ) # will get int

# shorthand assignment operators: =, +=, -=, *=, /=, %=

a=100
a=200 # updated value of a

print(a)

a+=100

print(a)

a-=50
print(a)

# Division operator always give float even if divided even number
a /=2
print(a) # will give float
print(int(a)) # will give int num

# logical operators: &&, ||, ! --> Java
# Python: and, or, not

s='Hello world'
print('H' and 'w' in s)

print(True and True)
print(True or False)
print (False and True)

s='Java Python C# c++'

print('Java' or 'Ruby' in s)
age=29
citizen_ship='USA'
is_elig= age >= 18 and citizen_ship=='USA'

print(is_elig)

# in or not in operator

has_java='Java' in s
print(has_java)
# in Java ! contains() but in Python will use 'not in'
print('Python' not in s)

print( not True)
print(not False) # same ! in java, ex: !true

# identity operator in Python

print('-------------------------------')
# It is pointing the same object
s='Java'
s2='Java'

print(s is s2) # == in Java, checking two variable if it is referring to same objects.




