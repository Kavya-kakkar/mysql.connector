import mysql.connector as sqltor
mycon = sqltor.connect(host="localhost",port=3306,user="root",passwd="12345678",database="smartindiahackathon")
if mycon.is_connected()== False:
    print("error connected to mysql")
cursor=mycon.cursor() 
#cursor.execute("CREATE DATABASE smartindiahackathon")
#cursor.execute("SHOW DATABASES")
#cursor.execute("CREATE TABLE problem (p_id INT NOT NULL,p_name VARCHAR(60),p_submit INT NOT NULL)")
#cursor.execute("SHOW TABLES")
st="INSERT INTO problem(p_id,p_name,p_submit) VALUES (%s,%s,%s)"
val=[(101,'mdtech',2),(102,'agritech',4),(103,'spacetech',1),(104,'wsa',0)]
#st=("select * from problem")
cursor.executemany(st,val)
mycon.commit()
print(cursor.rowcount,"row were inserted")
#for x in cursor:
 #   print(x)