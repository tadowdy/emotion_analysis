import tweepy
import mysql.connector
from mysql.connector import Error
import auth
import json
from dateutil import parser


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
            query = "INSERT INTO tweets (username, createdat, content,location, place) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(
                query, (username, created_at, tweet, location, place))
            connect.commit()
    except Error as e:
        print(e)
    cursor.close()
    connect.close()


class TheStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

    def on_data(self, data):
        try:
            raw_data = json.loads(data)
            if 'text' in raw_data:  # if there's text in the data
                username = raw_data['user']['screen_name']
                created_at = parser.parse(raw_data['created_at'])
                tweet = raw_data['text']
                location = raw_data['user']['location']
                # if there's a place
                if raw_data['place'] is not None:
                    place = raw_data['place']['country']
                else:
                    place = None
                connect(username, created_at, tweet, place, location)
        except Error as error:
            print(error)
