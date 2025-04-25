"""
Create a python file named age_groups, write a program that asks user to enter thier age and define the age groups of the user
            age groups are:
                    Teenager (< 21)
                    Adult   (>=21 && <55 )
                    Senior  ( > 55 )

             if age is negative or greater than 150, print invalid

             NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT
"""


age = int(input('Enter your age: '))
if 0 <= age <= 150:
    if age < 21:
        result = "Teenager"
    else:
        if age < 55:
            result = "Adult"
        else:
            result = "Senior"
else:
    result = "Invalid"

# Only one print statement
print(result)
