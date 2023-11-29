import os
# -- speech recognition 
import speech_recognition as sr
# -- chat gpt
import openai
openai.api_key='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'
# -- text to speech
from gtts import gTTS

def play_text(text):
    print("answer: " + text)
    tts = gTTS(text, lang='en')
    tts.save('response.mp3')
    os.system("vlc response.mp3 --play-and-exit")


while(True):
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        play_text('Say something!')
        audio = r.listen(source)
        print('listening finished')

    #convert audio to text
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        input_text = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said: " + input_text)

          # ask chat gpt for answer
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{input_text}"}])
        response_text = response.choices[0].message.content

        # convert answer to speech
        play_text(response_text)
  

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))



  
