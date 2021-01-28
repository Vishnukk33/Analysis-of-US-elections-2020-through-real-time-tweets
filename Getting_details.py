# Getting the followers, their mentioned location and whether their account is verified, from the Twitter users.

import numpy as np
import pandas as pd
import json
import tweepy
global api

pd.options.mode.chained_assignment = None
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

for name in range(1,6):    
    csvname="repub"+str(name)+".csv"
    data=pd.read_csv(csvname)
    users_list=list(data['user'])
    data["followers"]=-1
    data["verified"]=-1
    data["mentioned_location"]=""
    for i in range(len(users_list)):
        user=users_list[i]
        try:
            user_profile=api.get_user(user)
            data["followers"][i]=user_profile.followers_count
            data["mentioned_location"][i],data["verified"][i]=user_profile.location,user_profile.verified
    data.to_csv(csvname,index='False')    
