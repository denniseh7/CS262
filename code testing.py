import re
from difflib import SequenceMatcher
from nltk import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import sentiwordnet as swn
import nltk

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

counter=0
with open('noduprtfile1.txt',encoding='utf8') as f:
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
            else:
                word=wnlmz.lemmatize(w[0])

            processed+=(word + ' ')

        processed=processed.strip()


        f = open('testdatafile1.txt', 'a')
        f.write(processed + '\n')
        f.close()
        counter += 1

print("Tweets: " + str(counter))