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

with open('trainfile1.txt') as f:
    afinnscores = []
    swnscores=[]
    textlist=[]

    for line in f:
        datalist=line.strip().split(',')
        afinnscores.append(float(datalist[0]))
        swnscores.append(float(datalist[1]))
        textlist.append(datalist[2])




amin=min(afinnscores)
if amin<0:
    afinnscores = [x - amin for x in afinnscores]

smin=min(swnscores)
if smin<0:
    swnscores = [x - smin for x in swnscores]

print(afinnscores)
print(swnscores)


a=np.array(afinnscores)
b=np.array(swnscores)

c=np.column_stack((a,b))

enc=OneHotEncoder()

d=enc.fit_transform(c)

d=d.todense()

print(d)


X=np.matrix([[0,1],[2,3]])
Y=np.matrix([[4,5],[6,7]])

print(np.hstack([X,Y]))