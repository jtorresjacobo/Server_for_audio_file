import os
import controller
import utils as u

def audio(path,filename,user):
	#audio fomat wav
	file=filename

	#audio file name's
	filename=filename.split(".")
	os.system("ffmpeg -i '"+path+"/"+file+"' -acodec pcm_s16le -ac 1 -ar 16000 '"+path+"/"+filename[0]+"_features.wav"+"'")
	#os.system("rm '"+path+archivo+"'")
	destino=path+"/"+filename[0]+"_features.wav"

	#duracion del audio
	duracion=u.audio_duration(destino)


	#ingreso a bd
	controller.main(destino,user)

	return(filename[0]+"_features.wav")


	