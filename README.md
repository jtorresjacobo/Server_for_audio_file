
Server_for_audio_file

Documentación


Funcionalidades:
.Convierte audios formatos (Mp3,ogg) a fomrato .WAV 
.Separa el audio en partes de 30 segundos
.Crea un audio con ruido
.Crea un audio con velocidad 0.5 a comparacion del audio original
.Almacena cada audio ingresado en la base de datos "Audios", la documentacion para poder crear la base de datos con sus tablas respectivas se detalla en el archivo "Instalacion y conecion bd"


Ejecución del proyecto Server_for_audio_file:
se ejecuta con el archivo server.py
el comando  se ejecuta en el terminal ,para poder ejecutar el proyecto es
>>> python server.py
> se dirige a la url en Mozila: 0.0.0.0:5000

Al ejecutar el comando en el terminal, se creara una carpeta "Audios" , donde se almacenará todos los audios mencionados en las "funcionalidades" del presente documento

Caracteristicas adicionales:
-El archivo .WAV que se crea , tiene las siguientes caracteristicas: 
.canales:mono
.Frecuencia:16000 Hz
.Tsa de bits: N/D



