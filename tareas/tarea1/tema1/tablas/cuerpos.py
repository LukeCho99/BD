import mysql.connector
import pandas as pd
table_name="cuerpos"
var=['articulo_id INT','cantidad INT']
line=""
for a in var: line+=", "+a
line="CREATE TABLE "+table_name+" (id INT AUTO_INCREMENT PRIMARY KEY"+line+");"
print(line)
conexion1=mysql.connector.connect(host="localhost", user="root", passwd="password", database= "ejercicio1" )
cursor1=conexion1.cursor()	
try:	
	cursor1.execute(line)    
	conexion1.commit()
	print("The SQL table was created successfully...")
except Exception as e: print(e)
conexion1.close()
