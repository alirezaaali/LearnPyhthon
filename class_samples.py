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


class Studen(Person):
    # Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
    '''
    To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
    class Student(Person):
        def __init__(self, fname, lname):
            Person.__init__(self, fname, lname)
    '''

    def __init__(self, fname, lname, age, stdId):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.stdId = stdId

    # inherited from parent class person
    # def fullname():
    #     Person.fullname()

    def studentId(self):
        return self.stdId

    # pass
    # Note: Use the pass keyword when you do not want to add any other properties or methods to the class.


a = Studen('Beh', 'Sh', 30, 1)
print(a.fullname())

'''
Python also has a super() function that will make the child class inherit all the methods and properties from
its parent:
By using the super() function, you do not have to use the name of the parent element,
it will automatically inherit the methods and properties from its parent.
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
'''


class teacher(Person):
    def __init__(self, fname, lname, age, major):
        super().__init__(fname, lname, age)
        self.major = major

    def WelcomeMsg(self):
        # msg = "welcome Mr/Mrs.", self.fname, self.lname, "In major of", self.major
        msg = "welcome Mr/Mrs.", self.fullname(), "In major of", self.major
        return msg


b = teacher('Hh', 'zz', 55, 'Py')
print(b.fullname())
print(b.major)
print(str(b.WelcomeMsg()).replace('(', '').replace(')', ''))
