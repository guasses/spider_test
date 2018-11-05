import pymysql

db = pymysql.connect(host='localhost',user='root',password='951027',port=3306,db='spiders')
cursor = db.cursor()
sql = 'select * from students where age >= 20'
try:
    cursor.execute(sql)
    print('count: ',cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:',row)
        row = cursor.fetchone()
except:
    print('Error')
    
'''try:
    cursor.execute(sql)
    results = cursor.fetchall()
    print("all: ",results)
    for row in results:
            print(row)
    print("count: ",cursor.rowcount)
    one = cursor.fetchone()
    print("one: ",one)
    
except:
    print('Error')
    #尼玛 游标会向下走
'''
