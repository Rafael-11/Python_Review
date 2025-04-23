"""
8. create a python file named phone_number and declare the following variables:
            countryCode, areaCode, localNumber

            use string concatenation to display the phone number
            ex:
                if  country_code = 1
                    area_code = 703
                    localNumber = 4512625

                output:
                    Your phone number is +1(703)-4512625
"""

countrycode=1
areacode=703
localNumber=4512625

if countrycode ==1 and areacode== 703 and areacode == 4512625:
    pass
else:
    print('Your phone number is','+' + str(countrycode)+'('+str(areacode)+')'+'-'+str(localNumber))


