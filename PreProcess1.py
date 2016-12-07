#Dennis Hsu
#CS262
#12/6/16

#PreProcess Tweets
#Remove duplicates

import re
from difflib import SequenceMatcher
from nltk import WordNetLemmatizer

tweets=[]
duptweet=""

wnlmz=WordNetLemmatizer()

similarity_threshold=0.6

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

#with open('nortfile1.txt',encoding='utf8') as f:
#    for line in f:
#        cur_tweet=line.strip().lower()
#        tw = next((t for t in tweets if similarity(data.text, t) > similarity_threshold), None)


#test='madonna felt "betrayed" by women when donald trump won the us election. #theurbanbrunch on @ujfm'
#test='#thankyou2016for@ujfm donald trump! hlaodi mostweneng! guptas! death of mandoza &amp; prince. losing jozi &amp; pta to da! cant get any worse that this!'
test='hey donald trump, i heard you like to smell other peopleâ€™s farts. #trump2016 december 06, 2016 at 06:15am dogs'
output=re.sub(r"@[A-Za-z0-9_]+|#",' ',test)#remove @user, hashtags
output=re.sub(r"&amp;","and",output) #change &amp; to and
output=re.sub('[^a-zA-Z]+', ' ', output)

words=output.split()
tweet=""
for word in words:
    tweet+=wnlmz.lemmatize(word)
    tweet+=' '

tweet.strip()
print(tweet)
