import pymongo

myClinet = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myClinet["mydatabase"]
myCollection = mydb["Customers"]

# myQuery = {"address": "Park Lane 38"}

# mydoc = myCollection.find(myQuery)

# for x in mydoc:
#     print(x)


# for y in myCollection.find():
#     print(y)

# # greater than the parameter
# myquery = {"address": {"$gt": "O"}}
# for item in myCollection.find(myquery):
#     print(item)


# # user REGEX to find items
# myquery = {"address": {"$regex": "^S"}}
# for item in myCollection.find(myquery):
#     print(item)

# Sort
myquery = {"address": {"$gt": "O"}}
for item in myCollection.find(myquery).sort("address"):
    print(item)
