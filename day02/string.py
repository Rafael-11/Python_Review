name = 'python'

# length
print(len(name))

# access any element
print(name[0])

# last index
print(name[-1])
print(name[-2])

# slicing string is same substring in Java

s = 'Java Programming language'
s2=s[5:16]
print(s2)

s3=s[:4]
print(s3)

s4=s[:-1]
print(s4)

s5=s[17:-1]
print(s5)

# reverse the string after slicing
s6=s[::-1]
print(s6)

# reverse string in python with function
s7 = 'Python Programming'
reversed(s7)
print(s7)

# slicing from starting

s8 = 'Java is fun'
s9=s8[8:]
print(s9)

# get help with str doc
print(help(str))

print('-------------------------------------------------')

# captalize the first latter of sentence
j='java programming'
j=j.capitalize()
print(j)


print('---------------------------------------------')
# j=j.casefold();
j=j.title()
print(j)

print('------------------------------------------------')

o='     Pyhton    '
o=o.lstrip()
print(o)

print('------------------------------------------------')
s='JAVA'

print(s.index('A'))
print(s.rindex('A'))

print('------------------------------------------------')

s='JAVA JAVA'
s=s.replace('JAVA', 'Python',1)
print(s)

print('-----------------------------------------------')
s='C# C# Python'
s=s.replace(' C#',' Java')
print(s)

print('------------------------------------------------')

s='Java Java C#  C# Python C#'
cout_java=s.count('Java')
coun_python=s.count('Python')
print(cout_java)
print(coun_python)

print('------------------------------------------------')

# compare 2 objects
s1='JAVA'
s2='java'

print(s1.lower()==s2.lower()) # ignore case
print(s1.upper()==s2.upper()) # ingore case

print('------------------------------------------------')
s='Java'
print(s[1].islower())
print(s[0].isupper())

# is Digit

s='a'
print(s.isdigit())

# is title
s='Java Programing'
print(s.istitle())





