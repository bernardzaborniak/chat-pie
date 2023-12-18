# run for x (aybe 6) seconds and tell the average the high and the low of the environment

import pyaudio
import wave
import numpy as np
import audioop
from datetime import datetime
import statistics


duration = 6


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


volumes = []
for i in range(0, int(sample_rate / frames_per_buffer * duration)):
    data = stream.read(frames_per_buffer)
    rms = audioop.rms(data, 2)    # here's where you calculate the volume
    volumes.append(rms)
    print(f"Number: {i*sample_rate}", end='\r')

    #print(f"Volume: {rms:.2f}")

print(f"average volume: {sum(volumes) / len(volumes)}")
print(f"median volume: {statistics.median(volumes)}")
print(f"maximum volume: {max(volumes)}")
print(f"minimum volume: {min(volumes)}")
