import pandas as pd
pd.options.mode.chained_assignment = None
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
csvname="book3.csv"
data=pd.read_csv(csvname)
data.drop(data.columns[data.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
rows=len(data)
corpus=[]
for i in range (0,rows):
    oldtext=data['Tweet'][i]
    #newtext=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",oldtext).split()) 
    newtext=' '.join(re.sub("(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",oldtext).split()) #removes hashtag
   # newtext=' '.join(re.sub("([A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",oldtext).split())
    newtext= re.sub('[^a-zA-Z]'," ",newtext) #removes all other characters other than alphabets
    newtext=newtext.lower()
    newtext=newtext.split()
    ps=PorterStemmer()
    newtext= [ps.stem(word) for word in newtext if word not in set(stopwords.words('english'))]
    newtext=' '.join(newtext)
    print(newtext)
    data['Tweet'][i]=newtext
data.to_csv(csvname,index='False') 
