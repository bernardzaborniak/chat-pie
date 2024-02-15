import pyaudio
import wave
import numpy as np
import audioop
from datetime import datetime



def record_audio(file_name, volume_threshold=1500, silence_duration = 5, sample_rate=44100, channels=1):
    p = pyaudio.PyAudio()

    # Set the recording parameters
    format = pyaudio.paInt16
    frames_per_buffer = 1024

    # Open the audio stream
    stream = p.open(format=format,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=frames_per_buffer)

    print("Recording...")

    silence_passed = False
    silence_started_time = datetime.now()
    current_silence_time = 0
    starded_recording_after_reaching_threshold = False

    record_frames = []
    non_record_frames = []
    while(not silence_passed):
        data = stream.read(frames_per_buffer)

        non_record_frames.append(data)

        if(len(non_record_frames)>30): 
            rms = audioop.rms(data, 2)    # here's where you calculate the volume

            if(not starded_recording_after_reaching_threshold):
                print(f"Volume: {rms:.2f}", end='\r')

                if(rms > volume_threshold*3):
                    starded_recording_after_reaching_threshold = True

            if(starded_recording_after_reaching_threshold):
                record_frames.append(data)

                if(rms > volume_threshold):
                    silence_started_time = datetime.now()
                    current_silence_time = 0
                    print(f"Volume: {rms:.2f}", end='\r')

                else: 
                    current_silence_time = (datetime.now()-silence_started_time).total_seconds()
                    print(f"Volume: {rms:.2f}",f"current_silence_time: {current_silence_time}", end='\r')

                if(current_silence_time > silence_duration):
                    silence_passed = True

    print("Recording finished.")

    # Stop and close the audio stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded audio to a WAV file
    with wave.open(file_name, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(format))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(record_frames))

    
    print(f"Audio saved to {file_name}")

    return 

if __name__ == "__main__":
    # Set the file name and recording duration
    recording_duration = 10
    output_file = "recorded_audio.wav"
    volume_threshold = 1500
    silence_duration = 5

    # Start recording
    record_audio(output_file, volume_threshold=volume_threshold, silence_duration = silence_duration)