import wave


def wave_file_read_samples(filename):
    expected_n_channels = 1  # mono
    expected_sample_width = 2
    expected_framerate = 44100

    wr = wave.open(filename, mode="rb")
    if wr.getnchannels() != expected_n_channels:
        print("Error: utiliser un fichier mono")
        return None

    if wr.getframerate() != expected_framerate:
        print("Error: utiliser 44100Hz")
        return None

    if wr.getsampwidth() != expected_sample_width:
        print("Error: utiliser le format 16bits")
        return None
    nframes = wr.getnframes()
    print(nframes)
    frames_as_bytes = wr.readframes(nframes)

    wr.close()
    return frames_as_bytes