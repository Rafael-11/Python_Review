"""
Create a python file named fizz_buzz, write a program that asks user to enter an integer and prints "Fizz" if the number is divisible by 3, prints "Buzz" if the number is divisible by 5, and prints FizzBuzz if the number is divisible by both 3 and 5.

            Ex:
                number 15

            Output:
                FizzBuzz
"""

intNum = int(input("Enter an integer: "))

if intNum % 3 == 0 and intNum % 5 == 0:
    print("FizzBuzz")
elif intNum % 3 == 0:
    print("Fizz")
elif intNum % 5 == 0:
    print("Buzz")
else:
    print("Invalid Number")
