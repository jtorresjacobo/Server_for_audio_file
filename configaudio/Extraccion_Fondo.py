from pydub import AudioSegment
from pydub.playback import play
import controller

#RUTA DE EL ARCHIVO A MODIFICAR
#link='/home/diego/Escritorio/quechua.mp3'

#FUNCION PARA EJECUTAR EL CAMBIO DE EXTRACCION DE SONIDO

def Extrac_Sonido(paths,filename,user):

# read in audio file and get the two mono tracks
	sound_stereo = AudioSegment.from_file(paths+"/"+filename, format="mp3")

	sound_monoL = sound_stereo.split_to_mono()[0]

	sound_monoR = sound_stereo.split_to_mono()[1]

# Invert phase of the Right audio file
	sound_monoR_inv = sound_monoR.invert_phase()

# Merge two L and R_inv files, this cancels out the centers
	sound_CentersOut = sound_monoL.overlay(sound_monoR_inv)

# EXPORTACION DEL DOCUMENTO
	destino=paths+"/"+filename[0]+"fondo.wav"
	sound_CentersOut.export(destino, format="wav")

	#ingreso a bd
	controller.main(destino,user)


	fil=filename[0]+"fondo.wav"

	return fil