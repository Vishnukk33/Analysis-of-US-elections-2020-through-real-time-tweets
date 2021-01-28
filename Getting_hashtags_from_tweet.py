import pandas as pd
import re

pd.options.mode.chained_assignment = None 
for name in range(1,6):
    print("Name ",name)
    csvname="twittr"+name+".csv"
    data=pd.read_csv(csvname)
    data.drop(data.columns[data.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    rows=len(data)
    for i in range (0,rows):
            #print(i)
            hashtags_final=[]
            hashperrow=[]
            s=data['tweetText'][i]
            # removing URLs and usernames from the tweet text.
            result = re.sub(r"http\S+", "", s)
            result= re.sub('@[^\s]+',' ',result)
            q=result.strip()
            q.replace(" ","")
            result=" ".join(q.split())
            for word in result.split():
                # searching for hashtags.
                q=re.search('#[a-zA-Z0-9_#]+$',word)
                if q is not None:
                    hashperrow.append(q.group(0))
                    has=set(hashperrow)
                    hashperrow=list(has)
                    """The next 'if' block is used to disect hashtags without spaces.
                     eg: "#Trump#Redwave" would be broken down to "#Trump" and "#Redwave". """
                    if hashperrow is not None:
                        for hashtag in hashperrow:
                            hash_tag=hashtag.split('#')
                            hash_tag.remove('')
                            if hash_tag is not None:
                                hashtags_final.extend(hash_tag)
                        hashtags_final=list(set(hashtags_final))
            data['hashtags'][i]=hashtags_final
            #print(hashtags_final)    
    data.to_csv(csvname,index=False)




