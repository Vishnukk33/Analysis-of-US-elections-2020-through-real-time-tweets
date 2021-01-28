import pandas as pd
import botometer
import tweepy
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
    
rapidapi_key = "Insert_rapidapi_key_here" 
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

newcsvname="bot1.csv"
df = pd.DataFrame(index=[0,1,2])
df.to_csv(newcsvname)
data=pd.read_csv(newcsvname)
data.drop(data.columns[data.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
data['user']=" "
data['bot']=" "
data['probability']=0
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

