from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
pd.options.mode.chained_assignment = None 
analyser = SentimentIntensityAnalyzer()
sentiment=''
import re
csvname="twittr1229.csv"
data=pd.read_csv(csvname)
l=[]
data.drop(data.columns[data.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
rows=len(data)
data['sentiment']=" "
for i in range(0,rows):
    s=data['tweetText'][i]
    l.append(s)
    sentiment_data=analyser.polarity_scores(s)
    score=sentiment_data['compound']
    if (score >= 0.05):
        sentiment=' positive '
    elif (score<0.05 and score>-0.05):
        sentiment='neutral'
    else:
        sentiment='negative'
    data['sentiment'][i]=sentiment
data.to_csv(csvname,index=False)
