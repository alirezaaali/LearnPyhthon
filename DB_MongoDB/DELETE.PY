import pymongo

myClinet = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myClinet["mydatabase"]
myCollection = mydb["Customers"]


# DELETE
myquery = {"address": {"$gt": "O"}}
# for item in myCollection.find(myquery).sort("address", -1):
#     print(item)

# x = myCollection.delete_one(myquery)
# print(x.deleted_count)

# x = myCollection.delete_many(myquery)
# print(x.deleted_count)

# x = myCollection.delete_many({})
# print(x.deleted_count)
