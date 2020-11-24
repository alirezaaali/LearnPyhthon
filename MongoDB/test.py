import pymongo

# print('Mongo DB is Ok')

myClinet = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myClinet["mydatabase"]
myDbList = myClinet.list_database_names()
if "mydatabase" in myDbList:
    print("mydatabase is exists in DB List")
else:
    print("mydatabase is NoT exists in DB List")


myCollection = mydb["Customers"]
myColList = mydb.list_collection_names()

if "Customers" in myColList:
    print("Customers Collection is exists in collection List")
else:
    print("Customers is NoT exists in collection List")

# Insert one document
# mydict = {"name":"Alireza","address": "Highway 37" }

#  x = myCollection.insert_one(mydict)
# print(x.inserted_id)


# Insert many documents
# mylist = [
#   { "name": "Amy", "address": "Apple st 652"},
#   { "name": "Hannah", "address": "Mountain 21"},
#   { "name": "Michael", "address": "Valley 345"},
#   { "name": "Sandy", "address": "Ocean blvd 2"},
#   { "name": "Betty", "address": "Green Grass 1"},
#   { "name": "Richard", "address": "Sky st 331"},
#   { "name": "Susan", "address": "One way 98"},
#   { "name": "Vicky", "address": "Yellow Garden 2"},
#   { "name": "Ben", "address": "Park Lane 38"},
#   { "name": "William", "address": "Central st 954"},
#   { "name": "Chuck", "address": "Main Road 989"},
#   { "name": "Viola", "address": "Sideway 1633"}
# ]
# x= myCollection.insert_many(mylist)
# print(x.inserted_ids)

mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

x = myCollection.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)





