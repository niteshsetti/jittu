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
except Error as e:
    print(e)
