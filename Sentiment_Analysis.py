# To perform Sentiment analysis of the tweets using VADER sentiment analysis.

import pandas as pd
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

pd.options.mode.chained_assignment = None 
analyser = SentimentIntensityAnalyzer()
sentiment=''
for name in range(1,5):
    csvname="sentiday"+str(name)+".csv"
    print(name)
    data=pd.read_csv(csvname)
    data.drop(data.columns[data.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    rows=len(data)
    data['sentiment']=" "
    for i in range(0,rows):
        tweet=data['tweetText'][i]
        cleaned_tweet=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet).split())
        new_tweet= re.sub('[^a-zA-Z]'," ",cleaned_tweet)
        sentiment_data=analyser.polarity_scores(new_tweet)
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
