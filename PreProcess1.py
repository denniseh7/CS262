#Dennis Hsu
#CS262
#12/6/16

#PreProcess Tweets
#Remove duplicates

import re
from difflib import SequenceMatcher
from nltk import WordNetLemmatizer

latest_tweets=[]
duptweet=""

wnlmz=WordNetLemmatizer()

similarity_threshold=0.6

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def lemma(output):
    output = re.sub(r"@[A-Za-z0-9_]+|#", ' ', output)  # remove @user, hashtags
    output = re.sub(r"&amp;", "and", output)  # change &amp; to and
    output = re.sub('[^a-zA-Z]+', ' ', output)

    words = output.split()
    tweet = ""
    for word in words:
        tweet += wnlmz.lemmatize(word)
        tweet += ' '

    tweet.strip()
    return tweet

counter=0
with open('nortfile1.txt',encoding='utf8') as f:
    for line in f:
        output = line.strip().lower()
        output = re.sub(r"@[A-Za-z0-9_]+|#", ' ', output)  # remove @user, hashtags
        output = re.sub(r"&amp;", "and", output)  # change &amp; to and
        output = re.sub('[^a-zA-Z]+', ' ', output)
        output=' '.join(output.split())
        if len(latest_tweets)>0:
            tw = next((t for t in latest_tweets if similarity(output, t) > similarity_threshold), None)
            if tw == None:
                latest_tweets.append(output)
                if len(latest_tweets)>300:
                    for t in latest_tweets:
                        t+='\n'
                        f = open('noduprtfile1.txt', 'a')
                        f.write(t)
                        f.close()
                    latest_tweets=[]
                    print("wrote " + str(counter))
        else:
            latest_tweets.append(output)

        counter+=1
        if counter%100==0:
            print(counter)




#test='madonna felt "betrayed" by women when donald trump won the us election. #theurbanbrunch on @ujfm'
#test='#thankyou2016for@ujfm donald trump! hlaodi mostweneng! guptas! death of mandoza &amp; prince. losing jozi &amp; pta to da! cant get any worse that this!'
#test='hey donald trump, i heard you like to smell other peopleâ€™s farts. #trump2016 december 06, 2016 at 06:15am dogs'


