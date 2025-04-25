"""
Create a python file named grade, a variable named grade is given. write a program to print the following messages:
            'A': excellent
            'B': great job
            'C': good
            'D': passed
            'F': failed
            other wise: invalid

            NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT
"""

grade = input('Enter your grade: ')
if grade == 'A' or grade=='B' or grade=='C' or grade=='D' or grade=='F':
    if grade == 'A':
       result='Excellent'
    else:
       if grade=='B':
        result='Great job'
       else:
           if grade=='C':
              result='Good'
           else:
               if grade=='D':
                  result='Passed'
               else:
                   if grade=='F':
                      result='Failed'
else:
    result='Invalid'

print(result)
