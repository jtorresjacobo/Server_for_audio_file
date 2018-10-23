import sox
import os
import controller

def path(path,filename,user):
	destino=path+"/"+"noise_"+filename
	os.system("sox "+path+"/"+filename+ " noise.wav synth whitenoise vol 0.08 && sox -m  "+path+"/"+filename+" noise.wav "+path+"/"+"noise_"+filename)
	

	#ingreso a bd
	controller.main(destino,user)	
