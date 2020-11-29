import pymongo

myClinet = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myClinet["mydatabase"]
myCollection = mydb["Customers"]


# Drop
myCollection.drop()
