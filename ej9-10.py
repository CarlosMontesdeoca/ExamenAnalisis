import json
import pymongo

client= pymongo.MongoClient("mongodb+srv://carlos:Carlos@cluster0.y3s4w.mongodb.net/examen?retryWrites=true&w=majority")
db =client.get_database('examen')
col = db['facebook-atl']

myjson = []
for doc in col.find({}):
    myjson.append(doc) 

x = np.asarray(myjson)
np.savetxt("output.csv", x, delimiter=',')