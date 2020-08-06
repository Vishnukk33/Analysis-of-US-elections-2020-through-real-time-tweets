import pandas as pd
pd.options.mode.chained_assignment = None
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
from sklearn.metrics import accuracy_score 
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from vecstack import stacking
csvname="book3.csv"
data=pd.read_csv(csvname)
rows=len(data)

corpus=[]
y=[]
for i in range(rows):
    newtext=data['Tweet'][i]
    if(len(str((newtext)))!=0 and str(newtext)!='nan'):
        corpus.append(newtext)
        y.append(data['Party'][i])
    print(i)

vectorizer = TfidfVectorizer(min_df=50,max_features=1500)
vectorizer.fit(corpus)
X1 = vectorizer.transform(corpus)
X1=X1.toarray()

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X2 = cv.fit_transform(corpus).toarray()

y = np.array(y)

from sklearn.model_selection import train_test_split
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y, test_size = 0.2, random_state = 0)
from sklearn.model_selection import train_test_split
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y, test_size = 0.2, random_state = 0)

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
lda = LDA(n_components =2)
X1_train = lda.fit_transform(X1_train, y1_train)
X1_test = lda.transform(X1_test)

lda = LDA(n_components =2)
X2_train = lda.fit_transform(X2_train, y2_train)
X2_test = lda.transform(X2_test)


from sklearn.svm import SVC
from sklearn import svm
SVC1 = SVC(kernel = 'linear', random_state = 0)
SVC1.fit(X1_train, y1_train)

SVC2 = SVC(kernel = 'linear', random_state = 0)
SVC2.fit(X2_train, y2_train)

from sklearn.ensemble import AdaBoostClassifier
adaboostSVC1 = AdaBoostClassifier(n_estimators=50, base_estimator= SVC1,learning_rate=1, random_state = 1,algorithm='SAMME')
adaboostSVC1.fit(X1_train,y1_train)

adaboostSVC2 = AdaBoostClassifier(n_estimators=50, base_estimator= SVC2,learning_rate=1, random_state = 1,algorithm='SAMME')
adaboostSVC2.fit(X2_train,y2_train)


from xgboost import XGBClassifier
XGB1 = XGBClassifier()
XGB1.fit(X1_train, y1_train)

XGB2 = XGBClassifier()
XGB2.fit(X2_train, y2_train)

from sklearn.ensemble import RandomForestClassifier
RF1 = RandomForestClassifier(n_estimators = 100, criterion = 'entropy', random_state = 0)
RF1.fit(X1_train, y1_train)
RF2 = RandomForestClassifier(n_estimators = 100, criterion = 'entropy', random_state = 0)
RF2.fit(X2_train, y2_train)

from sklearn.tree import DecisionTreeClassifier
DT1 = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
DT1.fit(X1_train, y1_train)

DT2= DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
DT2.fit(X2_train, y2_train)

from sklearn.ensemble import VotingClassifier

eclf1 = VotingClassifier(estimators=[
     ('RF1',RF1),('adaboostSVC1',adaboostSVC1),('XGB1',XGB1)], voting='soft')
eclf1.fit(X1_train, y1_train)
y1_pred=eclf1.predict(X1_test)
print(accuracy_score(y1_test,y1_pred)) #Output 0.6799696345298775

eclf2 = VotingClassifier(estimators=[
     ('RF2',RF2),('adaboostSVC2',adaboostSVC2),('XGB2',XGB2)], voting='soft')
eclf2.fit(X2_train, y2_train)
y2_pred=eclf1.predict(X2_test)
print(accuracy_score(y2_test,y2_pred)) #Output 0.6747641253660124

eclf = VotingClassifier(estimators=[
      ('eclf1',eclf1),('eclf2',eclf2)], voting='soft')

eclf.fit(X2_train, y2_train)
y_pred=eclf1.predict(X2_test)
print(accuracy_score(y2_test,y_pred)) #Output 0.6747641253660124

#I tried boosting the resultant voting classifier using the below lines
'''
adaboost= AdaBoostClassifier(n_estimators=50, base_estimator= eclf,learning_rate=1,algorithm='SAMME')
adaboost.fit(X2_train,y2_train)
adaboost.predict(X2_test)'''
#But I got this error
''' ValueError: BaseClassifier in AdaBoostClassifier ensemble is worse than random, ensemble can not be fit.'''

#I tried getting the accuracy of individual classifiers and SVC alone seems to outperform the previous ensemble model

#Individual Classifiers

y_pred=DT1.predict(X1_test)
print(accuracy_score(y1_test,y_pred)) #Output 0.6437479665979828

y_pred=DT2.predict(X2_test)
print(accuracy_score(y2_test,y_pred)) #Output 0.6489534757618479

y_pred=XGB1.predict(X1_test)
print(accuracy_score(y1_test,y_pred)) #Output 0.6942847847305065

y_pred=XGB2.predict(X2_test)
print(accuracy_score(y2_test,y_pred)) #Output 0.6997071901095326

y_pred=RF1.predict(X1_test)
print(accuracy_score(y1_test,y_pred)) #Output 0.6439648628131439

y_pred=RF2.predict(X2_test)
print(accuracy_score(y2_test,y_pred)) #Output 0.6493872681921701

y_pred=SVC1.predict(X1_test)
print(accuracy_score(y1_test,y_pred)) #Output 0.6978635722806638

y_pred=SVC2.predict(X2_test)
print(accuracy_score(y2_test,y_pred)) #Output 0.7022014965838846

y_pred=adaboostSVC1.predict(X1_test)
print(accuracy_score(y1_test,y_pred)) #Output 0.6953692658063116

y_pred=adaboostSVC2.predict(X2_test)
print(accuracy_score(y2_test,y_pred)) #Output 0.6959115063442143
