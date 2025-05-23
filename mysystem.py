import speech_recognition as sr
import pyttsx3
import subprocess
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
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
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, I couldn't reach the speech recognition service.")
        return ""

def open_application(command):
    if "vs code" in command or "visual studio code" in command:
        speak("Opening Visual Studio Code")
        subprocess.Popen(["code"])  # VS Code must be in PATH
    elif "notepad" in command:
        speak("Opening Notepad")
        subprocess.Popen(["notepad.exe"])
    elif "chrome" in command:
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        if os.path.exists(chrome_path):
            speak("Opening Google Chrome")
            subprocess.Popen([chrome_path])
        else:
            speak("Chrome path not found.")
    elif "image" in command and "downloads" in command:
        folder = os.path.join(os.path.expanduser("~"), "Downloads")
        images = [f for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        if images:
            speak("Opening image from Downloads")
            os.startfile(os.path.join(folder, images[0]))
        else:
            speak("No image found in Downloads.")
    elif "resume" in command and "documents" in command:
        folder = os.path.join(os.path.expanduser("~"), "Documents")
        files = [f for f in os.listdir(folder) if "resume" in f.lower()]
        if files:
            speak(f"Opening {files[0]} from Documents")
            os.startfile(os.path.join(folder, files[0]))
        else:
            speak("No resume found in Documents.")
    else:
        speak("Sorry, I don't recognize that application or file yet.")

# Main loop
if __name__ == "__main__":
    speak("Voice Assistant Initialized. Say a command.")
    while True:
        command = listen()
        if command:
            if "exit" in command or "stop" in command:
                speak("Goodbye!")
                break
            open_application(command)
