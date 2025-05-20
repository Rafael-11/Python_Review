import os

path='/Users/rafaelp/PycharmProjects/Python_Review/day04/files/Test.txt'

text_file=open(path,'r')
# reading all lines
print(text_file.read())
# reading line by line
# print(text_file.readline())
# print(text_file.readline())

text_file.close()

print('----------Create file---------')

path='files/Test2.txt'
text_file=open(path,'w')
text_file.write('This is a new text file\nPython created this file')

print('-----------Remove file-----------')

os.remove(path)


