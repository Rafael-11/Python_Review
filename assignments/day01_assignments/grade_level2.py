"""
14. Create a python file named grade_level2.  write a program that asks user to enter the grade level number,  determine and print which school type the person is in is in.
            grade level and types are:
                    1-5: Elementary school
                    6-8: Middle school
                    9-12: High school
                    13-16: College
                    17-18: Grad School

                    For Any Other grade: Invalid grade level given

            NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT
"""

grade_level=int(input('Enter your grade level number:'))
if grade_level >= 1:
    if grade_level <= 5:
        result='Elementary school'
    else:
        if grade_level >= 6:
            if grade_level <= 8:
                result='Middle school'
            else:
                if grade_level >= 9:
                   if grade_level <= 12:
                    result='High school'
                   else:
                       if grade_level >= 13:
                           if grade_level <= 16:
                              result='College'
                           else:
                               if grade_level >= 17:
                                   if grade_level <= 18:
                                     result='Grad School'
                               else:
                                   result='Invalid grade level given'
else:
    result='Invalid grade level given'
print(result)



