import pymongo
from bson.json_util import dumps

uri = 'mongodb+srv://m220student:m220password@mflix.smtxw.mongodb.net/<dbname>?retryWrites=true&w=majority'

# create client
client = pymongo.MongoClient(uri)

# # check connection
# print(client.stats)

'''
Database(MongoClient(host=['mflix-shard-00-00.smtxw.mongodb.net:27017',\
 'mflix-shard-00-02.smtxw.mongodb.net:27017', 'mflix-shard-00-01.smtxw.mongodb.net:27017'],\
  document_class=dict, tz_aware=False, connect=True, retrywrites=True, w='majority',\
   authsource='admin', replicaset='atlas-d822o9-shard-0', ssl=True), 'stats')
'''

# # show dbs
# print(client.list_database_names())
'''
['sample_airbnb', 'sample_analytics', 'sample_geospatial', 'sample_mflix', 'sample_restaurants',\
 'sample_supplies', 'sample_training', 'sample_weatherdata', 'admin', 'local']
'''

# # use sample_mflix
mflix = client.sample_mflix
# mflix = client['sample_mflix']  # or we can use dictionary accessors
# # show collections
# print(mflix.list_collection_names())
# # ['sessions', 'users', 'movies', 'comments', 'theaters']

movies = mflix.movies
# # count documents
# print(movies.count_documents({}))
# # 23530

# # find one document in the "movies" collection - does not matter which one
# print(movies.find_one())
# # find one document in the "movies" collection - must have "Salma Hayek" in the "cast"
# print(movies.find_one({"cast": "Salma Hayek"}))

# # find all the documents in the "movies" collection with "Salma Hayek" in the "cast"
# # this returns a cursor, which IS a Python iterable, but is NOT a document!
# print(movies.find({"cast": "Salma Hayek"}))

# # return the count of movies with "Salma Hayek" in the "cast"
# print(movies.find({"cast": "Salma Hayek"}).count())

# find all movies with Salma Hayek
# then pretty print
# cursor = movies.find()
# print(dumps(cursor, indent=4))

# # find all movies with Salma Hayek, but only project the "_id" and "title" fields
# cursor = movies.find( { "cast": "Salma Hayek" }, { "title": 1, "_id":0 } )
# # print(cursor)
# '''
# <pymongo.cursor.Cursor object at 0x02E0F700>
# '''
# # print(dumps(cursor, indent=4))

cursor = movies.find({}, {"countries": 1, "_id": 0})
print(dumps(cursor, indent=4))

