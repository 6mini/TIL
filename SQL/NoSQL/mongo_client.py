URI = 'mongodb+srv://6mini:*****@cluster0.buhiu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

from pymongo import MongoClient
# print(MongoClient) # <class 'pymongo.mongo_client.MongoClient'>

client = MongoClient(URI)

# print(client)
'''
MongoClient(host=['cluster0-shard-00-00.buhiu.mongodb.net:27017', 'cluster0-shard-00-01.buhiu.mongodb.net:27017', 'cluster0-shard-00-02.buhiu.mongodb.net:27017'], document_class=dict, tz_aware=False, connect=True, retrywrites=True, w='majority', authsource='admin', replicaset='atlas-7sgtwy-shard-0', ssl=True)
'''

DB = 'myFirstDatabase'

db = client[DB]

COLL = '6mini-collection'

coll = db[COLL]

# print(coll)
'''
Collection(Database(MongoClient(host=['cluster0-shard-00-01.buhiu.mongodb.net:27017', 'cluster0-shard-00-02.buhiu.mongodb.net:27017', 'cluster0-shard-00-00.buhiu.mongodb.net:27017'], document_class=dict, tz_aware=False, connect=True, retrywrites=True, w='majority', authsource='admin', replicaset='atlas-7sgtwy-shard-0', ssl=True), 'myFirstDatabase'), '6mini-collection')
'''

coll.insert_one(document={'hello': '6mini'})

doc = coll.find_one()

print(doc) # {'_id': ObjectId('614b28ec8ac8de52d42de5bd'), 'hello': '6mini'}