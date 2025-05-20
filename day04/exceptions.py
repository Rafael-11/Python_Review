try:
    num =10/0
    print(num)
except:
    print('Something went wrong')
else:
    print('No error')
finally: # this finally block always executed.
    print('Finally block')

print('Test is completed')

print('---------------------')

tuple1=(10,20,30,40.,50)
try:
    print(tuple1[2000])
except: # if you specify exception type, if it does not match, it will give you error.
    print('Index number too large')
else:
    print('Index number is valid')

print('---------------------')

try:
    raise FileNotFoundError('No such file error')
except SyntaxError:
    print('Syntax error')
except OSError:
    print('OS error')
except ArithmeticError:
    print('Arithmetic error')

