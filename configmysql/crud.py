import connection 
import os, sys
import MySQLdb

def Insert(usuario,path,date,duration):

	c=connection.Connect()
	a=c.cursor()

	sql="insert File values('"+usuario+"','"+path+"','"+duration+"','"+date+"');"
	a.execute(sql)

	c.commit()
	
	c.close()

#def Update():
	#Metodo para actualizar registros

#def Delete():
	#Metodo para eliminar registros
