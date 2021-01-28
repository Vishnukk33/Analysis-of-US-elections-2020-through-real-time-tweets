# Twitter-Project

## Features:
We have incorporated the following in our project:
1. Streaming and collecting real-time tweets based on hashtags, locations and username.
2. Developing Machine Learning Classifiers to predict the political orientation of the tweet.
3. Performing Sentiment Analysis on the collected data.
4. Visualizing and analyzing the data with the help of bar graphs, pie charts, word-clouds and maps. 
5. Indentifying Bots amongst most tweeted users. 

## Dataset Creation:

### Data Collection:

* Used Tweepy Streaming API to stream through real-time tweets.
* Used "Filter_by_hashtags.py" to stream through real-time tweets.
* Stored the collected tweets locally using Sqlite Database as well as in the Cloud using Firebase.
* Tweets collected by "Filter_by_hashtags.py" has the following attributes:
 'tweetText','hashtags','user','date','location','latitude','longitude','state'.
* We further extracted the details of the user using "Getting_details.py". Thus the final attributes include 'tweetText','hashtags','user','date','state','latitude','longitude','followers','verified','mentioned_location'. 
* The reason we have extracted only a few details of the tweets and the detail of the users using "Filter_by_hashtags.py" and collected further details using "Getting_details.py" was to avoid data limit breach. 
* The attributes are explained below to better understand them:
   1. tweetText: The tweet which is of 1 to 280 characters in length. 
   2. hashtags: The hashtags mentioned in the tweet.
   3. user: The username of person tweeted.
   4. date: The date the tweet was posted.
   5. state: The state from which the tweet was posted (Null: 'XXXX').
   6. latitude: The latitude from which the tweet posted (Null: '99999.99'). 
   7. longitude: The longitude from which the tweet posted (Null: '99999.99').  
   8. followers: The number of followers of the user ('-1' if unable to extract the details).
   9. verified: Whether the username is a verifed by Twitter ('-1' if unable to extract the details).
   10. mentioned_location: The location mentioned in the user profile by the user.
 * We ran "Getting_details.py" exactly a week after collecting the tweets through "Filter_by_hashtags.py". We found that certain accounts had been deactivated/banned/removed. Thus we couldn't exctract the 'followers', 'verifed', 'mentioned_location' of those particular accounts and  appended '-1' instead.
 * The date of collection of the tweets are as follows:
    1. Democ1.csv, Repub1.csv: Aug 19th
    2. Democ2.csv, Repub2.csv: Aug 20th
    3. Democ3.csv, Repub3.csv: Aug 22nd
    4. Democ4.csv, Repub4.csv: Aug 23rd 
    5. Democ5.csv, Repub5.csv: Aug 25th
 * We ran two 'Filter_by_hashtags.py' simultaneously. One contains pro-democratic tweets in 'track' while the other contains pro-republic tweets in 'track'.
 * Based on this method, we were able to seperated pro-democratic tweets and pro-republic tweets , thereby elliminating the need for manual annotations, and stored them seperately in a database. This reduced the need for manual labour(by large margins) and saved us a lot of time(in hours) but came at a cost of reduced accuracy.
 * The hashtags used for this purpose were:
    1. Pro- Democratic:
    '#voteblue',' #BlueWave2020', '#UniteBlue','#Biden2020', ''#VoteBlue2020','#Biden2020ToSaveAmerica',  '#BidenHarrisLandslide2020','#Biden2020Landslide' , '#BidenHarris2020', '#BlueTsunami', '#VoteBlueToEndThisNightmare', '#BlueDot','#Resistance','#TheResistance','#FBR','#FBRParty','#DumpTrump2020' .
    2. Pro- Republican:
   #Trump2020Landslide','#FourMoreYears', '#KAGA2020',  '#MAGA2020','#Trump2020NowMoreThanEver', '#Trump2020Victory','#KAG2020', '#RedWave2020','#VoteRedToSaveAmerica','#VoteRedToSaveAmerica2020','#keepamericagreat','#donaldtrump2020','#magacountry','#magamovement','#ThatsMyPresident','#donaldtrump2020','#americafirst',''#KeepAmericaGreat','#MakeAmericaGreatAgain','#TrumpRocks','#protrump','#prorepublican',#Trump2020','#TRUMP2020','#DemocratsAreADisgrace','#DemocratsAreDestroyingAmerica','#DemocratsHateAmerica','#DemocratsHaveLostTheirDamnMinds','#DoNothingDemocrats','#Demexit' ,'#Joementia'
