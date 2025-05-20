from functools import reduce

print('-------------closure----------------------')

def display_message():


    def method():
            print('Hello world')
            print('Hello again')

    method()
    method()
    method()
    method()

print(display_message())

print('--------------------')


def display_palindrome(strings: list):


     def is_palindrome(s: str) -> bool:
         return s[::-1].lower() == s.lower()

     for s in strings:
         if is_palindrome(s):
             print(s)
print('-----------map--------------------')

nums=[10,20,30,40,50,60,70,80,90]

nums=list(map(lambda x: x *10,nums))
print(nums)

names = ['Java','java','pyThon','python','ruby']

names = list(map(lambda s: str(s).upper(),names))
print(names)

print('----------------filter----------------')



nums=[1,2,3,4,6,7,8,9,10,11,12,14,15,16,17,18,19,20]

nums=list(filter(lambda x: x % 5==0, nums))
print(nums)

names = ['Java','java','pyThon','python','ruby']

# remove any word which is not started with J/j

#names=[a for a in names if a.lower().startswith('j')]

names=list(filter(lambda x: str(x).lower().startswith('j'), names))

print(names)

print('--------------reduce-----------')

list1=[1,2,3,4,5,6,7,8,9]

print(reduce(lambda x, y: x+y, list1) )


list2=['Java','python','Ruby','C#']

print(reduce(lambda x, y: f'{x}+{y}', list2))

