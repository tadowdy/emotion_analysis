import tweepy
import auth as a

consumer_key = a.CONSUMER_KEY
consumer_secret = a.CONSUMER_SECRET
access_token = a.ACCESS_TOKEN
access_secret = a.ACCESS_TOKEN_SECRET

# oauth connection
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
