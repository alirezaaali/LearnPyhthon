'''
Here is some useful  methods
You can find more information in
https://www.w3schools.com/python/python_for_loops.asp
'''

# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
# simple
# for x in range(11):
#     print(x)

# complex
# for x in range(0, 11, 1):
#     print(x)

# Jadval zarb
result = ''
for x in range(11):
    for y in range(11):
        result = '{0} X {1} = ' + str(x*y)
        print(result.format(x, y))
