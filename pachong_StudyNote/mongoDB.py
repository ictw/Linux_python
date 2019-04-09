import pymongo

client = pymongo.MongoClient('localhost', port=27017)

db = client.test
collection = db.aaa

collection.insert({'username': 'suofeiya'})
collection.insert({'username': 'suofeiya', 'age': 21})
collection.insert({'username': 'suofeiya', 'age': 21, 'home': 'yunan'})

collection.insert({'name': 'suofeiya', 'age': 21, 'ide': 'pycharm'})
