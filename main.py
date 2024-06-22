import pyttsx3 
import speech_recognition as sr 
import wikipedia
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)

def speak(text):
    """This function takes text and returns voice"""
    engine.say(text)
    engine.runAndWait()

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
        except sr.UnknownValueError:
            print("Could not understand the audio, please try again...")
            return "None"
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return "None"
        except Exception as e:
            print(f"Error occurred: {e}")
            return "None"
        return query

if __name__ == "__main__":
    
    query = takeCommand().lower()
    print(query)
    
    if "wikipedia" or "Wikipedia" in query:
        speak ("Searching Wikipedia")
        results = wikipedia.summary(query, sentences = 2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
        print(results)

