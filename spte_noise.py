import os


#audiooriginal="vozdemujer.wav"
#noise="cut_ALONZOMONGOL_features_0.wav"


def audioclean(noise,audiooriginal):
	#Obteniendo la muestra de ruido
	os.system("sox "+noise+" -n noiseprof noise.prof")

	#comparando y extrayendo el audio sin fondo
	os.system("sox  "+audiooriginal+" sinfondo.wav noisered noise.prof 0.41")


