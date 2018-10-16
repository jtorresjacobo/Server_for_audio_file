import sox
import os

def path(path,filename):
	os.system("sox "+path+"/"+filename+ " noise.wav synth whitenoise vol 0.08 && sox -m  "+path+"/"+filename+" noise.wav "+path+"/"+"noise_"+filename)
	