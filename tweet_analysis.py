import textblob
from textblob import sentiments
import pandas as pd
import mysql.connector
import auth

# connect to db
connect = ""
try:
    connect = mysql.connector.connect(
        host=auth.HOST, database=auth.DATABASE,
        user=auth.USER, password=auth.PASSWORD)

except Error as e:
    print(e)

# create dataframes for both tables
df = pd.read_sql("select * from tweets", con=connect)
sent_df = pd.read_sql("select * from sentiments", con=connect)

# analyze tables and store data
for tweet in df['content']:
    analysis = textblob.TextBlob(tweet)
    analysis = analysis.sentiment
    sent_df['sentiment_score'] = analysis[0]
    sent_df['subjective_score'] = analysis[1]

    # set approximate value
    if analysis[0] > 0:
        sent_df['sentiment'] = "positive"
    elif analysis[0] < 0:
        sent_df['sentiment'] = "negative"
    else:
        sent_df['sentiment'] = "neutral"

sent_df.to_sql("sentiments")

connect.close()
