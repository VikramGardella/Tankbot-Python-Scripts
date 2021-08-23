from gtts import gTTS
import os

inp = ' '

language = 'en'

while(True):
    inp = raw_input()
    obj = gTTS(text = inp, lang = language, slow = False)
    obj.save('output.mp3')
    os.system('mpg321 output.mp3')
