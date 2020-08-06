import pandas as pd
pd.options.mode.chained_assignment = None 
import re
csvname="twittr1229.csv"
data=pd.read_csv(csvname)
data.drop(data.columns[data.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
rows=len(data)
for i in range (0,rows):
    hashtags=[]
    hashperrow=[]
    s=data['tweetText'][i]
    result = re.sub(r"http\S+", " ", s)
    result= re.sub('@[^\s]+',' ',result)
    q=result.strip()
    q.replace(" ","")
    result=" ".join(q.split())
    for word in result.split():
        q=re.search('^#[a-zA-Z0-9_]+$',word)
        if q is not None:
            hashperrow.append(q.group(0))
            has=set(hashperrow)
            hashperrow=list(has)      
            if hashperrow is not None:
                for hashtag in hashperrow:
                    hashtagk=hashtag.split('#')
                    hashtagk.remove('')
                    if hashtagk is not None:     
                        hashtags.extend(hashtagk)
            hashtagsg=set(hashtags)
            hashtags=list(hashtagsg)
            data['hashtags'][i]=hashtags
    data['tweetText'][i]=result
    #data['description'][i]=str(data['description'][i])
    #data['description'][i]=data['description'][i].encode('utf-8')
data.to_csv(csvname,index=False)
