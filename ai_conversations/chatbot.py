from datetime import datetime
import os
import threading
import time
import speech_recognition as sr
from openai import OpenAI
from gtts import gTTS
import dynamic_recorder as dynamic_recorder

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

#accent could be
    #'com.au'
    #'co.uk'
    #'us'
    #'ca'
    #'co.in'
    #'ie
    #'co.za

class Chatbot:
   
    def __init__(self, is_initiator, chat_character_prompt, accent):
        # Decides whether this chatbot starts a conversation first
        self.is_initiator = is_initiator
        # This prompt is used to shape the character of the chatbot
        self.chat_character_prompt = chat_character_prompt
        self.chat_history = []
        self.waiting_for_chat_gpt = False
        self.chat_gpt_response = ""
        self.chat_history = []
        self.accent = accent


    def play_text(self, text):
        print("answer: " + text)
        # tts = gTTS(text, lang="en", tld=self.accent)
        tts = gTTS(text, lang="en", tld="com")
        tts.save("response.mp3")
        os.system("vlc response.mp3 --play-and-exit")


    def get_chat_gpt_response_threaded(self, input_text):
        self.chat_history.append({"role": "user", "content": input_text})
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=self.chat_history
            #model="gpt-4", messages=self.chat_history
        )
        self.chat_gpt_response = response.choices[0].message.content
        self.chat_history.append({"role": "assistant", "content": self.chat_gpt_response})
        self.waiting_for_chat_gpt = False
        print("chat gpt finished: " + self.chat_gpt_response)


    def main(self):
        self.waiting_for_chat_gpt = True
        print('set up prompt is: ' + self.chat_character_prompt)
        threading.Thread(target=self.get_chat_gpt_response_threaded(self.chat_character_prompt)).start()

        print("initiating first prompt")
        print("waiting_for_chat_gpt")
        while self.waiting_for_chat_gpt:
            time.sleep(1)
            print("waiting for chat gpt... this can take some time...")
        
        if self.is_initiator:
            self.play_text(self.chat_gpt_response)
        else:
            print(self.chat_gpt_response)

        r = sr.Recognizer()

        from os import path
        AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "recorded_audio.wav")

        while True:
            print("listening startet")

            output_file = "ai_conversations/recorded_audio.wav"
            volume_threshold = 700 #if the volume gets over this value, we start recording
            silence_duration = 1.5 #if we stopped talking for this amount of seconds we stope recording
            dynamic_recorder.record_audio(output_file, volume_threshold=volume_threshold, silence_duration = silence_duration)          

            with sr.AudioFile(AUDIO_FILE) as source:
                audio = r.record(source)  # read the entire audio file

            # convert audio to text
            try:
                input_text = r.recognize_whisper(audio, language = 'en')
                #input_text = r.recognize_google(audio, language = 'en')
                print("recognized audio: " + input_text)

                if input_text == '' or input_text == "Thank you.":
                    continue

            except sr.UnknownValueError:
                print("listening not understood")
                self.play_text('I could not understand could you repeat that?')

                continue
            except sr.RequestError as e:
                print(  "Could not request results from Google Speech Recognition service; {0}".format( e ))
                continue

            self.waiting_for_chat_gpt = True
            threading.Thread(target=self.get_chat_gpt_response_threaded(input_text)).start()

            print("chat gpt time")
            print(self.waiting_for_chat_gpt)
            while self.waiting_for_chat_gpt:
                time.sleep(1)
                print("waiting for chat gpt... this can take some time...")

            self.play_text(self.chat_gpt_response)
