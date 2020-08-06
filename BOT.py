import pandas as pd
pd.options.mode.chained_assignment = None
df = pd.DataFrame(index=[0,1,2])
newcsvname="bot1.csv"
df.to_csv(newcsvname)
import botometer
import tweepy
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
rapidapi_key = "e8ac519084mshbec641a05aca5f1p1f553bjsn92af315e6906" # now it's called rapidapi key
twitter_app_auth = {
    'consumer_key': consumer_key,
    'consumer_secret': consumer_secret,
    'access_token': access_token,
    'access_token_secret': access_token_secret,
  }
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)


user_name_list=['@narendramodi','@MetaphorMagnet','@DeepDrumpf']
#Get the user name list and save it to user_name_list take max of 1999 and also add '@' symbol before using user = '@'+ user


data=pd.read_csv(newcsvname)
data.drop(data.columns[data.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
data['user']=" "
data['probability']=0
data['bot']=" "
data.to_csv(newcsvname,index=False)

for i in range (0,len(user_name_list)):

    print("Checking if user is a bot")
    bot_result = bom.check_account(user_name_list[i])
    score=bot_result["scores"]["english"]*100

    if (score>=40):
        bot_chance='Yes'
    elif (score<40):
        bot_chance='No'
   
    data['user'][i]=user_name_list[i]
    data['probability'][i]=score
    data['bot'][i]=bot_chance
   
data.to_csv(newcsvname,index=False)
