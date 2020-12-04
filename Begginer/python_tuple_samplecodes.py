'''
Here is some useful methods
You can find more information in
https://www.w3schools.com/python/python_tuples.asp
same as list but only changes here
'''

# ----create tuple--------
# thisIsTuple_cons = tuple(("apple", "banana", "cherry", "orange",
#                           "kiwi", "melon", "mango", "melon", True, 123, 12.5))

thisIsTuple = ("apple", "banana", "cherry", "orange",
               "kiwi", "melon", "mango", "melon", True, 123, 12.5, "mango", "mango")
# print(thisIsTuple)
# print('Change a tuple')
# ------------------------NUMBER OF ITEMS IN TUPELS---------------
# print('This is length of a tuple using tuple.__len__(): ', thisIsTuple.__len__())
# print('This is length of a tuple using len(tuple): ', len(thisIsTuple))
# print(type(thisIsTuple))

# print('This is length of a tuple using tuple.__len__(): ', thisIsTuple_cons.__len__())
# print('This is length of a tuple using len(tuple): ', len(thisIsTuple_cons))
# print(type(thisIsTuple_cons))
# -----------------------------------------------------------------------------


# -----------------------Access items
# print(thisIsTuple)
# print('Item First Item :tuple[0]', thisIsTuple[0])
# print('Item Last Item :tuple[-1]', thisIsTuple[-1])
# print('Item 2 to 5 (5 not included) :tuple[2:5]', thisIsTuple[2:5])
# print('Item 0 to 5 (5 not included) :tuple[:5]', thisIsTuple[:5])
# print('Item 2 to last item :tuple[2:]', thisIsTuple[2:])
# print('Item -5 to -2 (-2 not included) :tuple[-5:-2]', thisIsTuple[-5:-2])

# -----------------------Search tuple items
# if 'kiwi' in thisIsTuple:
#     print('Yes, kiwi is Here!')

'''
Once a tuple is created, you cannot change its values. Tuples are unchangeable, 
or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list,
 change the list, and convert the list back into a tuple.
'''

# # -----Chage a tuple
# mylist = list(thisIsTuple)
# print(thisIsTuple)
# print(mylist)

# # change index [0]
# mylist[0] = 'New Item'
# print(thisIsTuple)
# print(mylist)

# # insert or append new items
# mylist.insert(0, 'Used Insert()')
# mylist.append('Used append()')
# print(thisIsTuple)
# print(mylist)

# # remove item
# mylist.remove('cherry')
# print('used remove():', mylist)
# mylist.pop(2)
# print('used pop(2):', mylist)
# mylist.pop()
# print('used pop():', mylist)
# del mylist[3]
# print('used del mylist[3]:', mylist)

# # conevrt list to tuple
# thisIsTuple = tuple(mylist)
# print('this is after converting list to tuple:', thisIsTuple)


# --------------------------unpack the list
# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

# Using Asterix*
# This Asterix* make a list in the tuple,
# use it when you don`t know the len of the tuple

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (*green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

# --------------Loop the tuple

# ruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# # for x in ruits:
# #     print(x)

# # for i in range(len(ruits)):
# #     print(ruits[i])


# i = 0
# while i < len(ruits):
#     print(ruits[i])
#     i += 1

# # --------------JOIN tuples
# tuple1 = ("a", "b", "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)

#-------------count(item) in tuple
print(thisIsTuple)
print("this is the count of mango in this tupe:", thisIsTuple.count("mango"))

# -----------------------index
# thisIsTuple = ("apple", "banana", "cherry", "orange",
#                "kiwi", "melon", "mango", "melon", True, 123, 12.5)

print(thisIsTuple)
print("this is mango location in this tupe:", thisIsTuple.index("mango"))
