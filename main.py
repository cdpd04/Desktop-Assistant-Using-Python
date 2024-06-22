import pyttsx3
import speech_recognition as sr
import wikipedia


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


if __name__ == "__main__":
    query = takeCommand().lower()  # Convert the query to lowercase for uniformity
    print(query)
    
    if "wikipedia" in query:
        speak("Searching Wikipedia")
        try:
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        except Exception as e:
            speak("Sorry, I couldn't find anything on Wikipedia.")
            print("Error:", e)
