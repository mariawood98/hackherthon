# Hack-her-thongs: Flare App

The COVID-19 pandemic has increased incidence of domestic violence and potential for women to be trapped in uncomfortable/frightening/abusive situations. We have created an app which allows for inconspicuous contacting of friends, family or the police and asking for help in a way that is hidden from the aggressor. This is done by having the user interface masked as a calming meditation/photos app, and trigger words being typical everyday words used in conversation to not arouse suspicion. 

The app allows for the user to set an 'activation' word, 'trigger' words, and the numbers/contacts they would like to communicate with in Settings. When the image button is pressed, the app will start listening. If the activation word, such as 'weather' is heard, the app will wake up and listen further. If a specified trigger word is heard, such as 'sun', a message is sent via Whatsapp to an assigned contact for that trigger word, including the coordinates of the user. 

We have also built an alternative front-end HTML website design for the app. 

## kivy3.py
This python program uses Kivy to create an app with two buttons. 
The first, settings, allows the user to specify the contact numbers, activation word, trigger words, and message to send. This user input is typed into the IDE console.
The second button initiates the app to start listening to audio input to listen out for trigger words when pressed.
The ButtonApp() class creates the buttons and their functionality.

## webpage-test.html
This script opens in your browser and provides a front end solution to this app as a demo of what it will look like when we combine functionality with the kivy file. The webpage-setting.html is the second screen where you can input settings for the app.

## new_code 
A version of the kivy button which takes user input within the widget, rather than the interface. This is still in development, so does not have full functionality. 

## requirements.txt 
A list of packages required to run the code
