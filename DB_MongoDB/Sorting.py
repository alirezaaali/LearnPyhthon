import pymongo

myClinet = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myClinet["mydatabase"]
myCollection = mydb["Customers"]


# Sort
myquery = {"address": {"$gt": "O"}}
for item in myCollection.find(myquery).sort("address", -1):
    print(item)
