

employee1 ={}

employee1['Name'] = 'Jimmy'
employee1['Name'] = 'Denny'
employee1['Age'] = 45
employee1['salary']=100_000

print(employee1)

employee2 = {
    'Name': 'Jimmy',
    'Age': 29,
    'salary': 90_000,
    'full_time': False

}

print(employee2)
print(employee2['Name'])

employee2['salary']=100_000

print(employee2)

employee2.update({'age':40})
print(employee2)

employee2['full_time'] = True
print(employee2)

employee2.pop('full_time')
print(employee2)

employee2.popitem() # LIFO
print(employee2)

l=employee2.copy()
print(l)

print(employee2 is l)


print('--------------------Iterating dictionary-------------')

employee3={
    'Name': 'Shay',
    'Age': 21,
    'salary': 110_000,
    'full_time': False,
    'job_title': 'Engineer',
    'company':'Apple Inc'

}

print(list(employee3.keys()))

for key in employee3.keys():
    print(f'{key}: {employee3[key]}')

print('---------------------')

values=list(employee3.values())

print(values)

for value in employee3.values():
    print(value)

print('---------------------')

for x in employee3.items():
    print(f'{x[0]}: {x[1]}')


students = {
    'A01':{
        'name':'Jimmy',
        'gpa': 3.5,
        'gender':'male',
        'subject':['Math','History']
    },
    'A02': {
        'name': 'Karla',
        'gpa': 3.8,
        'gender': 'female',
        'subject': ['Biology', 'Sceince']
    },
    'A03': {
        'name': 'Tim',
        'gpa': 3.9,
        'gender': 'male',
        'subject': ['Chemisry', 'Programming']

    }
}

print(students)
students['A01']['gpa']=2.5
print(students)

students['A01'].update({'name':'Denny','gender':'male'})
print(students)

students['A03']['subject'][1]='Biology'
print(students)

print('-------------------------')

for x in students.items():
    print(x[1])
    for y in x[1]:
        print(y)
print('-------------------------')

for value in students.values():
    print(value)
    for item in value.items():
        print(item[1])
