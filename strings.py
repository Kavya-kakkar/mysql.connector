import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",port=3306,user="root",passwd="12345678",database="cabhub")
if mycon.is_connected()== False:
    print(" error connected  to my sql database")
cursor=mycon.cursor()
#st="select * from  car where charges <30 "
#st="insert into car(v_code,vehicle_name,make,color,capacity,charges) VALUES({},'{}','{}','{}',{},{})".format(109,"bmw","emw","black",4,46)
#st='UPDATE car SET charges=45 WHERE charges=46'
st="DELETE from car WHERE color='black' "
cursor.execute(st)
mycon.commit()
mycon.close()
#data=cursor.fetchall()
#for row in data:
 #   print(row)