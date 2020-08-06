import time
from requests.exceptions import Timeout, ConnectionError
from urllib3.exceptions import ReadTimeoutError
import json
import tweepy
import logging
global api
#from firebase import firebase
consumer_key="5tlYTpVNtcxNR1tmPTcgMBC0j"
consumer_secret="wVEX9My3v6340sHINjsJ2LVj6lmxxWPuo6KgALIMkUhlTu5lH4"
access_token="1002549079774093313-fCET9YfrjgVJLe1gZy1n8O4mnArToO"
access_token_secret="gNNGpKh7GBsQZYaguflQX5QXFSCER4mKyp5IVdOMcVKvE"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
if (api):
    print("Login Success")
else:
    print("Failed")
class TweetStreamListener(tweepy.StreamListener):
    def on_data(self,data):
        
        tweet=json.loads(data)
        try:
                def from_creator(data):
                    if hasattr(data, 'retweeted_status'):
                        return False
                    else:
                        return True
                if from_creator(data):                
                    if  not tweet["text"].startswith('RT'):
                        if tweet.get("extended_tweet"):
                            text = str(tweet['extended_tweet']["full_text"])
                        else:
                            text= str(tweet["text"])
                        print(text)
                        s=[]
                        s.append(text)
                        
                        user_profile=api.get_user(tweet['user']['screen_name'])
                        username=tweet['user']['screen_name']
                        
                        s.append(username)
            
                return True
                
        except Exception as e:
            print()
            print("")
            return True
        
if __name__ == '__main__':
    print("start \n")
    
    # Run the stream!
    l = TweetStreamListener()
    stream = tweepy.Stream(auth, l,tweet_mode='extended')
    stream.filter(follow=['1204812731620057088']) 
    # Filtering
    while not stream.running:
        try:
            logging.info("Started listening to twitter stream...")
            stream.filter(follow=['1204812731620057088'])            
        except(ProtocolError, AttributeError):
            continue
        except(Timeout, SSLError, ReadTimeoutError, ConnectionError) as e:
            logging.warning("Network error occurred. Keep calm and carry on.", str(e))
        except Exception as e:
            logging.error("Unexpected error!", e)
        finally:
            logging.info("Stream has crashed. System will restart twitter stream!")
    logging.critical("Somehow zombie has escaped...!")
