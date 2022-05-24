import mysql.connector
import pandas as pd
table_name="polideportivo"
var=['direccion_id INT','jefe TEXT','area INT','mapa_id INT','evento_id INT']
line=""
db_name='ejercicio3'
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
