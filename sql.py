import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",port=3306,user="root",passwd="12345678",database="cabhub")
if mycon.is_connected():
    print("successfully connected  to my sql database")
cursor=mycon.cursor()
cursor.execute("select* from car")
data=cursor.fetchone()
count=cursor.rowcount
print("total no of rows:",count)
data=cursor.fetchmany()
count=cursor.rowcount
print("total no of rows",count)
data=cursor.fetchall()
count=cursor.rowcount
print("total no of rows",count)
mycon.close()