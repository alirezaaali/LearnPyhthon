'''
Here is some useful methods
You can find more information in
https://www.w3schools.com/python/python_sets.asp
same as list but only changes here
'''

thisIsSet = {"apple", "banana", "cherry"}
print(thisIsSet)
print('Change a Set')
# ---------------------------------
print('Check if an item is exist in set:\n')
print('cherry' in thisIsSet)
print('m' in thisIsSet)
# ---------------------------------
print('add one item in set:\n')
thisIsSet.add("kk")
print(thisIsSet)
# ---------------------------------
print('add more item in set using update:\n')
thisIsSet.update(["orange", "mango", "grapes"])
print(thisIsSet)
# -------------------Join Two Sets-----------------
# Note: Both union() and update() will exclude any duplicate items.
set1 = {"a", "b", "c"}
print(set1)
set2 = {1, 2, 3}
print(set2)

set3 = set1.union(set2)
print(set3)
