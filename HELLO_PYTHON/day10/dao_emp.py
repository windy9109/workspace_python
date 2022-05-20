import pymysql

class DaoEmp:
    def __init__(self):
        # print("Animal:생성자")
        # self.age = 0
        self.conn = pymysql.connect(
        user="root",
        password="python",
        host="127.0.0.1",
        port=3305,
        db="python",
        charset='utf8'
        )
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor) #제이슨 형태

        
    def myselects(self):
        sql = "select e_id, e_name, sex, addr from emp"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        return rows
    
    def myselect(self, e_id):
        sql = f"""select e_id, e_name, sex, addr from emp where e_id={e_id}"""
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        return rows[0]
        
    def myinsert(self, e_id, e_name, sex, addr):
        sql = f"""insert into EMP(e_id,e_name,sex,addr) values ({e_id},{e_name},{sex},{addr})"""
        cnt = self.cur.execute(sql)
        #cur.execute(sql2, (4, '4', '4', '4'))
        self.conn.commit()
        return cnt
    
            
    def myupdate(self, e_name, sex, addr, e_id):
        sql = f"""update EMP set e_name={e_name}, sex={sex}, addr={addr} where e_id={e_id}"""
        cnt = self.cur.execute(sql)
        self.conn.commit()
        return cnt
    
    
    def mydelete(self, e_id):
        sql = f"""delete from EMP where e_id={e_id}"""
        cnt = self.cur.execute(sql)
        self.conn.commit()
        return cnt  
    
    def __del__ (self):

        self.cur.close()
        self.conn.close()
        
        
        
if __name__=="__main__" :
    de = DaoEmp()
    cnt = de.mydelete(3)
    print("cnt", cnt)
        
    