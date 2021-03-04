import datetime
import os
import smtplib
import ssl
import webbrowser

import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia

MASTER = "Daan"

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "daanvo.coding@gmail.com"
password = "Your Password"

# Create a secure SSL context
context = ssl.create_default_context()

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
    speak("Opening Google")
    url = "google.com"
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open youtube' in query.lower():
    speak("Opening Youtube")
    url = "youtube.com"
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'play something on youtube' in query.lower():
    print("What do you want to see?")
    speak("What do you want to see?")
    query = takeCommand()
    pywhatkit.playonyt(query)

elif 'open the weather' in query.lower():
    speak("Opening the weather")
    url = "https://www.google.com/search?q=weather&oq=weather&aqs=chrome..69i57j0j0i131i433l2j0l2j46j46i131i433j0j0i131i433.1564j0j7&sourceid=chrome&ie=UTF-8"
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open the news' in query.lower():
    speak("Opening the news")
    url = "https://news.google.com/topstories?hl=nl&gl=NL&ceid=NL:nl"
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'play music' in query.lower():
    speak("Opening the music")
    songs_dir = "music"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0]))

elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    print(strTime)
    speak(f"{MASTER} the time is {strTime}")

elif 'email to my dad' in query.lower():
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        print("What should i send")
        speak("What should i send")
        query = takeCommand()
        server.sendmail("Your Email", "Dad Email", query)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()

elif 'email to my mum' in query.lower():
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        print("What should i send")
        speak("What should i send")
        query = takeCommand()
        server.sendmail("Your Email", "Mum Email", query)
        print("Email successfully send")
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()


