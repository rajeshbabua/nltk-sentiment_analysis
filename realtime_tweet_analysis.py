from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
#####################################THE BELOWS KEYS CAN BE OBTAINED FROM "https://apps.twitter.com/"
#####################YOU NEED TO HAVE AN ACCOUNT IN TWITTER AND MAKE SURE THAT YOUR TWITTER NOTIFICATIONS FOR UR MOBILE/EMAIL
############ARE OFF WHEN YOU ARE DOING ANALYSIS.IF YOU FAIL YOUR EMAIL AND MOBILE WILL BE FLOODED WITH TWEET NOTIFICATIONS.

#consumer key, consumer secret, access token, access secret.
ckey="asdfsafsafsaf"
csecret="asdfasdfsadfsa"
atoken="asdfsadfsafsaf-asdfsaf"
asecret="asdfsadfsadfsadfsadfsad"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = all_data["text"]
        sent_val,con = s.sentiment(tweet)
        
        
        print(tweet,sent_val,con)
    
        if con*100 >= 80:
        o = open("twitter-out.txt","a")
        o.write(sent_val)
        o.write('\n')
        o.close
        
        return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
