class Person:
    def __init__(self,name:str,age:int):
        self.__name=None
        self.__age=None
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
        if self.__name is None or self.__name == '' or type(self.__name) !=str:
            raise RuntimeError(f'Invalid name has been set: {self.__name}')
        return self.__name

    def set_name(self,name:str):
        if  type(name) !=str:
            raise RuntimeError(f'Person name must be a string')
        if name == '':
            raise RuntimeError(f'Person name cannot be empty')
        self.__name=name

    def get_age(self)->int:
        return self.__age

    def set_age(self,age):
        if age < 0 or age > 150:
            raise RuntimeError(f'Invalid age {age}')
        self.__age=age

    def __str__(self):
        return f'{type(self).__name__}{type(self).__dict__}'


person1=Person('Kayl', 42)
# person1.set_name(123)
# person1.set_name(' ')
# person1.set_name('Jimmy')
print(person1.get_name())
print(person1.get_age())

print('----------------------')



