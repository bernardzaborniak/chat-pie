from gtts import gTTS
import os
import speech_recognition as sr

from gtts import gTTS

tts = gTTS('oj mat, where my pint?', lang='en', tld='ie')
tts.save('hello.mp3')
os.system("vlc hello.mp3 --play-and-exit")

tts = gTTS('do not redeeem! Fuck you bloody', lang='en', tld='co.in')
tts.save('hello.mp3')
os.system("vlc hello.mp3 --play-and-exit")


tts = gTTS('Oj senor, necessitas mas pixelas?', lang='es')
tts.save('hello.mp3')
os.system("vlc hello.mp3 --play-and-exit")

tts = gTTS('hello there, i have the highground', lang='fr')
tts.save('hello.mp3')
os.system("vlc hello.mp3 --play-and-exit")

tts = gTTS('hello there, i have even more highground now', lang='zh-CN')
tts.save('hello.mp3')
os.system("vlc hello.mp3 --play-and-exit")

print('finito')