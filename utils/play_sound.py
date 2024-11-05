import sounddevice as sd
import soundfile as sf
import threading


def play_audio(file_path):
    data, sample_rate = sf.read(file_path)
    sd.play(data, sample_rate)
    sd.wait()


def play_audio_thread(file_path):
    threading.Thread(target=play_audio, args=(file_path,)).start()
