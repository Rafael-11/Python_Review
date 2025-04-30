from assignments.day01_assignments.Rectangle import length

s='Python programming'

for each in s:
    print(each)

print('-----------------------')

for i in range(0, len(s)):
    print(i)

print('-----------------------')

for i in range(0, len(s)):
    print(s[i])

print('-----------------------')

for i in range(-len(s), 0):
    print(i)

print('-----------------------')

for i in range(-len(s), 0):
    print(s[i])

# reverse index number
print('-----------------------')

for i in reversed(range(0,len(s))):
    print(i)
# reverse chars
print('-----------------------')

for i in reversed(range(0,len(s))):
    print(s[i])


print('-----------------------')

for x in s[::-1]:
    print(x)

print('-----------------------')

for x in range(1,11):
    print('Hello World')

print('-----------------------')

num = int(input('Enter a positive number:\n'))

while num <=0:
    num = int(input())

print(f'You have entered {num}')

print('-----------------------')
answer = input('Enter yes or no:\n')
while not (answer.lower() == 'yes' or answer.lower() == 'no'):
    answer = input('Enter yes or no:\n')
print(f'You have entered {answer}')


