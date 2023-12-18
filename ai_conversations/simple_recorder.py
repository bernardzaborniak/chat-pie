import pyaudio
import wave
import numpy as np
import audioop


def record_audio(file_name, duration=3, sample_rate=44100, channels=1):
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


    frames = []
    for i in range(0, int(sample_rate / frames_per_buffer * duration)):
        data = stream.read(frames_per_buffer)
        frames.append(data)

         # Convert the byte data to NumPy array
        #audio_data = np.frombuffer(data, dtype=np.int16)

        rms = audioop.rms(data, 2)    # here's where you calculate the volume

        # Display the volume level
        #print(f"Volume: {rms:.2f}", end='\r')
        print(f"Volume: {rms:.2f}")

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
        wf.writeframes(b''.join(frames))

    print(f"Audio saved to {file_name}")

if __name__ == "__main__":
    # Set the file name and recording duration
    output_file = "recorded_audio.wav"
    recording_duration = 12
    volume_threshold = 1500

    # Start recording
    record_audio(output_file, duration=recording_duration)