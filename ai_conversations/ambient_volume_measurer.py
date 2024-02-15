# run for x (aybe 6) seconds and tell the average the high and the low of the environment

import pyaudio
import wave
import numpy as np
import audioop
from datetime import datetime
import statistics


duration = 6

file_name = "ambient_volume_measurer_recording.wav"

p = pyaudio.PyAudio()

# Set the recording parameters
format = pyaudio.paInt16
frames_per_buffer = 1024
sample_rate=44100
channels=1

# Open the audio stream
stream = p.open(format=format,
    channels=channels,
    rate=sample_rate,
    input=True,
    frames_per_buffer=frames_per_buffer)

print("Measuring...")

#ignore the first 0.5 seconds

volumes = []
frames = []
for i in range(0, int(sample_rate / frames_per_buffer * duration)):
    data = stream.read(frames_per_buffer)
    frames.append(data)

    # some laptops have a piep at the beginning of every recording,thats a little too loud 
    # theats why we start recording a little later
    #if(i*(sample_rate / frames_per_buffer)>1000): 
    if(len(frames)>30): 
        rms = audioop.rms(data, 2)    # here's where you calculate the volume
        print(f"Volume: {rms:.2f}")
        volumes.append(rms)

    #print(f"Number: {i*(sample_rate / frames_per_buffer)}", end='\r')


print(f"average volume: {sum(volumes) / len(volumes)}")
print(f"median volume: {statistics.median(volumes)}")
print(f"maximum volume: {max(volumes)}")
print(f"minimum volume: {min(volumes)}")

# Stop and close the audio stream
stream.stop_stream()
stream.close()
p.terminate()

    # Save the recorded audio to a WAV file
with wave.open(file_name, 'wb') as wf:
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))

    
print(f"Audio saved to {file_name}")
