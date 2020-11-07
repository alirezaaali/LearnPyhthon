'''
Here is some useful methods
You can find more information in
https://www.w3schools.com/python/python_classes.asp
'''
'''
The self Parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
'''


class Person:
    # Note: The __init__() function is called automatically every time the class is being used to create a new object.
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def fullname(self):
        return(self.fname + ' ' + self.lname)

    def myAge(self):
        return(self.age)


p1 = Person('Alireza', 'Ali', 38)
print(p1.fullname())
print(p1.myAge())
p1.age = 55
print(p1.myAge())
# del p1
