import json
from argparse import ArgumentParser
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId

try:
    client = MongoClient('localhost')
    print (client.list_database_names())
    db = client['examen']
    col = db['facebook']
    clientatl = MongoClient('mongodb+srv://carlos:Carlos@cluster0.y3s4w.mongodb.net/examen?retryWrites=true&w=majority')
    dbatl = clientatl['examen']
    colatl = dbatl['facebook-atl']
    print (clientatl.list_database_names())
except requests.ConnectionError as e:
    raise e

for doc in col.find({}):
    try:
        print(doc)
        colatl.insert_one(doc)
        print('guardado con exito')
    except: 
        print ("Already exists")
        pass

    

