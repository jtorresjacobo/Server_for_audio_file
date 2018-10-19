
import time
import subprocess
import re
import getpass


def Util_today():
	to=time.strftime("%c")
	print("Fecha y hora"+ time.strftime("%c"))
	return to




#get system user
def Util_getuser():
	user=getpass.getuser()
	return user




def Utils_Audio_duracion(paths):
	
	path=paths

	process = subprocess.Popen(['ffmpeg',  '-i',path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	stdout, stderr = process.communicate()
	matches = re.search(r"Duration:\s{1}(?P<hours>\d+?):(?P<minutes>\d+?):(?P<seconds>\d+\.\d+?),", stdout, re.DOTALL).groupdict()
	
	duracion=matches['hours']+":"+matches['minutes']+":"+matches['seconds']
	
	return  duracion






























