
import subprocess
import re
import os

path='/home/diego/Escritorio/quechua_next.wav'

def Audio_duracion(paths):
	
	paths=path

	process = subprocess.Popen(['ffmpeg',  '-i',path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	stdout, stderr = process.communicate()
	matches = re.search(r"Duration:\s{1}(?P<hours>\d+?):(?P<minutes>\d+?):(?P<seconds>\d+\.\d+?),", stdout, re.DOTALL).groupdict()
	
	print(matches['hours'])
	#matches['minutes']
	#matches['seconds']
	return j
	

#print matches['minutes']

#print matches['seconds']


Audio_duracion(path)






























