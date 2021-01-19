import couchdb
import pymongo

couch_server=couchdb.Server()
#%%
couch_server.resource.credentials=('Carlos','carlos')
#%%
couch_db = couch_server['juego']

client= pymongo.MongoClient("localhost")
db =client.get_database('examen')


for row in couch_db.view('_all_docs', include_docs=True):
    print(row['doc'])
    if db.minecraft.count_documents({"_id":row['doc']['_id']})==0:
        db.minecraft.insert(row['doc'])