'''
Here is some useful methods
You can find more information in
https://www.w3schools.com/python/python_lists.asp
'''

thisIsList = ["List Mem0", "List Mem1", "List Mem2", "List Mem3",
              "apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisIsList)
print("This is len of the list: \n")
print(thisIsList.__len__())
print("This is Memebr2 in the list: \n" + thisIsList[2])
print("This is negative index -2 in the list: \n" + thisIsList[-2])
print("This is range index from 2 to 5 in the list: \n")
print(thisIsList[2:5])
print("This is range index from begining of the list to 6 in the list: \n")
print(thisIsList[:5])
print("This is range index from a specific index to end of the list: \n")
print(thisIsList[3:])
print("This is range index from a specific negative index to ea specific negative index in the list: \n")
print(thisIsList[-7:-3])
print("------------------------------------------------------------------------")
print("Chanage Item[-3] from \'kiwi' to \'Fuckers': \n")
thisIsList[-3] = 'Fuckers'
print(thisIsList)
print("------------------------------------------------------------------------")
print("Here we go throu the thisIsList (loop): \n")
for x in thisIsList:
    print(x)
print("------------------------------------------------------------------------")
print("Check if Item Exists in thisIsList : \n")
if 'kiwi' in thisIsList:
    print('Yes, We have Kiwi')
else:
    print('No, We Do not have Kiwi')
print("------------------------------------------------------------------------")
print("No we add Kiwi to thisIsList and run it again : \n")
thisIsList.append('kiwi')
# print(thisIsList)

if 'kiwi' in thisIsList:
    print('Yes, We have Kiwi')
else:
    print('No, We Do not have Kiwi')
print("------------------------------------------------------------------------")
print("No we add Peakyess to third item of thisIsList and run it again : \n")
thisIsList.insert(3, 'Peakyess')
print(thisIsList)

if 'Peakyess' in thisIsList:
    print('Yes, We have Peakyess')
else:
    print('No, We Do not have Peakyess')
print("------------------------------------------------------------------------")
print(thisIsList)
print("No we remove fuckers from thisIsList and run it again : \n")
thisIsList.remove('Fuckers')
print(thisIsList)
print("No we pop index 2 from thisIsList and run it again : \n")
thisIsList.pop(2)
print(thisIsList)
print("No we pop del 0 from thisIsList and run it again : \n")
del thisIsList[0]
print(thisIsList)
print("------------------------------------------------------------------------")
print(thisIsList)
print("This list is going to del or clear: \n")
# thisIsList.clear()
# print(thisIsList)
print("------------------------------------------------------------------------")
print(thisIsList)
print("now copy to another list: \n")
newlist = thisIsList.copy()
print(newlist)
sew2list = list(thisIsList)
print(sew2list)
print("------------------------------------------------------------------------")
print(thisIsList)
print("Join 2 lists: \n")
newlist.extend(thisIsList)
print(newlist)

print("------------------------------------------------------------------------")
print("create new list using list contructor: \n")
newlist = list(('aa','bb','cc','ff','ee'))
print(newlist)