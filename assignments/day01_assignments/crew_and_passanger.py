"""
Create a python file named crew_and_passanger, Given a number of people on the ship,
determine how many need to be crew members and how many can be passengers. Print how many of each type there should be.

            Total: 50  ====> 20 crew, 30 passengers
            Total: 75  ====> 25 crew, 50 passengers
            Total: 100 ====> 30 crew, 70 passengers
            Any other number of people on the ship is not valid

            NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT
"""

total=int(input("Enter the number of people on the ship: "))
if total == 50 or total == 75 or total == 100:
    if total == 50:
        result='20 crew, 30 passengers'
    else:
        if total == 75:
            result='25 crew, 50 passengers'
        else:
            if total == 100:
               result='30 crew, 75 passengers'
else:
    result='Invalid'

print(result)


