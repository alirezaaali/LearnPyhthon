'''
Here is some useful methods
You can find more information in
https://www.w3schools.com/python/python_sets.asp
same as list but only changes here
'''


thisIsSet = {"abc", 34, True, 40, "male"}
# print(thisIsSet)
# print("The length of the set is:", thisIsSet.__len__(), " OR ", len(thisIsSet))
# # ------------SET Constructor---------------------
# newList = list(("orange", "mango", "grapes"))
# print(newList)

# --------LOOP THE LIST
thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#     print(x)


# print('Check if an item is exist in set:')
# print('cherry' in thisset)
# print('m' in thisIsSet)
# # ---------ADD NEW ITEM------------------------
# print('add one item in set:\n')
thisIsSet.add("kk")
# print(thisIsSet)
# # -----------------ADD A ANY ITERABLE TO LIST----------------
# print('add more item in set using update:\n')
thisIsSet.update(["orange", "mango", "grapes"])
# print(thisIsSet)
thisIsSet.update(thisset)
# print(thisIsSet)
# ----------------Remove Item------
thisIsSet.remove("mango")
# print(thisIsSet)
# thisIsSet.remove("mango") --> this will raise error
# --> this will NOT raise error even if the item does not exist
thisIsSet.discard("mango")
# ----------------POP the last Item------
# --- YOU dont know which item will be pop
# thisIsSet.pop()
# print(thisIsSet)
# thisIsSet.pop()
# print(thisIsSet)
# thisIsSet.pop()
# print(thisIsSet)
# ----------------del or clear a set
# thisIsSet.clear()
# del thisIsSet
# print(thisIsSet)

# # -------------------Join Two Sets-----------------
# # Note: Both union() and update() will exclude any duplicate items.
# set1 = {"a", "b", "c"}
# print(set1)
# set2 = {1, 2, 3}
# print(set2)

# set3 = set1.union(set2)
# print(set3)
# -------------KEEP ONLY DUPLICATES---------------
# The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# x.intersection_update(y) #--> this will update x
# z = x.intersection(y)  # --> create new set with duplicate item
# print(x, y, z)

# -------------KEEP ALL BUT NOT DUPLICATES---------------
# x.symmetric_difference_update(y)
z = x.symmetric_difference(y)
print(x, y, z)
