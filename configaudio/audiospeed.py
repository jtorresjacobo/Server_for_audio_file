from pydub import AudioSegment
import controller

def speed_change(sound,speed,path,filename,user):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    filename=filename.split(".")
    destino=path+"/"+filename[0]+"_slow"+"."+filename[1]    
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })

    slow_sound=sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)
    slow_sound.export(destino,format="wav")

    ###ingresando a bd
    controller.main(destino,user)


def input_pathaudio(audiopath,filename,user):
    sound=AudioSegment.from_file(audiopath+"/"+filename)
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * 0.50)
    })
    speed_change(sound,0.50,audiopath,filename,user)