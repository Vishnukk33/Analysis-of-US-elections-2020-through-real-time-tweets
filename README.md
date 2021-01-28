# Twitter-Project
# Features:
We have incorporated the following in our project:

Streaming and collecting real-time tweets based on hashtags, locations and username.
Developing Machine Learning Classifiers to predict the political orientation of the tweet.
Performing Sentiment Analysis on the collected data.
Visualizing and analyzing the data with the help of bar graphs, pie charts, word-clouds and maps.
Indentifying Bots amongst most tweeted users.


Dataset Creation:
Data Collection:
Used Tweepy Streaming API to stream through real-time tweets.
Used "Filter_by_hashtags.py", "Filter_by_location.py" to stream through real-time tweets.
Stored the collected tweets locally using Sqlite Database as well as in the Cloud using Firebase.
Tweets collected by "Filter_by_hashtags.py" has the following attributes: 'tweetText','hashtags','user','followers','date','location','description','verified'.
Tweets collected by "Filter_by_location.py" has the following attributes: 'tweetText','hashtags','user','date','location','latitude','longitude','state'.
We have used "Filter_by_location.py" to collect the tweets. The reason being, "Filter_by_hashtags.py" was able to collect very few 'latitude','longitude','state' data containing tweets.
Thus we have used "Filter_by_location.py" and further extracted the details of the user using ".py". Thus the final attributes include 'tweetText','hashtags','user','date','state','latitude','longitude','followers','verified','mentioned_location'.
The reason we have extracted only a few details of the tweets and the detail of the users using "Filter_by_location.py" and collected further details using ".py" was to avoid data limit breach.
The attributes are explained below to better understand them:
tweetText: The tweet which is of 1 to 280 characters in length.
hashtags: The hashtags mentioned in the tweet.
user: The username of person tweeted.
date: The date the tweet was posted.
state: The state from which the tweet was posted (Null: 'XXXX').
latitude: The latitude from which the tweet posted (Null: '99999.99').
longitude: The longitude from which the tweet posted (Null: '99999.99').
followers: The number of followers of the user ('-1' if unable to extract the details).
verified: Whether the username is a verifed by Twitter ('-1' if unable to extract the details).
mentioned_location: The location mentioned in the user profile by the user.
We ran ".py" exactly a week after collecting the tweets through "Filter_by_location.py". We found that certain accounts had been deactivated/ banned/ removed. Thus we couldn't exctract the 'followers', 'verifed', 'mentioned_location' of those particular accounts and appended '-1' instead.
The date of collection of the tweets are as follows:
Democ1.csv, Repub1.csv: Aug 19th
Democ2.csv, Repub2.csv: Aug 20th
Democ3.csv, Repub3.csv: Aug 22nd
Democ4.csv, Repub4.csv: Aug 23rd
Democ5.csv, Repub5.csv: Aug 25th
We ran two 'Filter_by_hashtags.py' simultaneously. One contains pro-democratic tweets in 'track' while the other contains pro-republic tweets in 'track'.
Based on this method, we were able to seperated pro-democratic tweets and pro-republic tweets , thereby elliminating the need for manual annotations, and stored them in seperately in a database. This reduced the need of manual labour(by a large margins) and saved us a lot of time(in hours) but came at a cost of reduced accuracy.
The hashtags used for this purpose were:
Pro- Democratic: '#voteblue',' #BlueWave2020', '#UniteBlue','#Biden2020', ''#VoteBlue2020','#Biden2020ToSaveAmerica', '#BidenHarrisLandslide2020','#Biden2020Landslide' , '#BidenHarris2020', '#BlueTsunami', '#VoteBlueToEndThisNightmare', '#BlueDot','#Resistance','#TheResistance','#FBR','#FBRParty','#DumpTrump2020' .
Pro- Republican: #Trump2020Landslide','#FourMoreYears', '#KAGA2020', '#MAGA2020','#Trump2020NowMoreThanEver', '#Trump2020Victory','#KAG2020', '#RedWave2020','#VoteRedToSaveAmerica','#VoteRedToSaveAmerica2020','#keepamericagreat','#donaldtrump2020','#magacountry','#magamovement','#ThatsMyPresident','#donaldtrump2020','#americafirst',''#KeepAmericaGreat','#MakeAmericaGreatAgain','#TrumpRocks','#protrump','#prorepublican',#Trump2020','#TRUMP2020','#DemocratsAreADisgrace','#DemocratsAreDestroyingAmerica','#DemocratsHateAmerica','#DemocratsHaveLostTheirDamnMinds','#DoNothingDemocrats','#Demexit' ,'#Joementia'
We considered anti-Trump as pro-Democratic and anti-Biden as pro-Republican.
We have also collected tweets to perform Sentiment Analysis based on the election results. All the methods of data collection were similar to the methods mentioned earlier.
The date of collection of the tweets are as follows:
sentiday1.csv: Nov 8th
sentiday2.csv: Nov 9th
sentiday3.csv: Nov 11th
sentiday4.csv: Nov 13th
The hashtags used for this purpose were: '#USElection2020',' #USElections2020', '#USAelection2020', '#USElectionResults2020','#uselection2020', '#RaceForTheWhiteHouse', '#POTUS46', '#USPresidentialElections2020', '#USElectionResults' , '#USPresidentialElections','#Elections2020', '#Elections2020results', '#Election2020'.











1.Created a Twitter Streaming model to collect real-time tweets based on location and hashtags and stored the collected tweets in the local database as well as in the cloud.

2.Performed sentiment analysis, bot identification and visualization from the data obtained.

3.Developed a Stack based Machine Learning Algorithm to predict the political orientation of the tweet(Republican/Democratic).

4.Successfully tested the codes using a Kaggle Dataset. Currently, collecting real-time tweets to perform analysis.

5.All the API keys were changed for our privacy.

6.A proper documentation of the project would be uploaded once the project is completed.

7.The project was done together with Arun Kumar (https://github.com/Arun152k).
