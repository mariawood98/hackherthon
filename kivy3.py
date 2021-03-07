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
##run the following on star-up in console:
#try:
#    from kivy.app import App
#except ImportError:
#    import pip._internal as pip
#    pip.main(['install', 'kivy'])
#    from kivy.app import App
#import kivy 
 
#import required modules
kivy.require("1.9.1") 
from kivy.app import App 
from kivy.uix.button import Button 
from kivy.uix.floatlayout import FloatLayout
import pywhatkit as kit
import datetime
import geocoder
import speech_recognition as sr
from kivy.core.window import Window

#get the time and the location
now = datetime.datetime.now()
g = geocoder.ip('me')

#make the kivy widget
class ButtonApp(App): 
  
    #initialise variables to default settings
    contact_number1 = "+447578477987"
    contact_number2 = "+447578477987"
    awaken_word = "hello"  
    trigger1 = "jam"
    trigger2 = "peanut"
    
    #build the buttons
    def build(self): 
        layout = FloatLayout(size=(375, 667))
        Window.clearcolor = (1, 1, 1, 1)
        
        #button 1 for beginning audio
        btn = Button(
                   background_normal = 'breaking_wave-1920x1200.jpg', 
                   color =(0, 1, 1, 1), 
                   size =(32, 32), 
                   size_hint =(.6, .6), 
                   pos =(150, 100))        
        btn.bind(on_press = self.callback) 
        layout.add_widget(btn)
        
        #button 2 for adjusting settings and changing variables
        btn2 = Button(text ="Settings", 
                   font_size ="20sp", 
                   background_color =(0.7, 1, 1, 1), 
                   color =(0, 1, 1, 1), 
                   size =(32, 5), 
                   size_hint =(.2, .1), 
                   pos =(300, 20))
        btn2.bind(on_press = self.settings) 
        layout.add_widget(btn2)     
        return layout

    #action when settings button pressed
    def settings(self, event):
        print("type in contact number 1: ")
        self.contact_number1 = input()
        print("type in contact number 2: ")
        self.contact_number2 = input()

        print("type in aactivation word:")
        self.awaken_word = input()

        print("contact 1 trigger word:")
        self.trigger1 = input()
        print("contact 2 trigger word:")
        self.trigger2 = input()
  
    #action when button 1 pushed
    def callback(self, event): 
        r1 = sr.Recognizer()
        r2 = sr.Recognizer()
        with sr.Microphone() as source:
             print('hi')
             print('speak now') #say the activation word
             audio = r1.listen(source)    
        if self.awaken_word in r2.recognize_google(audio):
            r2 = sr.Recognizer()
            print("speak again") #say the trigger word
            with sr.Microphone() as source:        
                audio = r2.listen(source)
                if self.trigger1 in r2.recognize_google(audio):
                    kit.sendwhatmsg(self.contact_number1, "hi my location is: "+str(g.latlng), now.hour, now.minute +2) #send whatsapp message to chosen contact with location
                elif self.trigger2 in r2.recognize_google(audio):
                    kit.sendwhatmsg(self.contact_number2, "hi my location is: "+str(g.latlng), now.hour, now.minute +2) #send whatsapp message to chosen contact with location
          
root = ButtonApp() 
#run the app
root.run() 
