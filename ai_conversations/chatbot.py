from datetime import datetime
import os
import threading
import time
import speech_recognition as sr
from openai import OpenAI
from gtts import gTTS

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
        tts = gTTS(text, lang="en", tld=self.accent)
        tts.save("response.mp3")
        os.system("vlc response.mp3 --play-and-exit")


    def get_chat_gpt_response_threaded(self, input_text):
        self.chat_history.append({"role": "user", "content": input_text})
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=self.chat_history
        )
        self.chat_gpt_response = response.choices[0].message.content
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

        while True:
            # obtain audio from the microphone
            #r = sr.Recognizer()

            with sr.Microphone() as source:
                print("listening startet")
                r.adjust_for_ambient_noise(source)
                counter = datetime.now()
                audio = r.listen(source)
                print(f"listening finished, listened for {datetime.now()-counter} seconds")

            # convert audio to text
            try:
                input_text = r.recognize_whisper(audio, language = 'en')
                print("recognized audio: " + input_text)

                if input_text == '':
                    continue

            except sr.UnknownValueError:
                #threading.Thread(   target=self.play_text("Sorry, I could not understand")).start()
                print("listening not understood")
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
