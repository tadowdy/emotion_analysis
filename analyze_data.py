import tweepy as tw
import auth

consumer_key = auth.CONSUMER_KEY
consumer_secret = auth.CONSUMER_SECRET
access_token = auth.ACCESS_TOKEN
access_secret = auth.ACCESS_TOKEN_SECRET

# oauth connection
authorization = tw.OAuthHandler(consumer_key, consumer_secret)
authorization.set_access_token(access_token, access_secret)

api = tw.api(authorization)
api.update_status("testing tweepy")
