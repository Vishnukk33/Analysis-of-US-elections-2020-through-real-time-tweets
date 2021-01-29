# This program filters tweets based on the coordinates mentioned (in locations).

from ssl import SSLError
import re
import time
from requests.exceptions import Timeout, ConnectionError
from urllib3.exceptions import ReadTimeoutError, ProtocolError
import json
import tweepy
import sqlite3
import logging
from firebase import firebase
global api

consumer_key="Insert_consumer_key_here"
consumer_secret="Insert_consumer_secret_here"
access_token="Insert_access_token_here"
access_token_secret="Insert_access_token_secret_here"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
if (api):
    print("Login Success")
else:
    print("Failed")
firebase= firebase.FirebaseApplication("Insert_your_firebase_table_URL_here", None)
if(firebase):
  print("Logged in fire base")

#Creating a table in sqlite database. 
connection = sqlite3.connect('realtime1.db')
c = connection.cursor()
c.execute('''CREATE TABLE twitter1
    (tweetText text,
    hashtags text,
    user text,
    followers integer,
    date text,
    location text,
    description text,
    verified text
     )''')
connection.commit()
connection.close()
connection = sqlite3.connect("realtime1db")
c = connection.cursor()

class Tweet():
    def __init__(self, text,user,followers,date,location,description,verified):
        self.text = text
        self.user=user
        self.followers = followers
        self.date = date
        self.location = location
        self.description=description
        self.verified=verified
        
    def insertTweet(self):
        # The data is uploaded/appended to firebase table as a dictionary 
        tweetDataForFirebase = {
            'text': self.text,
            'user': self.user,
            'followers': self.followers,
            'date': self.date,
            'location': self.location,
            'description': self.description,
            'verified': self.verified,
        }
        #inserting into firebase table
        result = firebase.post('Insert_your_firebase_table_link_here',tweetDataForFirebase)
        #inserting into sqlite table 
        c.execute("INSERT INTO twitter1(tweetText, user, followers, date, location,description,verified) VALUES (?,?, ?, ?, ?, ?, ?)",
            (self.text,self.user, self.followers, self.date, self.location,self.description,self.verified)) 
        connection.commit()  
        print("Inserted \n")
 
#Streaming
class TweetStreamListener(tweepy.StreamListener):
    def on_data(self,data):
        # Dumping JSON data
        tweet=json.loads(data)
        try:
                # Filtering out retweets, and getting the tweet text.
                # Extended tweet is used to get tweet texts which are between 140 to 280 characters.
                if  not tweet["text"].startswith('RT'):
                    if tweet.get("extended_tweet"):
                        text = str(tweet['extended_tweet']["full_text"])
                    else:
                        text= str(tweet["text"])
                    # Filtering out emojis and other special characters.    
                    emoji_pattern = re.compile("["u"\U0001F600-\U0001F64F"u"\U0001F300-\U0001F5FF" u"\U0001F680-\U0001F6FF"  u"\U0001F1E0-\U0001F1FF"  u"\U00002702-\U000027B0"u"\U000024C2-\U0001F251""]+", flags=re.UNICODE)
                    text = re.sub(r':', '', text)
                    text = re.sub(r'‚Ä¶', '', text)
                    text = re.sub(r'[^\x00-\x7F]+',' ', text)
                    text=" ".join( text.splitlines())
                    
                    user_profile=api.get_user(tweet['user']['screen_name'])
                    tweet_data = Tweet(text,tweet['user']['screen_name'],user_profile.followers_count,tweet['created_at'],tweet['user']['location'],tweet['user']['description'],tweet['user']['verified'])
                    tweet_data.insertTweet()
            
                return True
                
        except Exception as e:
            print(e)
            return True
        
if __name__ == '__main__':
    print("start \n")
    #Start listening
    l = TweetStreamListener()
    stream = tweepy.Stream(auth, l,tweet_mode='extended')
    
    # logging is used for keeping track of the errors and warning that has occured 
    while not stream.running:
        try:
            logging.info("Started listening")
             """The coordinates represents the north-eastern and south-western points. A bounding box is created enclosing the 
             mentioned coordinates and all the tweets tweeted within the area enclosed by the bounding box would be filtered."""   
            stream.filter(locations=[-180,-90,180,90],languages=["en"])         
        except(ProtocolError, AttributeError):
            continue
        except(Timeout, SSLError, ReadTimeoutError, ConnectionError) as e:
            logging.warning("Network error occurred.", str(e))
        except Exception as e:
            logging.error("Unexpected error.", e)
        finally:
            logging.info("Stream has crashed.")
    logging.critical("Somehow zombie has escaped...!")
