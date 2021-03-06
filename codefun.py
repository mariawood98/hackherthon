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
import pywhatkit as kit
import datetime

now = datetime.datetime.now()

import speech_recognition as sr
import webbrowser as wb 

class ButtonApp(App): 
      
    def build(self): 
        btn = Button(text ="Push Me !", 
                   font_size ="20sp", 
                   background_color =(1, 1, 1, 1), 
                   color =(1, 1, 1, 1), 
                   size =(32, 32), 
                   size_hint =(.2, .2), 
                   pos =(300, 250)) 

        btn.bind(on_press = self.callback) 
        return btn
  
    def callback(self, event): 
        r1 = sr.Recognizer()

        r2 = sr.Recognizer()

        with sr.Microphone() as source:
             print('[hi]')
             print('speak now')
             audio = r1.listen(source)    
        if 'hello' in r2.recognize_google(audio):
            r2 = sr.Recognizer()



            kit.sendwhatmsg("+447578477987", "hey sexy", now.hour, now.minute +2)



          
root = ButtonApp() 

root.run() 



