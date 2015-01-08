import pyttsx
import time

engine = pyttsx.init()
voices = engine.getProperty('voices')
gender = ['male', 'female', 'neutral']
for voice in voices:
	for gen in gender:
		engine.setProperty('voice', voice.id)
		engine.setProperty('gender', gen)
		engine.say('The quick brown fox jumped over the lazy dog.')
		time.sleep(1)
engine.runAndWait()