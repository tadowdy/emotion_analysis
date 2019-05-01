"""
last updated: 04/30/2019

Notes:
pandas requires using sqlalchemy--NOT mysql connector
"""

import textblob
from textblob import sentiments
import pandas as pd
import auth
from sqlalchemy import create_engine
import mysql.connector
from mysql.connector import Error

# connect to db
connect = ""
try:
    print("connecting...")
    connect = create_engine(
        "mysql+pymysql://root:password@localhost/twitter_db")
    connect_sql = mysql.connector.connect(
        host=auth.HOST, database=auth.DATABASE,
        user=auth.USER, password=auth.PASSWORD)
    cursor = connect_sql.cursor()

    print("connected")

except:
    print("couldn't connect to the database")
    exit()

# create dataframes for both tables
print("reading dataframe...")
df = pd.read_sql("select * from tweets", con=connect)
print("dataframe complete")

# analyze tables and store data
print("collecting scores...")
f = open("sql.txt", "w+")
for index, row in df.iterrows():
    query = ""
    analysis = textblob.TextBlob(row['content'])
    analysis = analysis.sentiment
    query = 'update twitter_db.tweets set sentiment_score = "' + \
        str(analysis[0])+'" where id = '+str(index)+';\n'
    f.write(query)
    query = 'update twitter_db.tweets set subjective_score = "' + \
        str(analysis[1])+'" where id = '+str(index)+';\n'
    f.write(query)

    # set approximate value
    value = ""
    if analysis[0] > 0:
        value = "positive"
    elif analysis[0] < 0:
        value = "negative"
    else:
        value = "neutral"
    query = 'update twitter_db.tweets set sentiment = "' + \
        value + '" where id = '+str(index)+';\n'
    f.write(query)

print("scores collected")

connect_sql.close()
print("done.")
