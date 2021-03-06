import pymysql

db = pymysql.connect(host='localhost',port=3306,user='root',password='951027',db='spiders')
cursor = db.cursor()
data = {
    'id':'20120002',
    'name':'bob',
    'age':20
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))
sql = 'insert into {table}({keys}) values({values})'.format(table=table,keys=keys,values=values)
try:
    if cursor.execute(sql,tuple(data.values())):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
