#Import the necessary methods from tweepy library
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import json

#Variables that contains the user credentials to access Twitter API 
consumer_token = 'ToPnkItTnJCjd8I3nqSUrPlYq' #substitute values from twitter website
consumer_secret = 'BxQjGfk3nLI2ifJwDxtoqidNcc4RZNQKzGMBLiz0s83tGsogYz'
access_token = '3473558363-V1vojUD02Sj8eQ8W5mwLHzZ4VVr0V1VI4Ls5ueV'
access_secret = 'QqwobRyno5sLo0iwacGSTN6YITwZ3P2s0hhBPu4gqaMLH'



auth = OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

time_limit = 10000

#This is a basic listener that just prints received tweets to stdout.
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, time_limit = time_limit):
        self.start_time = time.time()
        self.limit = time_limit
        super(MyStreamListener, self).__init__()

    def on_data(self, data):
        if (time.time() - self.start_time) < self.limit:
            try:
                a = json.loads(data)
                #if a.get('geo') is not None:
                print data

            except Exception as e:
                return True
        else:
            return False

    def on_error(self, status):
        print status


if __name__ == '__main__':
    myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener(time_limit= time_limit))
    myStream.filter(track=['leicester city', 'manchester city'])