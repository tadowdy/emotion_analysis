import tweepy
import mysql.connector
from mysql.connector import Error
import auth


class TheStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

    def connect(username, created_at, tweet, place, location):
        """
        connect to MySQL database and insert twitter data
        """
        try:
            connect = mysql.connector.connect(
                host=auth.HOST, database=auth.DATABASE,
                user=auth.USER, password=auth.PASSWORD)

            if connect.is_connected():
                """
                handle data
                """
                cursor = connect.cursor()
                query = "INSERT INTO Golf (username, created_at, tweet, place, location) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(
                    query, (username, created_at, tweet, location, place))
        except Error as e:
            print(e)
