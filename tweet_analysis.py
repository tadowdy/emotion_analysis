import textblob
import pandas as pd
import mysql.connector
import auth

# connect to db
try:
    connect = mysql.connector.connect(
        host=auth.HOST, database=auth.DATABASE,
        user=auth.USER, password=auth.PASSWORD)

except Error as e:
    print(e)
connect.close()
