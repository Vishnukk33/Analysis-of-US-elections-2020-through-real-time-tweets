from ssl import SSLError
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
consumer_key="5tlYTpR1tmPTcgMBC0j"
consumer_secret="wVEINjsJ2LVj6lmxxWPuo6KgALIMkUhlTu5lH4"
access_token="100254907977T9YfrjgVJLe1gZy1n8O4mnArToO"
access_token_secret="gNNGpQZYaguflQX5QXFSCER4mKyp5IVdOMcVKvE"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
if (api):
    print("Login Success")
else:
    print("Failed")
firebase= firebase.FirebaseApplication("https://try.firebaseapp.com/", None)
if(firebase):
  print("Logged in fire base")

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
        tweetDataForFirebase = {
            'text': self.text,
            'user': self.user,
            'followers': self.followers,
            'date': self.date,
            'location': self.location,
            'description': self.description,
            'verified': self.verified,
            
        }
        
        result = firebase.post('/try/table2',tweetDataForFirebase)
        c.execute("INSERT INTO twitter1(tweetText, user, followers, date, location,description,verified) VALUES (?,?, ?, ?, ?, ?, ?)",
            (self.text,self.user, self.followers, self.date, self.location,self.description,self.verified)) 
        connection.commit()  
        print("Inserted \n")
        
class TweetStreamListener(tweepy.StreamListener):
    def on_data(self,data):
        
        tweet=json.loads(data)
        try:
                                
                if  not tweet["text"].startswith('RT'):
                    if tweet.get("extended_tweet"):
                        text = str(tweet['extended_tweet']["full_text"])
                    else:
                        text= str(tweet["text"])
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
    l = TweetStreamListener()
    stream = tweepy.Stream(auth, l,tweet_mode='extended')
    
    while not stream.running:
        try:
            logging.info("Started listening to twitter stream...")
            stream.filter(track=['#india'],languages=["en"]) # Type your hashtags to be filtered here            
        except(ProtocolError, AttributeError):
            continue
        except(Timeout, SSLError, ReadTimeoutError, ConnectionError) as e:
            logging.warning("Network error occurred. Keep calm and carry on.", str(e))
        except Exception as e:
            logging.error("Unexpected error!", e)
        finally:
            logging.info("Stream has crashed. System will restart twitter stream!")
    logging.critical("Somehow zombie has escaped...!")
