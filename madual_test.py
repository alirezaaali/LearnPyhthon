'''
Here is some useful  methods
You can find more information in
https://www.w3schools.com/python/python_modules.asp
What is a Module?
Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.


'''
#import iterator as ite
#import class_samples as myc
import platform as pl

# z = ite.myclass(1, 4)
# myit = iter(z)

# for x in myit:
#     print(x)


# n = myc.Studen('aa', 'bb', 44, 55)
# print(n.fullname())

print('this is architecture():', pl.architecture())
print('this is machine():', pl.machine())
print('this is computer name using node():', pl.node())
print('this is CPU name using processor():', pl.processor())
print(dir(pl))
