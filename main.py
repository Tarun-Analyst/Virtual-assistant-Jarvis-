import speech_recognition as sr
import webbrowser 
import pyttsx3 
import musicLibrary

recognizer = sr.Recognizer() 
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c:
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in c:
        webbrowser.open("https://www.facebook.com")
    elif "open instagram" in c:
        webbrowser.open("https://www.instagram.com")
    elif "open linkedin" in c:
        webbrowser.open("https://www.linkedin.com")
    elif "open music" in c:
        webbrowser.open("https://www.youtube.com/watch?v=jCVjudmnByk")
    elif c.startswith("play"):
        try:
            song = c.split(" ", 1)[1].strip()
            link = musicLibrary.music.get(song)
            if link:
                speak(f"Playing {song}")
                webbrowser.open(link)
            else:
                speak("Sorry, I don't have that song.")
        except Exception as e:
            speak("Something went wrong while processing the song.")

if __name__ == "__main__":             
    speak("Initializing Jarvis...")

    while True:
        r = sr.Recognizer()
        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                try:
                    audio = r.listen(source, timeout=2, phrase_time_limit=2)
                except Exception as e:
                    print("Mic listen error:", e)
                    continue  # Skip this loop and try again

            if not audio:
                print("No audio captured.")
                continue

            try:
                word = r.recognize_google(audio)
                print("Heard:", word)
            except Exception as e:
                print("Speech recognition error:", e)
                word = ""

            if word.lower() == "jarvis":
                speak("Yes?")

                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    try:
                        audio = r.listen(source, timeout=4, phrase_time_limit=4)
                    except Exception as e:
                        print("Mic listen error:", e)
                        continue

                if not audio:
                    print("No command audio captured.")
                    continue

                try:
                    command = r.recognize_google(audio)
                    print("Command:", command)
                except Exception as e:
                    print("Speech recognition error:", e)
                    command = ""

                if command:
                    processCommand(command)
                else:
                    speak("Sorry, I didn't catch that.")

        except Exception as e:
            print("Error:", e)
