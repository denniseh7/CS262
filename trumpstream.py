import tweepy
import json

consumer_token="9jVZhmXLepmYSWiFY31bwLTPb"
consumer_secret="nIMcymRK2RZGz2LRJva25GrFx1721yj2adUhGbsbsvUEhqTTLC"

access_token="418316899-cnF7i2wwsMDQTEVmY4z14mnlqqEHzFeNEJpa5gEd"
access_secret="9D9qUPczrIybqnzmve3jxEzWtjkhjNdmuceMd9bXKlICT"


#authentication
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token,access_secret)


api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):
    def __init__(self):
        self.count=0

    def on_data(self, raw_data):
        json_data = json.loads(raw_data)
        if(int(json_data['user']['followers_count'])<10001):
            tweet=json_data['text']
            if "http" not in tweet:
                output=' '.join(tweet.split())
                output+='\n'
                f = open('trumptweet1.txt', 'ab')
                f.write(output.encode('utf-8'))
                f.close()

                self.count += 1
                if(self.count%1000==0):
                    print(str(self.count)+' '+output)


    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False



myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['Donald Trump'],languages=['en'],async=True)