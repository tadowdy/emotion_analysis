import textblob
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

mysql_df = pd.read_sql("select * from tweets", con=connect)
print("loaded dataframe. Records: ", len(mysql_df))

connect.close()
