from operator import index

unique_elements=set()

unique_elements.add(10)
unique_elements.add(10)
unique_elements.add(10)
unique_elements.add(20)
unique_elements.add(20)

print(type(unique_elements))
print(unique_elements)

#print(unique_elements[1]) set dose not have index

# can not be sliced as well
# unique_elements[:2]

# remove()
unique_elements.remove(10)
print(unique_elements)

# update()
unique_elements.update({1,2,3,4,5,1,2,3,4,5})

print(unique_elements)

# pop()

n=unique_elements.pop()
print(unique_elements)

#print(help(set.pop))

print(n)

print('-----------------difference-----------')
# difference(): compare the 2 sets and return a new set which contains the items that only exist in first set
s1={'Java','Python','C#'}
s2={'Ruby','Java','C++','Swift'}

diff=s1.difference(s2)
print(diff)

print('-----------------Intersection----------------')
# intersection(): compare two sets and returns a new set which contains common elements of two sets

set1={'Java','Python','C#','Cydeo'}
set2={'C++','Ruby','Swift','Java','Python',}

df=set1.intersection(set2)
print(df)

print('-----------------different_update----------------')
# different_update(): removes the elements of the first set that exist in the second set
a1={'Book','Pen','Apple','Cherry','Coffee'}
a2={'Book','Apple','Banana','Grape','TV'}
a1.difference_update(a2)
print(a1)

print('-----------------intersection_update----------------')
b1={'Cydeo','Python','Java','C#','Wooden Spoon','Ruby','Swift'}
b2={'Wooden Spoon','Python','Cydeo'}

b1.intersection_update(b2)
print(b1)

print('-----------------symmetric_difference----------------')
# symmetric_difference(): Compare two sets and returns a new set which contains all elements except the common once

c1={'Apple','Banana','Cherry'}
c2={'Grape','Strawberry','Banana','Mango','Lemon','Apple'}

symmetric_difference=c1.symmetric_difference(c2)
print(symmetric_difference)


