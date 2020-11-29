import pymongo

myClinet = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myClinet["mydatabase"]
myCollection = mydb["Customers"]

print('----------------- before upate -----------------------')
for item in myCollection.find({}):
    print(item)

print('----------------- after upate -----------------------')
# myquery = {'address': 'Valley 345'}
# myUpdateValue = {'$set': {'address': 'Velayati 54'}}

# x = myCollection.update_one(myquery, myUpdateValue)

# print(x.modified_count)

# for z in myCollection.find({}):
#     print(z)

myquery = {'address': {'$regex': '^S'}}
myUpdateValue = {'$set': {'address': 'Velayati 54 vahed 1 Hello to NoSql'}}

x = myCollection.update_many(myquery, myUpdateValue)

print(x.modified_count, 'document updated')

for z in myCollection.find({}):
    print(z)
