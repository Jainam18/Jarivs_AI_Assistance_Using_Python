import webbrowser
import pyttsx3
import speech_recognition as sr
from datetime import datetime
import wikipedia
import pyaudio
import os
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    '''This Function takes message as parameter and output the voice audio in return'''
    engine.say(audio)
    engine.runAndWait()

def wish():
    '''This Function wishes the user according to the currect timeframe and introduces the assistance'''
    dt = datetime.now()
    hour = dt.hour
    if hour>=5 and hour<12:
        speak("Good Morning Jainam!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Jainam!")
    else:
        speak("Good Evening Jainam!")

    speak("I am Jarvis, Please tell me How may I help you ?")

def take_command():
    '''This Function takes the Command from the User by Recognizing the Speech'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    query = ''
    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
        print(f"User Said : {query}\n")
    except Exception as e:
        # print(e)    As this will generate an error in terminal
        print("Please Say that Again!...")
        return "None"
    return query
if __name__ == "__main__" :
    # speak("Hello Jainam, You are making an awesome Project.")
    wish()
    while(True):
        query = take_command().lower()
        # print(query)
        if "wikipedia" in query:
            speak("Searching for the Text in Wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to the Wikipedia")
            speak(results)
            print(results)
        elif "how are you" in query:
            speak("Im Fine, Thank You Jainam For Being Concerned.")
        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("google.com")
        elif "open youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
        elif "open github" in query:
            speak("Opening Github")
            webbrowser.open("github.com")
        elif "play music" in query:
            speak("Playing the Songs")
            location = "E:\Programming languages\Web Development\Projects\Spotify Clone\Songs"
            songs = os.listdir(location)
            print(songs)
            os.startfile(os.path.join(location,songs[0]))
        elif "play my favourite songs" in query:
            speak("Opening your favourite Spotify Playist")
            webbrowser.open("https://open.spotify.com/playlist/4mN3ib45YfUfl9jIB2EQMp")
        elif "play new songs" in  query:
            speak("Opening New Songs From Spotify PLaylist")
            webbrowser.open("https://open.spotify.com/playlist/5P7H6AJYhsOr2xCbXbV7zg")
        elif "check mails" in query:
            speak("Open Your Gmail")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        elif "time" in query:
            dt = datetime.now()
            time = dt.strftime("%H:%M:%S")
            speak(f"The time right now is {time}")
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif "shutdown your program" in query:
            speak("Ok, Jainam Shutting Down My System.")
            exit()