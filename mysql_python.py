import os, sys
import MySQLdb
import signal, os, sys
import utils_day
import user

#database = Audios
#sql command for create database en mysql 
#create table(usuario nvarchar(50), path blob, datalles nvarhcar(80))

def connection():
	db = MySQLdb.connect(host='localhost',    # tu host, usualmente localhost
	                     user='root',         # tu usuario
	                     passwd='jacobo',  # tu password
	                     db='Audios') # el nombre de la base de datos
	return db


def input(path):
	#Conection
	c=connection()
	#cursor
	a=c.cursor()
	
	#get date of audio input to the database for parameter usuario
	details=utils_day.today()
	#get system user for parameters "usuario"
	usuario=user.getuser()
	#get into audio to database
	sql="insert File values('"+usuario+"','"+path+"','"+details+"');"

	a.execute(sql)
	c.commit()

	#close conection
	c.close()













