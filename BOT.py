#Botometer API used to check if top 10 twitter accounts are bots

import botometer
import json
import tweepy
from beautifultable import BeautifulTable
global api

consumer_key="insert_consumer_key"
consumer_secret="insert_consumer_secret_key"
access_token="insert_access_token"
access_token_secret="insert_access_token_secret"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
if (api):
    print("Login Success")
else:
    print("Failed")
    
rapidapi_key = "insert rapid api key" # now it's called rapidapi key
twitter_app_auth = {
    'consumer_key': consumer_key,
    'consumer_secret': consumer_secret,
    'access_token': access_token,
    'access_token_secret': access_token_secret,
  }
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)


user_name_list= list(set(most_tweeted))
user_name_list1= list(set(most_tweeted1))

print("Lets Check if the top Tweeters are Bots or not ")
print("We take the top 2 tweeters on each day for republican and democratic parties over 5 days ")
print("The results are as follows")

table = BeautifulTable()
table.columns.header = ["User", "Bot"]
print("\n Top democratic tweeters:")
for i in range (0,len(user_name_list)):
    try:
        bot_result = bom.check_account(user_name_list[i])
        score=bot_result["cap"]["english"]*100
        if (score>60):
            bot_chance='Yes' 
        if (score>40 and score<60):
            bot_chance='Maybe'
        if (score<40):
            bot_chance='No'
    except:
        bot_chance='Unknown'
        
    table.rows.append([user_name_list[i],bot_chance])

table.set_style(BeautifulTable.STYLE_GRID)
print(table)

table1 = BeautifulTable()
table1.columns.header = ["User", "Bot"]
print("\n Top republican tweeters:")
for i in range (0,len(user_name_list1)):
    try:
        bot_result = bom.check_account(user_name_list1[i])
        score=bot_result["cap"]["english"]*100
        if (score>60):
            bot_chance='Yes' 
        if (score>40 and score<60):
            bot_chance='Maybe'
        if (score<40):
            bot_chance='No'
    except:
        bot_chance='Unknown'
        
    table1.rows.append([user_name_list1[i],bot_chance])

table1.set_style(BeautifulTable.STYLE_GRID)
print(table1)

