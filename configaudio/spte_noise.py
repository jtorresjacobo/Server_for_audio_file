import os


#audiooriginal="vozdemujer.wav"
#noise="cut_ALONZOMONGOL_features_0.wav"


def audioclean(paths,name,fil):
	#Obteniendo la muestra de ruido

	os.system("ffmpeg -i "+paths+"/"+fil+" -vn -ss 00:00:03 -t 00:00:11 "+paths+"/"+"_12"+fil)

	os.system("sox "+paths+"/"+"_12"+fil+" -n trim 0 0.5 noiseprof " +paths+"/noise.prof")


	#comparando y extrayendo el audio sin fondo
	os.system("sox  "+paths+"/"+name+ " "+paths +"/_limpio"+name +" noisered "+ paths+"/noise.prof 0.41 silence -l 1 0.3 5% -1 2.0 5%")



