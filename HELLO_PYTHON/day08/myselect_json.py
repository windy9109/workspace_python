# Module Imports
import pymysql
from pymysql import charset

# Connect to MariaDB Platform
def dbconnect():
    conn = pymysql.connect(
        user="root",
        password="python",
        host="127.0.0.1",
        port=3305,
        db="python",
        charset='utf8'
    )
    return conn

def search_data(conn):
    cur = conn.cursor(pymysql.cursors.DictCursor) #제이슨 형태

    sql = 'SELECT * FROM EMP'
    cur.execute(sql)
    rows = cur.fetchall()
    print(rows)


def main():
    conn = dbconnect()
    print('연결완료')
    search_data(conn)
    conn.close()
    print('연결해제')
    

if __name__=="__main__" :
    main()
    