import re
from difflib import SequenceMatcher
from nltk import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import sentiwordnet as swn
import nltk

afinn = dict(map(lambda p: (p[0],int(p[1])),[ line.split('\t') for line in open("AFINN-111.txt") ]))

def afinnscore(aftweet):
    total=0
    tweets=aftweet.split()
    for tw in tweets:
        score=afinn.get(tw)
        if not(score is None):
            total+=float(afinn.get(tw))
    return total

wnlmz=WordNetLemmatizer()

def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return ''

def lemma(output):
    words = output.split()
    tweet = ""
    for word in words:
        tweet += wnlmz.lemmatize(word)
        tweet += ' '
    tweet.strip()
    return tweet

def wnscore(word,tag):
    pscore=0
    nscore=0
    swnset=[]
    if tag != '':
        swnset=list(swn.senti_synsets(word, tag))
        if len(swnset) > 0:
            pscore = (swnset[0]).pos_score()
            nscore = (swnset[0]).neg_score()
    else:
        swnset = list(swn.senti_synsets(word))
        if len(swnset) > 0:
            pscore = (swnset[0]).pos_score()
            nscore = (swnset[0]).neg_score()

    return (pscore - nscore)



counter=0
with open('TrumpNoSup1.txt',encoding='utf8') as f:
    for line in f:
        tweet=lemma(line)

        tokens = nltk.word_tokenize(tweet)
        tagged = nltk.pos_tag(tokens)

        processed=""
        sum=0
        afscore=0
        for w in tagged:
            tag=get_wordnet_pos(w[1])
            if tag != '':
                word=wnlmz.lemmatize(w[0],get_wordnet_pos(w[1]))
                sum+=wnscore(word,tag)
            else:
                word=wnlmz.lemmatize(w[0])
                sum+=wnscore(word,tag)

            processed+=(word + ' ')

        processed=processed.strip()
        afscore=afinnscore(processed)

        f = open('trainfile1.txt', 'a')
        f.write(str(afscore) + ',' + str(sum) + ',' + processed + '\n')
        f.close()
        counter += 1

print("Tweets: " + str(counter))

