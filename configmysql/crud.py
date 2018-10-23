import connection 
import os, sys
import MySQLdb

#insertando audio a la bd 
def Insert(usuario,path,date,duration):

	c=connection.Connect()
	sql="INSERT INTO File(Usuario,Audio,Duracion,Detalles) VALUES (%s,%s,%s,%s)"
	datos=(usuario,path,duration,date)
	connection.Run_query(sql,datos,c)

#def Update():
	#Metodo para actualizar registros

#def Delete():
	#Metodo para eliminar registros