* We considered anti-Trump as pro-Democratic and anti-Biden as pro-Republican.
* We have also collected tweets to perform Sentiment Analysis based on the election results. The Sentiment Analysis focuses to capture how the twitter users feel about the US Elections 2020 results. All the methods of data collection were similar to the methods mentioned earlier.      
 * The date of collection of the tweets are as follows:
    1. sentiday1.csv: Nov 8th 
    2. sentiday2.csv: Nov 9th 
    3. sentiday3.csv: Nov 11th
    4. sentiday4.csv: Nov 13th
 * The hashtags used for this purpose were:
 '#USElection2020',' #USElections2020', '#USAelection2020', '#USElectionResults2020','#uselection2020', '#RaceForTheWhiteHouse', '#POTUS46', '#USPresidentialElections2020', '#USElectionResults' , '#USPresidentialElections','#Elections2020', '#Elections2020results', '#Election2020'.

### Creating Datasets:
* The collected tweets stored in the Database was converted into .csv files so as to facilitate easier data manipulation and processing through python pandas library.
* There are 14 .csv files in total, which include democ1.csv, democ2.csv, democ3.csv, democ4.csv, democ5v, repub1.csv, repub2.csv, repub3.csv, repub4v, repub5.csv and sentiday1.csv, sentiday2.csv, sentiday3.csv, sentiday4.csv.
* "Getting_hashtags_from_tweet.py" was run on these above mentioned datasets in order to extract the additional datasets tagged by the users in their tweets.
* The Data visualization and Analysis, the Machine Learning based predictions were all performed using these .csv files.

## Machine Learning:
* The goal was to predict the political orientation of the tweets using Machine Learning Algorithms.
* The dataset "ML.csv" was created by running "Creating_ML_File.py" on the democ(1..5).csv and repub(1,5).csv.
* "ML.csv" contains 30000 rows in total, consisting of 3000 tweets selected randomly from each of the 10 .csv files i.e democ(1..5).csv and repub(1..5).csv.
* "ML.csv" contains the the tweets and the political orientation of each tweet.
* "ML.csv" is preprocessed so as to make it suitable to feed into Machine Learning Algorithms. The preprocessing is done by "Preprocess.py".
* The processed dataset, is used by "ML_prediction.py" to predict the political orientation of the tweets. 
* "ML_prediction.py" uses standard Machine Learning Algorithms to predict the political orientation of the tweets as well as attempts to use a Stack Based Voting Algorithm.



## Data Visualization and Analysis:

### Initialization and Preprocessing
Files and variables required for visualization were imported and declared in this section.
Reading of the input data as well as the preprocessing( segregation, ordering,etc) for it were carried out here.

### Visualization


