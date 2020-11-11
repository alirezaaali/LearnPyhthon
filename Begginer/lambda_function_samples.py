'''
Here is some useful methods
You can find more information in
https://www.w3schools.com/python/python_lambda.asp
'''
# Syntax
#lambda arguments : expression

# sample 1


def x(a, b, c): return (a*b)**c


print(x(10, 5, 3))

# sample2


def crossPower(n, m):
    return lambda a: (a+n)**m


mydoubler = crossPower(2, 2)

print(mydoubler(3))
