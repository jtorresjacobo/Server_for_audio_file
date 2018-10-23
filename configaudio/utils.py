
import time
import subprocess
import re
import getpass

def date():
	to=time.strftime("%c")
	print("Fecha y hora"+ time.strftime("%c"))
	return to

#get system user
def user():
	user=getpass.getuser()
	return user

def audio_duration(path):	
	process = subprocess.Popen(['ffmpeg',  '-i',path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	stdout, stderr = process.communicate()
	matches = re.search(r"Duration:\s{1}(?P<hours>\d+?):(?P<minutes>\d+?):(?P<seconds>\d+\.\d+?),", stdout, re.DOTALL).groupdict()	
	duracion=matches['hours']+":"+matches['minutes']+":"+matches['seconds']
	
	return  duracion






























