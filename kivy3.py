# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 22:03:56 2021

@author: maria
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 21:12:30 2021
@author: madeleinejenkins
"""

import kivy 
  
kivy.require("1.9.1") 

from kivy.app import App 
from kivy.uix.button import Button 
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
import pywhatkit as kit
import datetime
import geocoder
now = datetime.datetime.now()
g = geocoder.ip('me')
import speech_recognition as sr
import webbrowser as wb 

class ButtonApp(App): 
    contact_number1 = "+447578477987"
	contact_number2 = "+447578477987"
    awaken_word = "hello"  
	trigger1 = "jam"
	trigger2 = "peanut"
    def build(self): 
        layout = FloatLayout()
        btn = Button(text ="Push Me !", 
                   font_size ="20sp", 
                   background_color =(0.7, 1, 1, 1), 
                   color =(0, 1, 1, 1), 
                   size =(32, 32), 
                   size_hint =(.2, .2), 
                   pos =(300, 500))        
        btn.bind(on_press = self.callback) 
        layout.add_widget(btn)
    
    
        btn2 = Button(text ="Settings", 
                   font_size ="20sp", 
                   background_color =(0.7, 1, 1, 1), 
                   color =(0, 1, 1, 1), 
                   size =(32, 5), 
                   size_hint =(.2, .2), 
                   pos =(300, 20))
        btn2.bind(on_press = self.settings) 
        layout.add_widget(btn2)     
        img = Image(source='breaking_wave-1920x1200.jpg',
                    size_hint=(0.6, 0.6),
                    pos=(200,100))
        layout.add_widget(img)
        return layout

    def settings(self, event):
        print("type in contact number 1: ")
        self.contact_number1 = input()
        print("type in contact number 2: ")
        self.contact_number2 = input()

        print("type in awaken word:")
        self.awaken_word = input()

        print("contact 1 trigger word:")
        self.trigger1 = input()
        print("contact 2 trigger word:")
        self.trigger2 = input()
  
    def callback(self, event): 
        r1 = sr.Recognizer()
        r2 = sr.Recognizer()
        with sr.Microphone() as source:
             print('[hi]')
             print('speak now')
             audio = r1.listen(source)    
        if self.awaken_word in r2.recognize_google(audio):
            r2 = sr.Recognizer()
            print("speak again")
            with sr.Microphone() as source:        
                audio = r2.listen(source)
                if self.trigger1 in r2.recognize_google(audio):
                    kit.sendwhatmsg(self.contact_number1, "hi I am scared. my location is: "+str(g.latlng), now.hour, now.minute +2)
                elif self.trigger2 in r2.recognize_google(audio):
                    kit.sendwhatmsg(self.contact_number2, "hi I am scared. my location is: "+str(g.latlng), now.hour, now.minute +2)

          
root = ButtonApp() 
root.run() 
