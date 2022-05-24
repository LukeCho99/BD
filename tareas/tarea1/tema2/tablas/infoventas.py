import mysql.connector
import pandas as pd
table_name="infoventas"
var=['producto_id INT','precio_actual INT','cantidad INT','total INT']
line=""
db_name='ejercicio2'
for a in var: line+=", "+a
line="CREATE TABLE "+table_name+" (id INT AUTO_INCREMENT PRIMARY KEY"+line+");"
print(line)
conexion1=mysql.connector.connect(host="localhost",user="root",passwd="password",database=db_name)
cursor1=conexion1.cursor()	
try:	
	cursor1.execute(line)    
	conexion1.commit()
	print("The SQL table was created successfully...")
except Exception as e: print(e)
conexion1.close()