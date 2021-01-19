import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

y = "XERPGu67zV0dBxgp2NQnarA1R"
csecret = "U5KIdVpGfrWGRxoYflFmc8dhGwNImbufmZk2uCQM5ij8KlVei4"
atoken = "1343642563765526540-Y2a8NDwhMxsstaewzZHBh618dfLsgS"
asecret = "E66UDWDjIxE7OiYEYR5jAyZ8BIHvnBPuqSpE84MVugixi"

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

server = couchdb.Server('http://Carlos:carlos@localhost:5984/')

try:
    db = server.create('juego')
except:
    db = server['juego']
#%%   
#twitterStream.filter(locations=[-9.47,36.55,-0.54,42.4])  
twitterStream.filter(track=['minecraft'])