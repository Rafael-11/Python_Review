"""
13.  Create a python file named grade_level1.  write a program that asks user to enter the grade level number,  determine and print which school type the person is in is in.
            grade level and types are:
                    1-5: Elementary school
                    6-8: Middle school
                    9-12: High school
                    13-16: College
                    17-18: Grad School

              Assume that the given number is 1 ~ 18
"""

level = int(input('Enter your grade level number: '))
if level == 1 or level == 2 or level == 3 or level == 4 or level == 5:
    print('Elementary school')
elif level == 6 or level == 7 or level == 8:
    print('Middle school')
elif level == 9 or level == 10 or level == 11 or level == 12:
    print('High school')
elif level == 13 or level == 14 or level == 15 or level == 16:
    print('College ')
elif level == 17 or level == 18:
    print('Grad School')



