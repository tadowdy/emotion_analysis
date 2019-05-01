import mysql.connector
from mysql.connector import Error
import auth
import datetime

# connect and read in data
try:
    connect = mysql.connector.connect(
        host=auth.HOST, database=auth.DATABASE,
        user=auth.USER, password=auth.PASSWORD)
    cursor = connect.cursor()
except Error as e:
    print(e)
    cursor.close()
    connect.close()

query = "select * from "+auth.DATABASE+".tweets ORDER BY createdat;"
cursor.execute(query)
records = cursor.fetchall()

print("total records: "+str(cursor.rowcount))

hours = [{'total': 0.0, 'num': 0, 'avg': 0.0}, {'total': 0.0, 'num': 0, 'avg': 0.0},
         {'total': 0.0, 'num': 0, 'avg': 0.0}, {'total': 0.0, 'num': 0, 'avg': 0.0},
         {'total': 0.0, 'num': 0, 'avg': 0.0}, {'total': 0.0, 'num': 0, 'avg': 0.0},
         {'total': 0.0, 'num': 0, 'avg': 0.0}, {'total': 0.0, 'num': 0, 'avg': 0.0},
         {'total': 0.0, 'num': 0, 'avg': 0.0}, {'total': 0.0, 'num': 0, 'avg': 0.0},
         {'total': 0.0, 'num': 0, 'avg': 0.0}, {'total': 0.0, 'num': 0, 'avg': 0.0},
         {'total': 0.0, 'num': 0, 'avg': 0.0}, {'total': 0.0, 'num': 0, 'avg': 0.0},
         {'total': 0.0, 'num': 0, 'avg': 0.0}, {'total': 0.0, 'num': 0, 'avg': 0.0},
         {'total': 0.0, 'num': 0, 'avg': 0.0}, {'total': 0.0, 'num': 0, 'avg': 0.0},
         {'total': 0.0, 'num': 0, 'avg': 0.0}, {'total': 0.0, 'num': 0, 'avg': 0.0},
         {'total': 0.0, 'num': 0, 'avg': 0.0}, {'total': 0.0, 'num': 0, 'avg': 0.0},
         {'total': 0.0, 'num': 0, 'avg': 0.0}, {'total': 0.0, 'num': 0, 'avg': 0.0}]

# gather average data
for rec in records:
    dt = datetime.datetime.strptime(rec[2], '%Y-%m-%d %H:%M:%S')  # convert
    hours[dt.hour]['total'] += rec[7]
    hours[dt.hour]['num'] += 1

# calculate average
for hour in hours:
    if(hour['num'] is not 0):
        hour['avg'] = hour['total'] / hour['num']

i = 0
for i in range(len(hours)):
    sentiment = ""
    if hours[i]['avg'] > 0:
        sentiment = "positive"
    elif hours[i]['avg'] < 0:
        sentiment = "negitive"
    else:
        sentiment = "neutral"
    print("hour "+str(i)+": "+sentiment)