<ol type="1">
  <li><h4>Average number of tweets tweeted per user in a day</h4></li>
  
   <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/Average.PNG" width="550" height="400"/>
  
  
  The above results indicate that the average number of tweets per user is slightly higher among republic candidates than democratic candidates and the overall average comes  out to be 1.59 tweets per day.
  <li><h4>Total no. of tweets tweeted per day</h4></li>
    <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/BarGraph_Demo1.png" width="450" height="400"/>          
  
   <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/BarGraph_Rep1.png" width="450" height="400"/>
  
  From the Above graphs we can tell that the total number of republican and democratic supporting tweets are almost comparable during the 5 days that we collected them. 
  
  
  <li><h4>No. of unique users tweeted per day</h4></li>
    <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/BarGraph_Demo2.png" width="450" height="400"/>
    <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/BarGraph_Rep2.png" width="450" height="400"/>
    
  From the Above graphs we can tell that the total number of UNIQUE republican and democratic users are almost comparable during the 5 days that we collected them.
  
  
  <li><h4>Follower distribution</h4></li>
    <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/BarGraph_Followers.png" width="600" height="400"  />
  
  
  The Graph shows how many followers the republic and democratic users have by segregating them into classes. From the above, we can tell that on average republican accounts have more followers than democratic users since the numbers from the republic users are higher in every class. Ofcourse this is limited to only the users from whom we collected the tweets.
  
  
  <li><h4>Tweet count vs Originating State</h4></li>
    <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/BarGraph_DemoTweetcount.png" width="700" height="500"  />
   
   <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/Pie_DemoState.png" width="700" height="600"  />
    
   The above Graphs indicate that California, Florida, New York, Texas and Illinois are the states from which majority of the Democratic Party tweets originate from in descending order. 
    
   <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/BarGraph_RepTweetcount.png" width="700" height="500"  /> 
    
   <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/Pie_RepState.png" width="700" height="600"  />
    
    
   The above Graphs indicate that Texas, California, Florida, New York, and Illinois are the states from which majority of the Republic Party tweets originate from in descending order. 
  <li><h4>Removed vs verified vs non-verfied</h4></li>
  While checking the number of verified accounts we came across something interesting. Many of the accounts from which we had collected tweets earlier had been removed. This is evidence that many accounts which tweeted about the elections were actually fake bots that were designed to spread propaganda to potentially skew the election towards one of the candidates.
   <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/Pie_Verified.png" width="400" height="400"  />
   
   
  These accounts according to some media could be used by different countries to sow discord during the election. From all the tweets we collected,  we found that over half of the twitter accounts that tweeted during these 5 days were in fact removed by the twitter team as they were suspected for being bots. This is an alarmingly large amount of accounts which was used to spread propaganda and fake opinions that could very well have impacted the voters and maybe even tipped the scale towards a certain party. 
  Hopefully the twitter team continuous to remove such malicious fake accounts to prevent any bias towards or against a party due to the propaganda spread.
  
  
  
</ol>  

### Botometer API

  <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/TopDemoTweetsSS.PNG" width="600" height="400"  />
  
 <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/TopRepuTweetsSS.PNG" width="600" height="400"  />

### Top Hashtags

  <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/TopDemoHashSS.PNG" width="500" height="400"  />
  
 <img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/TopRepuHashSS.PNG" width="500" height="400"  />


### Word Clouds
#### List of Most popular hastags as a word cloud  


<img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/wordcloud_dem_hash.jpg" width="500" height="400"  />

<img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/wordcloud_rep_hash.jpg" width="500" height="400"  />


#### Most popular words used in tweets as a world cloud


<img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/wordcloud_dem_tweet.jpg" width="500" height="400"  />

<img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/wordcloud_rep_tweet.jpg" width="500" height="400"  />

### Sentiment Analysis

<img src="https://github.com/Vishnukk33/Twitter-Project/blob/master/Graphs/Pie_Sentiment.png" width="500" height="400"  />



1. Average No. of tweets tweeted per user in a day (dem/rep)
2. Bar graph Total no of tweets tweeted per day (dems/rep)
3. Bar graph No. of unique users tweeted per day (dems/rep)
4. Bar graph groups vs followers (dems/rep)
5. Bar graph Tweet count vs state (dems/rep)
6. pie chart Tweet cout percentage vs state (dems/rep)
7. pie chart removed vs verified vs non-verfied
8. Bot check top 10 most tweeted users in each day (top 2 per day) (dems/repub)
9. Top 10 hashtags with count (dems/rep)
10. Word cloud Hashtags (dems/rep)
11. Word cloud words in tweet (dem/rep)
12. Pie chart Sentiment Analysis on election result
13. Summary of all data counts
14. Mapploter




1.Created a Twitter Streaming model to collect real-time tweets based on location and hashtags and stored the collected tweets in the local database as well as in the cloud.

2.Performed sentiment analysis, bot identification and visualization from the data obtained.

3.Developed a Stack based Machine Learning Algorithm to predict the political orientation of the tweet(Republican/Democratic).

4.Successfully tested the codes using a Kaggle Dataset. Currently, collecting real-time tweets to perform analysis.

5.All the API keys were changed for our privacy.

6.A proper documentation of the project would be uploaded once the project is completed.

7.The project was done together with Arun Kumar (https://github.com/Arun152k).
