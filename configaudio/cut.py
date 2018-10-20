import os
from os import path
from pydub import AudioSegment
import soundfile as sf
import controller


def separate_audio(paths,filename):
	#tiempo total en segundos
	s_extension=path.split(".")

	name=filename.split(".")
	f = sf.SoundFile(paths+"/"+filename)
	#total duration time in seconds
	total=int(format(len(f) / f.samplerate))

	#amount od audio with parts of 30 seconds
	cant=total/30
	sobrante=total-cant*30

	sound=AudioSegment.from_wav(paths+"/"+filename)

	#total lenght od audio
	halfway_point=len(sound)

	first_half=sound[:30000]

	i=0
	j=0
	k=30000

	for i in range(0,cant):
		audio=sound[j:k]
		destino=paths+"/"+"cut_"+name[0]+"_"+str(i)
		audio.export(destino,format="wav")
		
		#ingreso a bd
		controller.main(destino)

		j=j+30000
		k=k+30000
		i=i+1

		#cut the last part of audio
		if i==cant and sobrante!=0:
			k=k+30000
			audio=sound[j:halfway_point]
			destino=paths+"/"+"cut_"+name[0]+"_"+str(i)
			audio.export(destino,format="wav")

			#ingreso a bd
			controller.main(destino)
