'''
Here is some useful methods
You can find more information in
https://www.w3schools.com/python/python_conditions.asp
'''


a = input('Enter a:')
a = int(a)
b = 230
c = 330
if a > b:
    print('a is greater than b')
elif a < b:
    print('b is greater than a')
else:
    print(c)

# This technique is known as Ternary Operators, or Conditional Expressions.
# One line if else statement, with 3 conditions:
print("a is greater than b") if a > b else print(
    "b is greater than a") if a == b else print("C")
# to pass the if statement use pass

if a > b:
    pass
