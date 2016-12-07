import tweepy
import re

filename="trumptweet1.txt"
count=0

with open (filename, encoding='utf8') as f:
    for line in f:
        tweet=line.lower()
        if tweet.startswith("rt"):
            f = open('rtfile1.txt', 'ab')
            f.write(tweet.encode('utf-8'))
            f.close()
        else:
            f = open('nortfile1.txt', 'ab')
            f.write(tweet.encode('utf-8'))
            f.close()
            count+=1

print("TweetCount: " + str(count))

