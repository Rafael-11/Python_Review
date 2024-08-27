"""
Java Methods:
      public static void main(String[] args) {

         }


"""
import numbers


def display_message():
    print("Hello World!")
    print("Hello Cydeo!")


display_message()

print("---------------------------------")


def value():
    return "Hello Cydeo!"


print(value())

print('------------------------------------')


def return_int() -> int:
    return 42


print(return_int())


def return_str() -> str:
    return "Hello Cydeo!"


print(return_str())

print('------------------------------------')


def square(num):
    return num * num


print(square(10))


def divide(num1, num2):
    return num1 / num2


print(divide(100, 20))

print('-------------------------------------------------')


def add(num1: int, num2: int) -> int:
    return num1 + num2


print(add(10, 20))

print('---------------------------------------')


def add(num1: numbers, num2: numbers) -> numbers:  # double or float
    return num1 + num2


print(add(10.8, 20.9))

print('---------------------------------------')


def cal(num1: numbers, num2: numbers, operator: str) -> numbers:
    if operator == '-':
        return num1 - num2
    elif operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print('Operator Error')
        return 0


print(cal(10, 20, '+'))
print(cal(10, 20, '/'))

print('---------------------------------------')


# example of method overloading
def sum(n1: numbers, n2: numbers, n3: numbers = 0, n4: numbers = 0) -> numbers:
    return n1 + n2 + n3 + n4


print(sum(10, 20, ))
print(sum(30, 20, 50))
print(sum(10, 20, 50, 60))

print('-------------------------------------------------')


# Method in python should inside the class

class test:
    def method(self):
        pass
