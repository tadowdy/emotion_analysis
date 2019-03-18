import tweepy
import auth as a
from db_stream import TheStreamListener

consumer_key = a.CONSUMER_KEY
consumer_secret = a.CONSUMER_SECRET
access_token = a.ACCESS_TOKEN
access_secret = a.ACCESS_TOKEN_SECRET

# oauth connection
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
# reading tweets from feed (for testing connection)
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# creating a stream
s_listener = TheStreamListener()
my_stream = tweepy.Stream(auth=api.auth, listener=s_listener)

# track a stream by a word
my_stream.filter(track=['stl', 'work'])

# for tracking by a single user
# myStream.filter(follow=["2211149702"])
