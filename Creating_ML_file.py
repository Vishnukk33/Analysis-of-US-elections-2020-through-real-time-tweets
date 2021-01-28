import pandas as pd
import numpy as np
import random

pd.options.mode.chained_assignment = None
final_file=pd.read_csv('ML.csv')
i=1
for name in range(1,6):
    print(name)
    data=pd.read_csv('democ'+str(name)+'.csv')
    rows=len(data)
    index_set=set()
    while len(index_set)<=3000:
        index=random.randint(0, rows-1)
        if index not in index_set:
            index_set.add(index)
            #print(index)
            final_file['Tweet'][i]=data['tweetText'][index]
            final_file['Party'][i]=0
            i+=1

for name in range(1,6):
    print(name)
    data=pd.read_csv('repub'+str(name)+'.csv')
    rows=len(data)
    index_set=set()
    while len(index_set)<3000:
        index=random.randint(0, rows-1)
        if index not in index_set:
            index_set.add(index)
            final_file['Tweet'][i]=data['tweetText'][index]
            final_file['Party'][i]=1
            i+=1
        else:
            continue
final_file.to_csv('ML.csv',index='False')
