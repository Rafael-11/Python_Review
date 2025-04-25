"""
Create a python file named browser. Write a program that can display the name of selected browser
        1. declare a String variable named browser_name
        2. Assume that the valid browsers are: chrome, firefox, opera, safari, edge.
        3. if the browser name does not match with the valid browser names, out put should be: Invalid Browser Name

        Ex:
            String browser = "chrome";

        Output:
            Chrome Browser is selected

        Note: MUST use nested if
"""

browser_name = input('Enter browser name: ')
if browser_name == 'chrome' or browser_name == 'firefox' or browser_name == 'opera' or browser_name == 'safari' or browser_name == 'edge':
    if browser_name == 'chrome':
       result = 'Chrome browser is selected'
    else:
        if browser_name == 'firefox':
            result = 'Firefox browser is selected'
        else:
            if browser_name == 'opera':
                result = 'Opera browser is selected'
            else:
                if browser_name == 'safari':
                    result = 'Safari browser is selected'
                else:
                    if browser_name == 'edge':
                        result = 'Edge browser is selected'
else:
    result='Invalid Browser Name'

print(result)