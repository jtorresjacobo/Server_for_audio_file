import os
import controller

def audio(path,filename):
	#audio fomat wav
	file=filename

	#audio file name's
	filename=filename.split(".")
	os.system("ffmpeg -i '"+path+"/"+file+"' -acodec pcm_s16le -ac 1 -ar 16000 '"+path+"/"+filename[0]+"_features.wav"+"'")
	#os.system("rm '"+path+archivo+"'")
	destino=path+"/"+filename[0]+"_features.wav"

	#ingreso a bd
	controller.main(destino)

	return(filename[0]+"_features.wav")


	