import re
from difflib import SequenceMatcher
from nltk import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import sentiwordnet as swn

import nltk

afinn = dict(map(lambda p: (p[0],int(p[1])),[ line.split('\t') for line in open("AFINN-111.txt") ]))

def afinnscore(processed):
    return sum(map(lambda word: afinn.get(word, 0), processed.lower().split()))

print(afinnscore("hillary clinton stole over delegate to be a illegal counterfeit opponent against donald j trump for president"))

wnlmz=WordNetLemmatizer()

def lemma(output):
    words = output.split()
    tweet = ""
    for word in words:
        tweet += wnlmz.lemmatize(word)
        tweet += ' '
    tweet.strip()
    return tweet


print(lemma("pleaded"))
print(lemma("pleads"))

print(wnlmz.lemmatize("pleaded",pos=wordnet.VERB))

print(wordnet.ADJ)

swnset=list(swn.senti_synsets("hillary",'a'))
print(len(swnset))
pscore=(list(swn.senti_synsets("hillary",'a'))[0]).pos_score()
nscore=(list(swn.senti_synsets("sad",'a'))[0]).neg_score()

print((nltk.pos_tag(["hillary"]))[0])

print(pscore)
print(nscore)