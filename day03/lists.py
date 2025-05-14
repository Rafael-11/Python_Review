grocery_list=['Eggs','Cucumber','Water']

grocery_list.append('Tomato')
grocery_list.extend(('Beef','Lamb','Orange'))
print(len(grocery_list))
print(grocery_list)

grocery_list[-2]='Cherry'
print(grocery_list)

print('--------------------')
numbers_list=[10,20,30,40,50,60,70,80]
print(numbers_list)
numbers_list[2:-2]=[3000,4000,5000,6000]
print(numbers_list)

characters_list=['A','B','C','D','E','F','G','H']
list1=characters_list[2:len(characters_list)-3]
print(list1)

list2=characters_list[:4]
print(list2)

list3=characters_list[2:]
print(list3)

characters_list[2:5]=['I','J','K','L','M','N','O','P']
print(characters_list)

print('--------------------')

names=['Jack','Mia','Charles','Alim']
for x in names:
    print(x)
nums=[10,20,30,40,50]

for i in range(0,len(nums)):
    nums[i]=int(nums[i]/5)
print(nums)

print('--------------------')
# backwards
nums=[10,20,30,40,50,60]

for i in reversed(range(len(nums))):
    print(nums[i])

print('--------------------')
# easy way

for i in nums[::-1]:
    print(i)
print('--------------------')
# with reserve()

for i in reversed(nums):
    print(i)
print('--------------------')
# with While loop, not recommend to use in list.

i=0
while i<len(nums):
    print(nums[i])
    i+=1
print('--------------------')

for i in range(1,6):
    i+=2
    print(i)
print('--------------------')

# sort()

nums=[40,50,700,9,10,8,0]
#nums.sort() # sorted in acsending order
# descending order
nums.sort(reverse=True)
print(nums)

print('--------------------')

list1=[10,20,30,40]
# list1=list1(reversed(list1))
list1.reverse()
print(list1)

print('--------------------')

tuple_elements=('Java','Python','C#','Ruby')
list_elements=list(tuple_elements)
list_elements[-2]='C++'
list_elements.append('SWIFT')
print(list_elements)

# convert list to tuple
tuple_elements=tuple(list_elements)
print(tuple_elements)

list1=[1,2,3,4,5]
list2=[1,2,3,4,5]
print(list1 is list2) # False

tuple1=(1,2,3,4,5)
tuple2=(1,2,3,4,5)
print(tuple1 is tuple2) # True

print('--------------------')

grocery_list=['Eggs','Cucumber','Water']

grocery_list.append('Tomato')
grocery_list.extend(('Beef','Lamb','Orange'))
print(grocery_list)
grocery_list.remove('Beef')
print(grocery_list)

print('--------------------')

grocery_list.insert(2,'Tomato')
print(grocery_list)

print('--------------------')

print(grocery_list.index('Tomato'))
print('-----------Comprehensions---------')

nums=[]

for x in range(1,51):
    nums.append(x)
print(nums)
print('--------------------')
"""
divisible_by_5=[]
for x in nums:
    if x % 5 == 0:
        divisible_by_5.append(x)
print(divisible_by_5)
"""

divisible_by_5=[x for x in nums if x % 5 == 0]
print(divisible_by_5)
print('--------------------')

even_numbers=[x for x in nums if x % 2 == 0]
odd_numbers=[x for x in nums if x % 2 != 0]
print(even_numbers)
print(odd_numbers)
print('--------------------')

names=['Python','Java','Java','Ruby','C#']
names=[x for x in names if x.lower() !='java']
print(names)













