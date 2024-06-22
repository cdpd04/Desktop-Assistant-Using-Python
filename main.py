import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import os

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)  # Use the first voice in the list
engine.setProperty('rate', 150)  # Set the speed of the voice


# Function to convert text to speech
def speak(text):
    """This function takes text and returns voice

    Args:
        text (str): string to be spoken
    """
    engine.say(text)
    engine.runAndWait()


# Function to recognize voice and convert it to text
def takeCommand():
    """This function will recognize voice & return text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query

def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Assistant. Tell me How can I help you")
    
if __name__ == "__main__":
    wish_me()
    while True:
        query = takeCommand().lower()  # Convert the query to lowercase for uniformity
        print(query)
    
        if "wikipedia" in query:
            speak("Searching Wikipedia")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
           
        if "stop" in query:
            break