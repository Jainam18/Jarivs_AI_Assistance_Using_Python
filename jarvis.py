import webbrowser
import pyttsx3
import speech_recognition as sr
from datetime import datetime
import wikipedia
import pyaudio
import os
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
        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("google.com")
        elif "open youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
        elif "open github" in query:
            speak("Opening Github")
            webbrowser.open("github.com")
        # elif "open" in query:
        #     query = query.replace("open","")
        #     try:
        #         webbrowser.open(f"{query}.com")
        #     except Exception as e:
        #         speak("No Such Website Found")
        elif "play music" in query:
            location = "E:\Programming languages\Web Development\Projects\Spotify Clone\Songs"
            songs = os.listdir(location)
            print(songs)
            os.startfile(os.path.join(location,songs[0]))
        elif "play my favourite songs" in query:
            webbrowser.open("https://open.spotify.com/playlist/4mN3ib45YfUfl9jIB2EQMp")
        elif "play new songs" in  query:
            webbrowser.open("https://open.spotify.com/playlist/5P7H6AJYhsOr2xCbXbV7zg")