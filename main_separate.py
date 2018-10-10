import spte_noise
from pydub import AudioSegment
from pydub.playback import play

audiooriginal="vozdemujer.wav"
noise="cut_ALONZOMONGOL_features_0.wav"



spte_noise.audioclean(noise,audiooriginal)