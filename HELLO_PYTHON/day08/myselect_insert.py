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
    cur = conn.cursor() #제이슨 형태
    
    sql = """insert into EMP(e_id,e_name,sex,addr) values (%s, %s, %s, %s)"""
    cnt = cur.execute(sql, (5, '3', '3', '3'))
    #cnt
    print("cnt", cnt)
    #cur.execute(sql2, (4, '4', '4', '4'))
    conn.commit()


def main():
    conn = dbconnect()
    print('연결완료')
    search_data(conn)
    conn.close()
    print('연결해제')
    

if __name__=="__main__" :
    main()
    