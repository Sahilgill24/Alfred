import pyttsx3 as pt
from mouse import videoon
from eyecam import eyecamon
import speech_recognition as sr
import pyaudio
import datetime
from bots import youtube,spotify,markuphero
import pywhatkit




listner = sr.Recognizer()

def speech():
    try:
        with sr.Microphone() as source:
            print("alfred here , how may I help you ")
            voice = listner.listen(source)
            command=listner.recognize_google(voice)
            command=command.lower()
            if 'alfred' in command:
                print(command)

    except:
        pass
    return command


def talk(t):
    engine=pt.init()
    engine.say(t)
    engine.runAndWait()


def alfred():
    cd=speech()
    if 'mouse' in cd:
        videoon()
    elif 'time' in cd:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'eyecam' in cd:
        eyecamon()
    elif 'youtube' in cd:
        youtube()
    elif 'play' in cd:
        spotify()
    elif "image converter" in cd:
        markuphero()
    else:
        talk("pls say the command again ...... ")

while True:
    alfred()




