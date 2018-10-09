from pydub import AudioSegment

def speed_change(sound,speed,path,filename):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })
    filename=filename.split(".")
    slow_sound=sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)
    print(path+"/"+filename[0]+"_slow"+"."+filename[1])
    slow_sound.export(path+"/"+filename[0]+"_slow"+"."+filename[1],format="wav")

def input_pathaudio(audiopath,filename):
    sound=AudioSegment.from_file(audiopath+"/"+filename)
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * 0.50)
    })
    speed_change(sound,0.50,audiopath,filename)