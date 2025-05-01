import speech_recognition as sr
import json


r = sr.Recognizer()
with sr.Microphone() as source:
    print('listening...')
    audio = r.listen(source, timeout=10, phrase_time_limit=60)
    print("......")

try:
    text = r.recognize_vosk(audio, language='ko')
    text = json.loads(text)['text']
    print("[Vosk]", text)

except sr.UnknownValueError:
    print("Recognizer Failed..")

except sr.RequestError as e:
    print("Request Failed...", e)