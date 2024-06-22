import pyttsx3
import speech_recognition as sr
import wikipedia

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

# Speak function
def speak(text):
    """This function takes text and returns voice

    Args:
        text (str): The text to be spoken
    """
    engine.say(text)
    engine.runAndWait()

# Speech recognition function
def takeCommand():
    """This function will recognize voice & return text

    Returns:
        str: Recognized text
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return "None"
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return "None"
        return query

if __name__ == "__main__":
    print("Main block is being executed")
    query = takeCommand().lower()
    print(f"Query: {query}")

    if "wikipedia" in query:
        speak("Searching Wikipedia")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=1)
        speak("According to Wikipedia")
        print(results)
        speak(results)
