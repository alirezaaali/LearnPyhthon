'''
Here is some useful methods
You can find more information in
https://www.w3schools.com/python/python_dictionaries.asp
same as list but only changes here
'''
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
# You can access the items of a dictionary by referring to its key name, inside square brackets:
print('access the items of a dictionary by referring to its key name:\n')
print(thisdict['model'])
print('access the items of a dictionary using get("keyname"):\n')
print(thisdict.get('year'))
# change a value
thisdict['year'] = 2020
print(thisdict)
# loops
# this will print only the keys
for x in thisdict:
    print(x)

# this will print keys & values
for x in thisdict:
    print(thisdict[x])
# this will print only values
for x in thisdict.values():
    print(x)
# loop through both keys and values, by using the items() method:
for key, value in thisdict.items():
    print(key, value)
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict['Driver'] = 'Alireza'
print(thisdict)
# The pop() method removes the item with the specified key name:
thisdict.pop('Driver')
print(thisdict)
