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


def run():
    cd=speech()
    if 'mouse' in cd:
        return videoon()
    
def run2():
    cd=speech()
    if 'youtube' in cd:
        return youtube()

def run3():
    cd=speech()
    if 'spotify' in cd:
        return spotify()

def run4():
    cd=speech()
    if 'image converter' in cd:
        return markuphero()

def run5():
    cd=speech()
    if 'eyecam' in cd:
        return eyecamon()

def run6():
    cd=speech()
    if 'time ' in cd:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)



while True:
    cd=speech()
    if 'mouse' in cd:
        run()

    if 'time' in cd:
        run6()

    if 'eyecam' in cd:
        run5()

    if 'image converter' in cd:
        run4()

        

        
    




