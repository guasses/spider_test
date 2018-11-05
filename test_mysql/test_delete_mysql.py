import pymysql

db = pymysql.connect(host='localhost',port=3306,user='root',password='951027',db='spiders')
cursor = db.cursor()
table='students'
condition = 'age > 20'
sql = 'delete from {table} where {condition}'.format(table=table,condition=condition)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
                     
