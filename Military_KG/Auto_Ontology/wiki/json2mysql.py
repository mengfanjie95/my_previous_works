import pymysql
def prem(db):
  cursor = db.cursor()
  cursor.execute("SELECT VERSION()")
  data = cursor.fetchone()
  print("Database version : %s " % data) # 结果表明已经连接成功

if __name__ == "__main__": # 起到一个初始化或者调用函数的作用
  db = pymysql.connect("127.0.0.1", "123456", "root", "wiki", charset='utf8mb4')
  cursor = db.cursor()
  prem(db)
  reviewdata_insert(db)
  cursor.close()
