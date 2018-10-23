import MySQLdb as mdb
import sys


def Connect():
	_host='localhost'
	_user='root'
	_passwd='jacobo'
	_db='Audios'

	try:
		con = mdb.connect(host=_host,    # tu host, usualmente localhost
		              	  user=_user,         # tu usuario
		                  passwd=_passwd,  # tu password
		                  db=_db) # el nombre de la base de datos
		print("conectado")
		return con	

	except mdb.Error, e:
	    print "Error %d: %s" % (e.args[0],e.args[1])
	    sys.exit(1)	 


def Run_query(sql,datos,conn):
	a=conn.cursor()
	
	a.execute(sql,datos)

	conn.commit()
	
	conn.close()
