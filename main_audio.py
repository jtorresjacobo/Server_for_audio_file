import sys
sys.path.insert(0, sys.path[0]+'/configaudio/')
import convert_wav_with_features,noise_s,cut,audiospeed,mysql_python
import Extraccion_Fondo
from werkzeug.utils import secure_filename
import os
import spte_noise

def audio(file,paths,filenames):
      

	file.save(os.path.join(paths,filenames))

	#convert to format wav with features 
	#"name " is the name of audio file 
	name=convert_wav_with_features.audio(paths,filenames)

	#modify audio speed to 0.5
	audiospeed.input_pathaudio(paths,name)

	#separating audio every 30 seconds
	cut.separate_audio(paths,name)



	#entering audio file to database
	mysql_python.input(paths+"/"+name,file)

	#noise
	noise_s.path(paths,name)

	fil=Extraccion_Fondo.Extrac_Sonido(paths,filenames)

	spte_noise.audioclean(paths,name,fil)
