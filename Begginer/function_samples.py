'''
Here is some useful methods
You can find more information in
https://www.w3schools.com/python/python_functions.asp
'''


def my_fun():
    print('Hi, from Function')


my_fun()


def my_param_fun(someName):
    print('Loorom ' + someName)


my_param_fun("Zertan")


def my_2param_fun(fname, lname):
    print('Hi, my name is: ' + fname + ' ' + lname)


my_2param_fun('Alireza', 'Ali')

'''
Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly:
Example
If the number of arguments is unknown, add a * before the parameter name:
'''


def my_arbitrary_fun(*fname):
    # this mean the index 2 will be in place from set
    print('Hi, my name is: ' + fname[2])


my_arbitrary_fun('Alireza', 'Ali', 'jj')

'''
Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly:
Example
If the number of keyword arguments is unknown, add a double ** before the parameter name:
'''


def my_function(**kid):
    print("His last name is " + kid["moshi"])


my_function(fname="Tobias", lname="Refsnes", age=44, moshi="hh")

# ------------------------
# Default Parameter Value


def my_defvalue_fun(country="Norway"):
    print("I am from " + country)


my_defvalue_fun("Sweden")
my_defvalue_fun("India")
my_defvalue_fun()
my_defvalue_fun("Brazil")

# -------------------------
# parssing a list


def my_listParser_fun(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry", "Koloche"]

my_listParser_fun(fruits)
# ------------------


def my_zarb_fun(x, y):
    return y * x


print(my_zarb_fun(3, 5))
print(my_zarb_fun(5, 10))
print(my_zarb_fun(9, 25))

# Recursion


def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
