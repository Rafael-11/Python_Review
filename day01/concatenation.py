name = 'James'
age = 26

# plus+ should be used only when the 2 variable is string
print('Name is '+name)
# print('Age is '+age) # can only concatenate str (not "int") to str

# format() for concatenation for str and int
print('Age is {}'.format(age))

print('My name is {} and I am {} year old'.format(name,age))

# easy way for format()
print(f'My name is {name} and I am {age} year old')

print('Python', 3, 'is good:', True)
