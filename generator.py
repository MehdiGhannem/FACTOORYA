import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import math as m
from random import *
t=0
#x=0
phi=m.pi*1/3
"""for j in range(1,3):"""
#while 1:
#for i in range(0,N):
id=0
iMax=randint(6,30)
while (t<=(0.02)):
    u1=round(310*(m.sin(2*m.pi*50*t)),4)
      #u2=round(310*(m.sin(2*m.pi*50*t+phi)),4)
      #u3=round(310*(m.sin(2*m.pi*50*t-phi)),4)
    i1=round(iMax*(m.sin(2*m.pi*50*t+phi)),4)
      #i4=0
    try:
        connection = mysql.connector.connect(host='localhost',
                              database='odhreb_bel_chwaya',
                              port='3307',
                              user='root',
                              password='Dorra@123')
        id += 1
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO `test2`
                                     (`id_mesure`, `tension`, `intensite`,`temps`) VALUES (%s,%s,%s,%s)"""
        val = (id, u1, i1, t)
        result  = cursor.execute(sql_insert_query,val)
        connection.commit()
        print ("Record inserted successfully into python_users table")
    except mysql.connector.Error as error :
         connection.rollback() #rollback if any exception occured
         print("Failed inserting record into python_users table {}".format(error))
    finally:
         #closing database connection.
         if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    t=round(t+0.0001,4)
  # x=x+0.02