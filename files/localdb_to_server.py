from pymongo import MongoClient

client_server = MongoClient('mongodb://test123:test123@54.180.94.114', 27017)
db_server = client_server.dbikea

client_local = MongoClient('localhost', 27017)
db_local = client_local.dbikea

col_names = db_local.collection_names()
for col_name in col_names:
    docs = list(db_local[col_name].find({}, {'_id': False}))
    db_server[col_name].insert_many(docs)