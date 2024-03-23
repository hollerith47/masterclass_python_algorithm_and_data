from wave_file_manager import *

wav_samples = wave_file_read_samples("./data_audio/test1.wav")
if wav_samples is None:
    print("Erreur")
    exit(0)
