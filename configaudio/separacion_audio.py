from pydub import AudioSegment
from pydub.playback import play

file='/home/diego/Escritorio/Voz de Mujer.mp3'
load='leer.mp3'
# read in audio file and get the two mono tracks
sound_stereo = AudioSegment.from_file(file, format="mp3")
sound_monoL = sound_stereo.split_to_mono()[0]
sound_monoR = sound_stereo.split_to_mono()[1]

# Invert phase of the Right audio file
sound_monoR_inv = sound_monoR.invert_phase()

# Merge two L and R_inv files, this cancels out the centers
sound_CentersOut = sound_monoL.overlay(sound_monoR_inv)

# Export merged audio file
fh = sound_CentersOut.export(load, format="mp3")



