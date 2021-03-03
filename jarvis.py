import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import os

MASTER = "Daan"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak(f"Good morning {MASTER}")

    if hour>=12 and hour<18:
        speak(f"Good afternoon {MASTER}")

    else:
        speak(f"Good evening {MASTER}")

    speak("I'm Jarvis. Please tell me how i can help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return query

wishMe()
query = takeCommand().lower()

if 'wikipedia' in query.lower():
    speak("Initializing Jarvis...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)

elif 'open google' in query.lower():
    speak("Opening google")
    url = "google.com"
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open youtube' in query.lower():
    speak("Opening youtube")
    url = "youtube.com"
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)