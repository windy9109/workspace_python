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
    
    e_id= "5"
    sql = f"""delete from EMP where e_id={e_id}"""
    #f를 붙이면 변수에 값을 넣고 바로 쓸수있다. %s를 주지 않아도 된다.
    # 문자열 포멧팅(f-string) - 안쓸수도있다.
    
    
    cnt = cur.execute(sql)
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
    