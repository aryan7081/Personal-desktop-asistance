import pyttsx3 
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import time
import datetime as dt
import os
import random


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening....')

        r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')
            print(Query)

        except Exception as e:
            print(e)
            print("Say that again please")
            # speak("Sorry...  Say that again please")
            return "None"

        return Query

    takeCommand()
 

def speak(audio):

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    engine.setProperty('voice',voices[0].id)
    engine.say(audio)
    engine.runAndWait()
 


def tellTime():
    
    tim = time.strftime("%H:%M")
    print(tim)
    speak("The time is")
    speak(tim)

def playmusic():
    n = random.randint(0,43)
    music_dir = "E:\songs"

    songs = os.listdir(music_dir)
    print(len(songs))

    os.startfile(os.path.join(music_dir,songs[n]))

   



def wishme():
    hour = dt.datetime.today().hour
    if hour>=4 and hour<12:
        speak("Good Morning Sir... Please tell me how may i help you")

    elif hour>=12 and hour<16: 
        speak(" Good Afternoon sir... Please tell me how may i help you") 
    
    elif hour>=16 and hour<22:
        speak("Good Evening sir... Please tell me how may i help you")

    elif hour>=22 and hour<4:
        
        speak("Good Night sir....It's time to sleep........but if u have any query... Please tell me how may i help you")


def Take_query():

    wishme()
    
    while(True):
        query = takeCommand().lower()
        if "open google" in query:
            speak("Opening google")
            webbrowser.open("www.google.com")
            continue


        if "open youtube" in query:
            speak("Opening youtube")
            webbrowser.open("www.youtube.com")
            continue

        elif "which day it is" in query:
            day = time.strftime('%A')
            print(day)
            speak("The day is")
            speak(day)
            continue

        elif "tell me the time" in query:
            tellTime()
            continue

        elif "bye" in query:
            speak("Bye.")
            exit()

        elif "wikipedia" in query:
            try:
                speak("searching for wikipedia")
                query = query.replace("wikipedia","") 

                result = wikipedia.summary(query,sentences=1)
                print(result)

                speak("According to wikipedia")
                speak(result)
                continue

            except Exception as e:
                print(e)
                speak("Not a valid command...Say in a valid manner")
                
                # return query
                continue
            return query

        elif "tell me your name" in query:
            speak("I am Jarvis. Your desktop Assistance")
 
        elif "play music" in query:

            n = random.randint(0,43)

            music_dir = "E:\songs"

            songs = os.listdir(music_dir)
            speak("Playing music from your music directory")
            os.startfile(os.path.join(music_dir,songs[n]))
            


        

   
            


        

        elif "who is your creator" in query:
            speak("My creator's name is Aryan yadav")

        elif "introduce your creator" in query:
            speak("My creator aryan yadav is in 10th standard....Father...Mr. Suneel kumar yadav....Mother..Mrs Seema Devi..And Brother... Mr. Anurag yadav")
            



Take_query()

