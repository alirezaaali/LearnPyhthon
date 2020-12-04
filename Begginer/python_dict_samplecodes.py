'''
Here is some useful methods
You can find more information in
https://www.w3schools.com/python/python_dictionaries.asp
same as list but only changes here
'''
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "myList": ["List Mem0", "List Mem1", "List Mem2", "List Mem3"],
    "mySet":  {"abc", 34, True, 40, "male"},
    "mytuple": ("kiwi", "melon", "mango", "melon", True, 123, 12.5)

}
# print(thisdict)
# print("this is dictionary len:", len(thisdict), " OR ", thisdict.__len__())
# ---------------------------------------------------------------
# You can access the items of a dictionary by referring to its key name, inside square brackets:
# print('access the items of a dictionary by referring to its key name:\n')
# print(thisdict['model'], thisdict["mySet"])
# print('access the items of a dictionary using get("keyname"):\n')
# print(thisdict.get('year'), thisdict.get("mytuple"))
# ---------------------SHOW ALL KEYS------------------------------------------
# print(thisdict.keys())

# -----------ADD NEW KEY TO DIC--------------
# print("before adding new item:", thisdict.keys())
# thisdict["mytuple"] = ("apple", "banana", "cherry", "orange",
#                        "kiwi", "melon", "mango", "melon", True, 123, 12.5, "mango", "mango")
# print("after adding new item:", thisdict.keys())
# ---------------------------------------GET VALUES-----------
# print(thisdict.values())
# thisdict["mytuple"] = ("apple", "banana", "cherry", "orange")
# print(thisdict.values())
# print(thisdict.items())  # ---> print all values as tuplesss
# ------------------------------CHECK IF KEY is EXISTS

# if "myList" in thisdict:
#     print(thisdict.get("myList"))
# print(thisdict.get("myList32")) --> this will return None

# -----------------change a value
# thisdict['year'] = 2020
# print(thisdict)
# thisdict.update({"year": 2020})
# print(thisdict)
# ---------------------loops
# # this will print only the keys
# for x in thisdict:
#     print(x)
# ------------------REMOVE POP CLEAR DEL----------------
# print(thisdict, "\n")
# thisdict.pop("myList")
# print(thisdict, "\n")
# thisdict.popitem()
# print(thisdict)
# del thisdict["year"]

# print(thisdict, "\n")

# thisdict.clear()
# print(thisdict, "\n")
# del thisdict
# print(thisdict, "\n")  # --- show error because dictionary was deleted
# -----------------LOOPS-------------
# Print all key names in the dictionary, one by one:
# for x in thisdict:
#     print(x)

# # this will print keys & values
# for x in thisdict:
#     print(thisdict[x])
# # # this will print only values
# for x in thisdict.values():
#     print(x)
# # this will print only keys
# for x in thisdict.keys():
#     print(x)
# # loop through both keys and values, by using the items() method:
# for key, value in thisdict.items():
#     print(key, value)
# ---------------------copy dictionary----------------------------
# newDict = thisdict.copy()
# newDict2 = dict(thisdict)

print("Hello"[0])