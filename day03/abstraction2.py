import numbers
from abc import ABC, abstractmethod

class Volume(ABC):
    @abstractmethod
    def volume(self):
        pass


class Shape(ABC):

    """
    abc : module name (built-in module)
    ANC: abstract class in abc module
    abstractmethod: annotation that can be given to abstract method
    """
    def __init__(self):
        self.name = type(self).__name__
    @abstractmethod
    def area(self) -> numbers:
        pass

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'

class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self) -> numbers:
        return self.side * self.side

square1 = Square(5)
print(square1)
print(square1.area())

class Circle(Shape):

    def area(self) -> numbers:
        pass


class Rectangle(Shape):

    def area(self) -> numbers:
        pass


class Cube(Shape,Volume):

    def area(self) -> numbers:
        pass

    def volume(self):
        pass


class Clyinder(Shape,Volume):

    def area(self) -> numbers:
        pass

    def volume(self):
        pass