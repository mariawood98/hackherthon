import speech_recognition as sr
import webbrowser as wb
import pywhatkit
import datetime
r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()
now = datetime.datetime.now()
print("type in contact number: ")
contact_number = input()
with sr.Microphone() as source:
    print("speak now")
    audio = r3.listen(source)

if 'hello' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    if 'maddie' in r2.recognize_google(audio):
        pywhatkit.sendwhatmsg("contact_number", "hi", now.hour, now.minute+2)
    elif 'cathy' in r2.recognize_google(audio):
        pywhatkit.sendwhatmsg("+contact_number", "hi", now.hour, now.minute+2)