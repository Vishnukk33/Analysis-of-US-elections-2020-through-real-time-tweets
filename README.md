# Twitter-Project

## Introduction:
This project is an attempt to collect, process, and analyze data on United States Elections 2020. My friend Arun Kumar(https://github.com/Arun152k) and I decided to proceed with this project because we wanted to know how it feels to solve a real-world problem where we need to do everything from scratch including collecting data, creating and processing data-sets, and recording our observations. We felt undertaking this project, would increase our knowledge domain and motivate us to venture into new fields.    

## Features:
We have incorporated the following in our project:
1. Streaming and collecting real-time tweets based on hashtags, locations, and username.
2. Developing Machine Learning Classifiers to predict the political orientation of the tweet.
3. Performing Sentiment Analysis on the collected data.
4. Visualizing and analyzing the data with the help of bar graphs, pie charts, word-clouds, and maps.
5. Identifying Bots amongst most tweeted users.

## Dataset Creation:

### Data Collection:

* Used Tweepy Streaming API to stream through real-time tweets.
* Used "Filter_by_hashtags.py" to stream through real-time tweets.
* Stored the collected tweets locally using ‘Sqlite’ Database as well as in the Cloud using Firebase.
* Tweets collected by "Filter_by_hashtags.py" has the following attributes:
 'tweetText','hashtags','user','date','location','latitude','longitude','state'.
* We further extracted the details of the user using "Getting_details.py". Thus the final attributes include 'tweetText','hashtags','user','date','state','latitude','longitude','followers','verified','mentioned_location'.
* The reason we have extracted only a few details of the tweets and the detail of the users using "Filter_by_hashtags.py" and collected further details using "Getting_details.py" was to avoid data limit breach.
* The attributes are explained below to better understand them:
   1. tweetText: The tweet is 1 to 280 characters in length.
   2. hashtags: The hashtags mentioned in the tweet.
   3. user: The username of person who tweeted.
   4. date: The date the tweet was posted.
   5. state: The state from which the tweet was posted (Null: 'XXXX').
   6. latitude: The latitude from which the tweet was posted (Null: '99999.99').
   7. longitude: The longitude from which the tweet was posted (Null: '99999.99').  
   8. followers: The number of followers of the user ('-1' if unable to extract the details).
   9. verified: Whether the username is verified by Twitter ('-1' if unable to extract the details).
   10. mentioned_location: The location mentioned in the user profile by the user.
 * We ran "Getting_details.py" exactly a week after collecting the tweets through "Filter_by_hashtags.py". We found that certain accounts had been deactivated/banned/removed. Thus we couldn't extract the 'followers', 'verified', 'mentioned_location' of those particular accounts and appended '-1' instead.
 * The dates on which the tweets were collected are as follows:
    1. Democ1.csv, Repub1.csv: Aug 19th
    2. Democ2.csv, Repub2.csv: Aug 20th
    3. Democ3.csv, Repub3.csv: Aug 22nd
    4. Democ4.csv, Repub4.csv: Aug 23rd
    5. Democ5.csv, Repub5.csv: Aug 25th
 * We ran two 'Filter_by_hashtags.py' simultaneously. One contains pro-democratic hashtags in 'track' while the other contains pro-republic hashtags in 'track' (see code).
 * Based on this method, we were able to separate pro-democratic tweets and pro-republic tweets, thereby eliminating the need for manual annotations and stored them separately in a database. This reduced the need for manual labor (by large margins) and saved us a lot of time(in hours) but came at a cost of reduced accuracy.
 * The hashtags used for this purpose were:
    1. Pro-Democratic:
    '#voteblue',' #BlueWave2020', '#UniteBlue','#Biden2020', ''#VoteBlue2020','#Biden2020ToSaveAmerica',  '#BidenHarrisLandslide2020','#Biden2020Landslide' , '#BidenHarris2020', '#BlueTsunami', '#VoteBlueToEndThisNightmare', '#BlueDot','#Resistance','#TheResistance','#FBR','#FBRParty','#DumpTrump2020' .
    2. Pro-Republican:
   #Trump2020Landslide','#FourMoreYears', '#KAGA2020',  '#MAGA2020','#Trump2020NowMoreThanEver', '#Trump2020Victory','#KAG2020', '#RedWave2020','#VoteRedToSaveAmerica','#VoteRedToSaveAmerica2020','#keepamericagreat','#donaldtrump2020','#magacountry','#magamovement','#ThatsMyPresident','#donaldtrump2020','#americafirst',''#KeepAmericaGreat','#MakeAmericaGreatAgain','#TrumpRocks','#protrump','#prorepublican',#Trump2020','#TRUMP2020','#DemocratsAreADisgrace','#DemocratsAreDestroyingAmerica','#DemocratsHateAmerica','#DemocratsHaveLostTheirDamnMinds','#DoNothingDemocrats','#Demexit' ,'#Joementia'
* We considered anti-Trump as pro-Democratic and anti-Biden as pro-Republican.
* We have also collected tweets to perform Sentiment Analysis based on the election results. The Sentiment Analysis focuses to capture how Twitter users feel about the US Elections 2020 results.
 * The date of collection of the tweets are as follows:
    1. sentiday1.csv: Nov 8th
    2. sentiday2.csv: Nov 9th
    3. sentiday3.csv: Nov 11th
    4. sentiday4.csv: Nov 13th
    (These .csv files were used solely for Sentiment Analysis).
 * The hashtags used for this purpose were:
 '#USElection2020',' #USElections2020', '#USAelection2020', '#USElectionResults2020','#uselection2020', '#RaceForTheWhiteHouse', '#POTUS46', '#USPresidentialElections2020', '#USElectionResults' , '#USPresidentialElections','#Elections2020', '#Elections2020results', '#Election2020'.

### Creating Datasets:
* The collected tweets stored in the Database was converted into .csv files so as to facilitate easier data manipulation and processing through python pandas library.
* There are 14 .csv files in total, which include democ1.csv, democ2.csv, democ3.csv, democ4.csv, democ5.csv, repub1.csv, repub2.csv, repub3.csv, repub4.csv, repub5.csv and sentiday1.csv, sentiday2.csv, sentiday3.csv, sentiday4.csv.
* "Getting_hashtags_from_tweet.py" was run on these above mentioned datasets in order to extract the additional datasets tagged by the users in their tweets.
* The Data visualization, analysis and the Machine Learning based predictions were all performed using these .csv files.

## Machine Learning:
* The goal was to predict the political orientation of the tweets using Machine Learning Algorithms.
* The dataset "ML.csv" was created by running "Creating_ML_File.py" on the democ(1..5).csv and repub(1..5).csv.
* "ML.csv" contains 30000 rows in total, consisting of 3000 tweets selected randomly from each of the 10 .csv files i.e democ(1..5).csv and repub(1..5).csv.
* "ML.csv" contains the the tweets and the political orientation of each tweet.
* "ML.csv" is preprocessed so as to make it suitable to feed into Machine Learning Algorithms. The preprocessing is done by "Preprocess.py".
* The processed dataset, is used by "ML_prediction.py" to predict the political orientation of the tweets.
* "ML_prediction.py" uses standard Machine Learning Algorithms to predict the political orientation of the tweets as well as attempts to use a Stack Based Voting Algorithm.
* ".ipynb" file contains the entire sequence in a single file. The accuracy obtained through each algorithm is mentioned in this file.

### Note:
* The collected tweets/data is publicly available and have been tweeted by public twitter handles. These tweets/data were collected and uploaded only for strict academic purposes.  
* We have used the terms republican and democratic as synonyms for users who tend to be politically oriented towards the republic and democratic party respectively.



## Data Visualization and Analysis:
The entire visualization and analysis can be found in the file named 'Data_Visualization.ipynb'


### Visualization

*Pictures speak a thousand words*

<ol type="1">
  <li><h4>Average number of tweets tweeted per user in a day</h4></li>
  
   <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/Average.PNG" width="550" height="400"/>
  
  
  The above results indicate that the average number of tweets per user is slightly higher among the republican supporters than the democratic supporters. The overall average comes out to be 1.59 tweets per day.
  <li><h4>Total no. of tweets tweeted per day</h4></li>
    <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/BarGraph_Demo1.png" width="600" height="400"/>          
  
   <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/BarGraph_Rep1.png" width="600" height="400"/>
  
  From the Above graphs we can tell that the total number of republican and democratic supporting tweets are almost comparable during the 5 days that we collected them. 
  
  
  <li><h4>No. of unique users tweeted per day</h4></li>
    <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/BarGraph_Demo2.png" width="600" height="400"/>
    <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/BarGraph_Rep2.png" width="600" height="400"/>
    
  From the Above graphs we can tell that the total number of UNIQUE republican and democratic users are almost comparable during the 5 days that we collected them.
  
  
  <li><h4>Followers distribution</h4></li>
    <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/BarGraph_Followers.png" width="600" height="400"  />
  
  
  The Graph shows how many followers the republican and democratic users have by segregating them into classes(0-50,50-200,200-1000,1000 and above). For example if a user has 250 followers, he would be placed under the third class(200-1000). From the above, we can tell that on average republican accounts have more followers than democratic users since the numbers from the republic users are higher in every class. Ofcourse this is limited to only the users from whom we collected the tweets.
  
  
  <li><h4>Tweet count vs Originating State</h4></li>
    <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/BarGraph_DemoTweetcount.png" width="700" height="500"  />
   
   <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/Pie_DemoState.png" width="700" height="600"  />
    
   The above Graphs indicate that California, Florida, New York, Texas and Illinois are the states from which majority of the tweets supporting the Democratic Party originate ( in descending order). 
    
   <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/BarGraph_RepTweetcount.png" width="700" height="500"  /> 
    
   <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/Pie_RepState.png" width="700" height="600"  />
    
    
   The above Graphs indicate that Texas, California, Florida, New York, and Illinois are the states from which majority of the tweets supporting the Republican Party originate(in descending order)
   
  <li><h4>Removed vs verified vs non-verfied</h4></li>
  While checking the number of verified accounts we came across something interesting. Many of the accounts from which we had collected tweets earlier were not available. This is because those accounts were either banned(by Twitter) or deactivated. This suggests that a good number of accounts which tweeted about the elections were actually fake bots that were designed to spread propaganda to potentially skew the election towards one of the candidates. These accounts according to some media-outlets may have been used by different countries to sow discord during the election. This article here goes into more detail:                                                                                                         
  
   <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/Pie_Verified.png" width="400" height="400"  />
</ol>  

### Botometer API
In order to check if the top most tweeted user's were bots or not, we used an API called Botometer. After running the API on the top 2 tweeters of each of day totalling to 9 users(since one of the top tweeters were repeated) for republican and democratic supporters, we found the following:


  <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/TopDemoTweetsSS.PNG" width="500" height="450"  />
  
  
 <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/TopRepuTweetsSS.PNG" width="500" height="450"  />


The Accounts marked as unkown are either set to private or removed so we weren't be able to check if its a bot or not. Nevertheless,
We had some interesting findings such as:
* With a threshold of 60%, 10 out of 12 public users were found to be bots and with a threshold of 40% all of them were marked as bots.
* One user made the top for both most number of democratic as well republican tweets. We can conlude that this was most likely some kind of spam bot.
* Some users consistently maintained the most number of tweets for more than a day also showing us that these where extremely active accounts and may have also been spam bots.

### Top Hashtags
The images below show the top 10 most popular hashtags in the tweets that we collected in the democratic and republican data-sets respectively:

  <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/TopdemoHashSS.PNG" width="500" height="400"  />
  
 <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/ToprepHashSS.PNG" width="500" height="400"  />

From the above images we can infer that Trump2020 was the most popular tweet with a whopping 47k tweets followed by BidenHarris2020 at 41k.

### Word Clouds
#### *List of Most popular hashtags as a word cloud  

We have represented the most popular hashtags as word clouds since it is more appealing and serves as a better illustration.

<img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/wordcloud_dem_hash.jpg" width="500" height="400"  />

<img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/wordcloud_rep_hash.jpg" width="500" height="400"  />


#### *Most popular words used in tweets as a world cloud

We have represented the most frequently occurring words in the tweets as word clouds as well.
<img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/wordcloud_dem_tweet.jpg" width="500" height="400"  />

<img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/wordcloud_rep_tweet.jpg" width="500" height="400"  />

### Sentiment Analysis

We performed sentiment analysis on a separate data-set as mentioned earlier and the results obtained is shown below.

<img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/Pie_Sentiment.png" width="500" height="400"  />

To perform sentiment analysis we used the  Vader sentiment analysis API on the data-set. From the image you can tell that almost 50% of the tweets are positive in nature. This suggests that almost half of the users have a positive outlook on the elections results.

### Mapploter




## Conclusion
