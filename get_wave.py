import pyaudio
import wave

def record_audio(format=pyaudio.paInt16, channels=1, rate=44100, duration):
    p = pyaudio.PyAudio()
    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=1024)
    
    frames = []
    # loop for the duration of the recording
    for i in range(0, int(rate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open("output.wav", "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b"".join(frames))
    wf.close()
    
    return "output.wav"
