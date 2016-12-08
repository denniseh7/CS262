#Dennis Hsu
#CS262
#12/7/16
#Classifier for Tweets

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder

from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,VotingClassifier

from sklearn.model_selection import cross_val_score
import numpy as np
import random

with open('trainfile1.txt') as f:
    afinnscores = []
    swnscores=[]
    textlist=[]

    for line in f:
        datalist=line.strip().split(',')
        afinnscores.append(float(datalist[0]))
        swnscores.append(float(datalist[1]))
        textlist.append(datalist[2])

shifter=50 #change to positive
flag=True
flag2=True

amin=min(afinnscores)
if amin<0:
    afinnscores = [x + shifter for x in afinnscores]
    flag=False

smin=min(swnscores)
if smin<0:
    swnscores = [x + shifter for x in swnscores]
    flag2=False


a=np.array(afinnscores)
b=np.array(swnscores)

c=np.column_stack((a,b))

enc=OneHotEncoder()

d=enc.fit_transform(c)

d=d.todense()

#count or tfidf
#vec=CountVectorizer(analyzer='word',ngram_range=(2,3))
vec=TfidfVectorizer(analyzer='word',ngram_range=(1,3))

sparsedata=vec.fit_transform(textlist)

e=sparsedata.todense()

x=np.hstack([e,d])

y=[]
for i in range(0,200):
    y.append(1)

for i in range(0,200):
    y.append(0)




#clf=SVC(kernel="linear",probability=True)
#gnb=GaussianNB()
#lgr=LogisticRegression()
#sgd=SGDClassifier("modified_huber")
#knn=KNeighborsClassifier()
#dtc=DecisionTreeClassifier()
#rfc=RandomForestClassifier()

clf2=SVC(kernel="linear",probability=True)
gnb2=GaussianNB()
lgr2=LogisticRegression()
sgd2=SGDClassifier(loss="modified_huber")
knn2=KNeighborsClassifier()
dtc2=DecisionTreeClassifier()
rfc2=RandomForestClassifier()

#voc=VotingClassifier(estimators=[('svc', clf2), ('gnb', gnb2), ('lr',lgr2), ('sgd',sgd2),('knn',knn2),('dtc',dtc2)],voting='soft',weights=[1,1,1,1,1,1])
voc2=VotingClassifier(estimators=[('svc', clf2), ('gnb', gnb2), ('lr',lgr2), ('sgd',sgd2),('knn',knn2),('dtc',dtc2)],voting='hard',weights=[1,1,1,1,1,1])

voc2.fit(x,y)



#reservoir sampling
sample_size=1000
count=0

reslist=[]
randlist=[]
totallist=[]

rescount=0
randcount=0
totalcount=0

resavg=[]
randavg=[]
totalavg=[]

randchosen=[]

resavgcount=0
randavgcount=0
totalavgcount=0

with open('testfeaturefile1.txt') as g:

    for line in g:

        if count%100 == 0:
            print(count)

        if count <1000:

            afinnscores2 = []
            swnscores2 = []
            textlist2 = []

            datalist2=line.strip().split(',')
            afinnscores2.append(float(datalist2[0]))
            swnscores2.append(float(datalist2[1]))
            textlist2.append(datalist2[2])

            if not flag:
                afinnscores2 = [x + shifter for x in afinnscores2]

            if not flag2:
                swnscores2 = [x + shifter for x in swnscores2]

            a2=np.array(afinnscores2)
            b2=np.array(swnscores2)

            c2=np.column_stack((a2,b2))

            d2=enc.transform(c2)

            d2=d2.todense()

            sparsedata2 = vec.transform(textlist2)

            e2 = sparsedata2.todense()

            x2 = np.hstack([e2, d2])

            predicted=voc2.predict(x2)

            #reslist.append(predicted[0])
            #randlist.append(predicted[0])
            totallist.append(predicted[0])

            #rescount+=predicted[0]
            totalcount+=predicted[0]
            #randcount+=predicted[0]
        else:
            afinnscores2 = []
            swnscores2 = []
            textlist2 = []

            r = random.randint(0, count)
            #if r < 999:
                #do prediction and replacement

            datalist2 = line.strip().split(',')
            afinnscores2.append(float(datalist2[0]))
            swnscores2.append(float(datalist2[1]))
            textlist2.append(datalist2[2])

            if not flag:
                afinnscores2 = [x + shifter for x in afinnscores2]

            if not flag2:
                swnscores2 = [x + shifter for x in swnscores2]

            a2 = np.array(afinnscores2)
            b2 = np.array(swnscores2)

            c2 = np.column_stack((a2, b2))

            d2 = enc.transform(c2)

            d2 = d2.todense()

            sparsedata2 = vec.transform(textlist2)

            e2 = sparsedata2.todense()

            x2 = np.hstack([e2, d2])

            predicted = voc2.predict(x2)

            #if (reslist[r]==1):
            #    if predicted[0]==0:
            #        rescount-=1
           # elif(reslist[r]==0):
            #    if predicted[0]==1:
          #          rescount+=1
            #reslist[r]=predicted[0]
            totallist.append(predicted[0])

            #randchosen=random.sample(range(1,count+1),1000)

           #randcount=0
            #for j in randchosen:
            #    randcount+=totallist[j-1]

          #  randavgcount=randcount/1000

          #  randavg.append(randavgcount)

            totalcount += predicted[0]
            #resavgcount=rescount/1000
            #resavg.append(resavgcount)

            totalavgcount=totalcount/(count+1)

            f = open('totalavg.txt', 'a')
            f.write(str(totalavgcount) + '\n')
            f.close()

        count+=1


        #totalavg.append(totalcount/count)




#print(totallist)
#print(totalavg)


