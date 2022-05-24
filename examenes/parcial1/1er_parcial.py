import mysql.connector
def create_database(**kw):
        db_name=kw.get('db_name',None) 
	conexion1=mysql.connector.connect(host="localhost", user="root", passwd="password", database= "" )
	cursor1=conexion1.cursor()
	line="CREATE DATABASE "+db_name
	try:
		cursor1.execute(line)
		conexion1.commit()
		print("The database was created successfully...")
	except Exception as e: print(e)
	conexion1.close()
def create_table(**kw):
	table,var,db_name,line=kw.get('table',None),kw.get('var',[]),kw.get('db_name',None),""
	for a in var: line+=", "+a
	line="CREATE TABLE "+table+" (id INT AUTO_INCREMENT PRIMARY KEY"+line+");"
	print(line)
	conexion1=mysql.connector.connect(host="localhost",user="root",passwd="password",database=db_name)
	cursor1=conexion1.cursor()	
	try:	
		cursor1.execute(line)    
		conexion1.commit()
		print("The SQL table was created successfully...")
	except Exception as e: print(e)
	conexion1.close()
def create_relation(**kw):
    table1,table2,key1,key2,name,db_name=kw.get('table1',None),kw.get('table2',None),kw.get('key1',None),kw.get('key2',None),kw.get('name',None),kw.get('db_name',None)
    line='ALTER TABLE '+table1+' ADD CONSTRAINT '+name+' FOREIGN KEY ('+key1+') REFERENCES '+table2+'('+key2+') ON DELETE CASCADE ON UPDATE CASCADE;'
    print(line)
    try:
        conexion1=mysql.connector.connect(host="localhost", user="root", passwd="password", database=db_name )
        cursor1=conexion1.cursor()
        cursor1.execute(line)
        conexion1.commit()
        print('The SQL relation was added successfully...')
    except Exception as e:print(e)
    conexion1.close()
