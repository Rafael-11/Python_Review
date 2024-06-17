
# Get help from python about any method
# print(help(input))

name=input('Enter your name:\n')
age=input('Enter your age:\n')
gpa=float(input('Enter your GPA:\n'))
enter_boolean=bool(input('Enter True or False:\n'))


print(name)
print(type (name))
print(gpa)
print(enter_boolean)


# print(age+5) # not allowed
print(int(age)+5) # casting into int and concat, you can also cast in input method level. Ex: age=int( input('Enter your age:\n') )
print(type (age))
print(type (gpa))
print(type(enter_boolean))