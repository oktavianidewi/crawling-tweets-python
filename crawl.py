import time

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from token import *

class listener(StreamListener):
    def on_data(self, data):
        try:
            saveFile = open('twitDB2full.csv', 'a')
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException, e:
            print('failed ondata', str(e))
            time.sleep(5)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(consumerkey, consumersecret)
auth.set_access_token(accesstoken, accesstokensecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["bromo"])