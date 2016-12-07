#Dennis Hsu
#CS262
#12/7/16
#Reservoir Sampling

from nltk import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import sentiwordnet as swn
import nltk

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,VotingClassifier

from sklearn.model_selection import cross_val_score
import numpy as np

with open('trainfile1.txt') as f:
    afinnscores = []
    swnscores=[]
    textlist=[]

    for line in f:
        datalist=line.strip().split(',')
        afinnscores.append(datalist[0])
        swnscores.append(datalist[1])
        textlist.append(datalist[2])

#count or tfidf
#vec=CountVectorizer(analyzer='char_wb',ngram_range=(1,2))
vec=TfidfVectorizer(analyzer='char_wb',ngram_range=(2,4))

sparsedata=vec.fit_transform(textlist)

x=sparsedata.todense()

y=[]
for i in range(0,200):
    y.append(1)

for i in range(0,200):
    y.append(0)




clf=SVC(kernel="linear",probability=True)
gnb=GaussianNB()
lgr=LogisticRegression()
sgd=SGDClassifier("modified_huber")
knn=KNeighborsClassifier()
dtc=DecisionTreeClassifier()
rfc=RandomForestClassifier()

clf2=SVC(kernel="linear",probability=True)
gnb2=GaussianNB()
lgr2=LogisticRegression()
sgd2=SGDClassifier(loss="modified_huber")
knn2=KNeighborsClassifier()
dtc2=DecisionTreeClassifier()
rfc2=RandomForestClassifier()

voc=VotingClassifier(estimators=[('svc', clf2), ('gnb', gnb2), ('lr',lgr2), ('sgd',sgd2),('knn',knn2),('dtc',dtc2)],voting='soft',weights=[1,1,1,1,1,1])
voc2=VotingClassifier(estimators=[('svc', clf2), ('gnb', gnb2), ('lr',lgr2), ('sgd',sgd2),('knn',knn2),('dtc',dtc2)],voting='hard',weights=[1,1,1,1,1,1])


#Reservoir
counter=0
with open('testdatafile1.txt',encoding='utf8') as f:
    for line in f:
        print(line)