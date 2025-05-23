import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening for your command...")
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, I couldn't reach the speech recognition service.")
        return ""

def open_website(command):
    if "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "twitter" in command:
        speak("Opening Twitter")
        webbrowser.open("https://www.twitter.com")
    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")
    else:
        speak("I can only open Google, Twitter, YouTube, or GitHub for now.")

if __name__ == "__main__":
    while True:
        command = listen()
        if command:
            if "exit" in command or "stop" in command:
                speak("Goodbye!")
                break
            open_website(command)
