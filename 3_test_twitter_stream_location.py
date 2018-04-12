#using Dr Gene's Code, modified by Abishek
from twython import TwythonStreamer
import sys
import json

tweets = []

class MyStreamer(TwythonStreamer):
    '''our own subclass of TwythonStremer'''

    # overriding
    def on_success(self, data):
        if 'lang' in data and data['lang'] == 'en':
            if 'trump' in data['text'].lower():
                tweets.append(data['text'])
        print ('received tweet #', len(tweets), data['text'][:100])
        len_tweets = 200
        sav_list = [i for i in range(10,len_tweets) if i%10 == 0]
        if len(tweets) in  sav_list:
            self.store_json()
        if len(tweets) >= len_tweets:
            self.store_json()
            self.disconnect()

    # overriding
    def on_error(self, status_code, data):
        print (status_code, data)
        self.disconnect()

    def store_json(self):
        #with open('tweet_stream_{}_{}.json'.format(keyword, len(tweets)), 'w') as f:
        with open('tweet_stream_location_{}.json'.format(keyword), 'w') as f:
            json.dump(tweets, f, indent=4)


if __name__ == '__main__':

    #with open('your_twitter_credentials.json', 'r') as f:
    with open('your_twitter_credentials.json', 'r') as f:
        credentials = json.load(f)

    # create your own app to get consumer key and secret
    CONSUMER_KEY = credentials['CONSUMER_KEY']
    CONSUMER_SECRET = credentials['CONSUMER_SECRET']
    ACCESS_TOKEN = credentials['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = credentials['ACCESS_TOKEN_SECRET']

    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    if len(sys.argv) > 1:
        keyword = sys.argv[1]
    else:
        keyword = 'trump'

    stream.statuses.filter(locations='-124.48,32.53,-114.13,42.01')
