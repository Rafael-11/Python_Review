days=("Mon","Tues","Wed","Thurs","Fri","Sat","Sun",1,2,3,4,5, True, False)
print(type(days))
print(len(days))

print(days)

#days[0]='Java'
#print(days)

print(days[0])
print(days[-1])

days=("Mon","Tues","Wed","Thurs","Fri","Sat","Sun")

#workdays=days[1:-3]
workdays=days[1:4]
print(workdays)

weekdays=days[:-2]
print(weekdays)

weekend=days[-2:]
print(weekend)

# Verify tuples
# == , is
tuple1=(1,2,3)
tuple2=(1,2,3)
print(tuple1==tuple2)
print(tuple1 is tuple2)

#merge tuples
tuple3=tuple1+tuple2
print(tuple3)

#multiply tuple
tuple4=tuple1*5
print(tuple4)

reversed_tuple1=days[::-1]
print(reversed_tuple1)

reversed_tuple2=tuple(reversed(days))
print(reversed_tuple2)

# index() in tuple

print(days.index('Wed'))

numbers=(10,10,10,10,20,30,40,50,10)
print(numbers.count(10))

for x in days:
    print(x)
for x in range(0,len(days)):
    print(x)
print('------------------------------')
for x in reversed(range(0,len(days))):
    print(x)



