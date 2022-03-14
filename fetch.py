from msilib.schema import Error
import mysql.connector
try:
     connection= mysql.connector.connect(
     host="localhost",
     user="root",
     password="tiger",
     database="face"
    )
     if connection.is_connected():
         print("Connected to MYSQL database Successfully")
         mycursor = connection.cursor()
         sql="SELECT Email from register where ID = %s"
         mycursor.execute(sql,(1,))
         myresult = mycursor.fetchall()
         for x in myresult:
            for t in x:
                print(t)
except Error as e:
    print(e)
