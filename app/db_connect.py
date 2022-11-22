import pymysql

def connect():
    connection = pymysql.connect(host='localhost',database='users_db',user='root',password='',cursorclass=pymsql.cursors.DictCursor)

    return connection