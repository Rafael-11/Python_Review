
if False:
    print('Python Programming')
# } same in java, we will use indentation in Python
print('Java Programming')


score=70
if score >=60:
# must include code fragment if not give pass keyword
    print('Congrats! you pass the exam!')

s='Hello world'

if 'H' and 'w' in s:
    print(s, ' has', 'J and w')

if score >=60:
    print('Passed')
else:
    print('Failed')

print('-----------------------------')

age=20
result=None

if age >= 21:
    result= 'Eligible'
else:
    result='Not Eligible'
print(result)

print('-------------------------')

# ternary:
age=26
result= 'Eligible' if age >=21 else 'Not Eligible'
print(result)

"""
Multi-branch if-statement 
"""
print('---------------------')

num = 100
result=None

if num > 0:
    result='Positive'
elif num < 0: # elif is same as else if in Java
    result='Negative'
else:
    result='Zero'

print(result)

print('----------------------------')
# convert above code to Ternary
num=200

result2 = 'Positive' if num >= 0 else 'zero'
print(result2)

print('----------------------------')

# Nested if

score = -300


# if score >= 0 and score <=100: is allowed but complicated
if 0 <= score <=100: # Preferable in Python

    if score >= 60:
        print('Pass')
    else:
        print('Fail')
else:
    print('Invalid score')

print('----------------------------')

# More nested if_statement

score = 95

if 0 <= score <=100:
    if score >=90:
        print('A')
    elif score >=80:
        print('B')
    elif score >=70:
        print('C')
    elif score >=60:
        print('D')
    else:
        print('F')
else:
    print('Invalid score')


