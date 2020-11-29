import pymongo

# print('Mongo DB is Ok')

myClinet = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myClinet["mydatabase"]
myCollection = mydb["Customers"]

# print("these are databases:", myClinet.list_database_names())
# print("these are collections:", mydb.list_collection_names())

# x = myCollection.find_one()
# print(x)

for item in myCollection.find().limit(4):
    print(item)

# for item in myCollection.find({}, {'_id': 0, 'name': 1, 'address': 1}):
#     print(item)

# for item in myCollection.find({}, {'address': 0}):
#     print(item)

# x = myCollection.find_one(
#     {}, {'_id': 0, 'name': 1, 'address': 1})
# print(x)


# x = myCollection.find_one(
#     {}, {'_id': 7})
# print(x)
