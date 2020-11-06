'''
Here is some useful string methods
You can find more information in
https://www.w3schools.com/python/python_tuples.asp
same as list but only changes here
'''

thisIsTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thisIsTuple)
print('Change a tuple')
'''
Once a tuple is created, you cannot change its values. Tuples are unchangeable, 
or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list,
 change the list, and convert the list back into a tuple.
'''
mylist = list(thisIsTuple)
mylist[1] = 'Fuckers'
thisIsTuple = tuple(mylist)
print(thisIsTuple)
