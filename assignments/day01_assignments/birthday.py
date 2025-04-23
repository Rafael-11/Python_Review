"""
9. Create a python file named birthday and create the following variable
             name, birthDay, birthMonth, birthYear

             use concatenation to display the birthday of the person

                 if  name = "John"
                     birth_day = 25
                     birth_month = "April"
                     birth_year = 1995;

                 output:
                     John was born on April/25/1995.
"""

name = 'John'
birth_day = 25
birth_month = 'April'
birth_year = 1995

if name == 'John' and birth_day == 25 and birth_month ==  'April' and birth_year == 1995:
    pass
print(name,'was born on',birth_month+'/'+str(birth_day)+'/'+str(birth_year)+'.')
