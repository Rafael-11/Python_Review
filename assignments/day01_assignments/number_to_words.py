"""
Create a python file named number_to_words, Write a program that can convert user entered number (from 0~9) to words.

    NOTE: MUST use ternary
"""

num = int(input("Enter a number (0-9): "))
word = "Zero" if num == 0 else \
       "One" if num == 1 else \
       "Two" if num == 2 else \
       "Three" if num == 3 else \
       "Four" if num == 4 else \
       "Five" if num == 5 else \
       "Six" if num == 6 else \
       "Seven" if num == 7 else \
       "Eight" if num == 8 else \
       "Nine" if num == 9 else \
       "Invalid"
print(word)

"""
value_if_true if condition else value_if_false
"""
