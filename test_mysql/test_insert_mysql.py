import pymysql

id = '20120001'
user = 'Bob'
age = 20

db = pymysql.connect(host='localhost',port=3306,user='root',password='951027',db='spiders')
cursor = db.cursor()
sql = 'insert into students(id,name,age) values(%s,%s,%s)'
try:
    cursor.execute(sql,(id,user,age))
    db.commit()
except:
    db.rollback()
db.close()
