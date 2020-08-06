from ssl import SSLError
import string
import re
import time
from requests.exceptions import Timeout, ConnectionError
from urllib3.exceptions import ReadTimeoutError
import json
import tweepy
from urllib3.exceptions import ProtocolError
import sqlite3
import logging
global api
from firebase import firebase 
consumer_key="5tlYTpVNtcxNR1tmPTcgMBC0j"
consumer_secret="wVEX9My3v6340sHINjsJ2LVj6lmxxWPuo6KgALIMkUhlTu5lH4"
access_token="1002549079774093313-fCET9YfrjgVJLe1gZy1n8O4mnArToO"
access_token_secret="gNNGpKh7GBsQZYaguflQX5QXFSCER4mKyp5IVdOMcVKvE"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=10, retry_delay=5, retry_errors=5)
if (api):
    print("Login Success")
else:
    print("Failed")

#firebase= firebase.FirebaseApplication("https://try1-c613f.firebaseio.com/", None)
print("Logged in fire base")

connection = sqlite3.connect('realtime14.db')
c = connection.cursor()
c.execute('''CREATE TABLE twittr206
    (tweetText text,
    hashtags text,
    user text,
    date text,
    location text,
    state text,
    latitude float,
    longitude float)''')
connection.commit()
connection.close()
connection = sqlite3.connect("realtime14.db")
c = connection.cursor()

class Tweet():
    def __init__(self, text,user,date,location,state,latitude,longitude):
        self.text = text
        
        self.user=user
        self.date = date
        self.location = location
        self.state=state
        self.latitude=latitude
        self.longitude=longitude
    
    def insertTweet(self):
        tweetDataForFirebase = {
            'text': self.text,
           
            'user': self.user,
            'date': self.date,
            'location': self.location,
            'state': self.state,
            'latitude': self.latitude,
            'longitude': self.longitude
        }
        #result = firebas.post('/try1-c613f/table1',tweetDataForFirebase)
        self.text=" ".join( self.text.splitlines()) 
        c.execute("INSERT INTO twittr206(tweetText,user,date, location,state,latitude,longitude) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (self.text,self.user, self.date, self.location,self.state,self.latitude,self.longitude)) 
        connection.commit()

        print("Inserted \n")
        
class TweetStreamListener(tweepy.StreamListener):
    def on_data(self,data):
        tweet=json.loads(data)
        try:
                state="XXXX"
                latitude=99999.99
                longitude=9999.99
                if  not tweet["text"].startswith('RT'):
                    if tweet.get("extended_tweet"):
                        text = str(tweet['extended_tweet']["full_text"])
                    else:
                        text= str(tweet["text"])
                    
                    
            
                    emoji_pattern = re.compile("["u"\U0001F600-\U0001F64F"u"\U0001F300-\U0001F5FF" u"\U0001F680-\U0001F6FF"  u"\U0001F1E0-\U0001F1FF"  u"\U00002702-\U000027B0"u"\U000024C2-\U0001F251""]+", flags=re.UNICODE)
                    text = re.sub(r':', '', text)
                    text = re.sub(r'‚Ä¶', '', text)
                    text = re.sub(r'[^\x00-\x7F]+',' ', text)
        
                    user_profile=api.get_user(tweet['user']['screen_name'])
                    if(tweet['place'] ):
                        if(str(tweet['place']['full_name'].split(', ')[1])):
                            s=str(tweet['place']['full_name'].split(', ')[1])
                            states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID","IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI","NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "NONE"]
                            if(s in states):
                                state=s
                              
                                
                    if(tweet['coordinates']):
                        latitude=tweet['coordinates']['coordinates'][1]
                        longitude=tweet['coordinates']['coordinates'][0]
                          
                    
                        
                    tweet_data = Tweet(text,tweet['user']['screen_name'],tweet['created_at'],tweet['user']['location'],state,latitude,longitude)
                    tweet_data.insertTweet()
            
                return True
                
        except Exception as e:
            print(e)
            print("sdf")
            return True
if __name__ == '__main__':
    print("start \n")
    l = TweetStreamListener()
    stream = tweepy.Stream(auth, l,tweet_mode='extended')
    while True:
        try:
            
            logging.info("Started listening to twitter stream...")
            stream.filter(locations=[-180,-90,180,90],languages=["en"])            
        except(ProtocolError, AttributeError):
            time.sleep(200)
            continue
        except(Timeout, SSLError, ReadTimeoutError, ConnectionError) as e:
            logging.warning("Network error occurred. Keep calm and carry on.", str(e))
        except Exception as e:
            logging.error("Unexpected error!", e)
        finally:
            logging.info("Stream has crashed. System will restart twitter stream!")
    logging.critical("Somehow zombie has escaped...!")
