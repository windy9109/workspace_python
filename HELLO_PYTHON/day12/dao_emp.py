import pymysql

class DaoBlog:
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

        
        
    def myinsert(self, title,link,description,bloggername,bloggerlink,postdate):
        sql = f"""insert into blog(title,link,description,bloggername,bloggerlink,postdate) 
                    values ('{title}','{link}','{description}','{bloggername}','{bloggerlink}','{postdate}')"""
        cnt = self.cur.execute(sql)
        #cur.execute(sql2, (4, '4', '4', '4'))
        self.conn.commit()
        return cnt
    
            
    
    def __del__ (self):

        self.cur.close()
        self.conn.close()
        
        
        
if __name__=="__main__" :
    blog = DaoBlog()
    # cnt = blog.myinsert()
    # print("cnt", cnt)
        
    