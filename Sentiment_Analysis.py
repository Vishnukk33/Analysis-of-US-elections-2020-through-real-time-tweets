# To perform Sentiment analysis of the tweets using VADER sentiment analysis.

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import re

pd.options.mode.chained_assignment = None 
for name in range(1,6):
    analyser = SentimentIntensityAnalyzer()
    sentiment=''
    csvname="sentiday"+str(name)+".csv"
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
        # Polarity score ranges from -1 (most extreme negative) to +1 (most extreme positive)
        if (score >= 0.05):
            sentiment=' positive '
        elif (score<0.05 and score>-0.05):
            sentiment='neutral'
        else:
            sentiment='negative'
        data['sentiment'][i]=sentiment

    data.to_csv(csvname,index=False)

