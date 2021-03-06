import speech_recognition as sr
import webbrowser as wb
import pywhatkit
import datetime
r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()
now = datetime.datetime.now()

print("type in contact number 1: ")
contact_number1 = input()
print("type in contact number 2: ")
contact_number2 = input()

print("type in awaken word:")
awaken_word = input()

print("contact 1 trigger word:")
trigger1 = input()
print("contact 2 trigger word:")
trigger2 = input()

with sr.Microphone() as source:
    print("speak now")
    audio = r3.listen(source)

if awaken_word in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    print("speak now")
    with sr.Microphone() as source:        
        audio = r2.listen(source)   
        if trigger1 in r2.recognize_google(audio):
            pywhatkit.sendwhatmsg(contact_number1, "hi", now.hour, now.minute+2)
        elif trigger2 in r2.recognize_google(audio):
            pywhatkit.sendwhatmsg(contact_number2, "hi", now.hour, now.minute+2)