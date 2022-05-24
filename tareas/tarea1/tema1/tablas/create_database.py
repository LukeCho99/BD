import mysql.connector
conexion1=mysql.connector.connect(host="localhost", user="root", passwd="password", database= "" )
cursor1=conexion1.cursor()
db_name="ejercicio1"
line="CREATE DATABASE "+db_name
try:
        cursor1.execute(line)
        conexion1.commit()
        print("The database was created successfully...")
except Exception as e: print(e)
conexion1.close()

