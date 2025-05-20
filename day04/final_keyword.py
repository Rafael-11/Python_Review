from typing import final


"""
Uppercase for var can be sign of constant vars

PI= 3.14
"""
pi: final = 3.14

pi=3.4

@final
class Animal:
    pass
class Dog(Animal):
      pass
# got warning that 'final' class can not be extended
# final method also can not be overriden


class Employee:
      @final
      def work(self):
          print('Working')

class Driver(Employee):
      def work(self):
          print('Working')


class Person:

    def __init__(self, age: int):
           self.__age = age

    @property
    def person_age(self):
        return self.__age
        
    @person_age.setter
    def person_age(self, value):
       raise RuntimeError(f' age is constant and cannot be changed')








