import os
'''
Here is some useful methods
You can find more information in
https://www.w3schools.com/python/python_file_handling.asp
'''
# ----OPEN and READ
# myFile = open('test.txt', 't')
# myFile = open('test.txt', 'rt')
# print('File name is: ', myFile.name)
# print('only first 10 characters: \n', myFile.read(10))
# print('Whole file read is: \n', myFile.read())
# print('Read one line:: \n', myFile.readline())
# print('Read one line:: \n', myFile.readline())
# print('Read one line:: \n', myFile.readline())
# for x in myFile:
#     print(x)

# myFile.close()

# ----CREATE
# myFile = open('textss.txt', 'w')
# myFile.write(
#     'this is my first simple file operation in python\n , which is agreat experience.\n I hope I learn more about: \t Python \t and it`s liberaries.')
# myFile.close()

# myFile = open('textss.txt', 'rt')
# print(myFile.read())
# myFile.close()

# ----DELETE_FILE
# os.remove('test.txt')

print(os.getcwd()+'\\logfiles\\')
