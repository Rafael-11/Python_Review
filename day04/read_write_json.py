import json
import csv

path='files/Test.json'

jason_file=open(path,'r')


dictionary = json.load(jason_file)
print(dictionary)
print(type(dictionary))

for x in dict(dictionary).keys():
    print(x)


jason_file.close()

print('-------Write Json file------------')

dictionary['name']='Aaron King'
dictionary['age']=28

print(dictionary)

open('files/Test.json','w').write(json.dumps(dictionary))


json_file=open('files/Test2.json','w')
json_obj=json.dumps(dictionary, indent=2)
json_file.write(json_obj)
json_file.close()

"""
Web Automation:
    BeautifulSoap
    request
    pytest
    robot
Web Development:
    Django
    Flask
    FastAPI
    .....
"""

