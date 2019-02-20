import tweepy


class TheStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
