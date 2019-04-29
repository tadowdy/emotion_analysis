import textblob
from textblob import sentiments
import pandas as pd
import mysql.connector.dbapi
from mysql.connector import Error
import auth
from sqlalchemy import create_engine

# connect to db
connect = ""
try:
    print("connecting...")
    connect = create_engine(
        "mysql+pymysql://root:password@localhost/twitter_db")
    print("connected")
    # connect = mysql.connector.connect(
    #     host=auth.HOST, database=auth.DATABASE,
    #     user=auth.USER, password=auth.PASSWORD)

except Error as e:
    print(e)

# create dataframes for both tables
print("reading dataframe...")
df = pd.read_sql("select * from tweets", con=connect)
print("dataframe complete")
# analyze tables and store data
print("collecting scores...")
for tweet in df['content']:
    analysis = textblob.TextBlob(tweet)
    analysis = analysis.sentiment
    df['sentiment_score'] = analysis[0]
    df['subjective_score'] = analysis[1]

    # set approximate value
    if analysis[0] > 0:
        df['sentiment'] = "positive"
    elif analysis[0] < 0:
        df['sentiment'] = "negative"
    else:
        df['sentiment'] = "neutral"
print("scores collected")
print(df)
df.to_sql("sentiments", connect, if_exists='append')

connect.close()
