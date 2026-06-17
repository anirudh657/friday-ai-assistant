import ollama
import pywhatkit
import requests
import speech_recognition as sr
import time
import os
import webbrowser
import json
from datetime import datetime
import asyncio
import edge_tts
import pyautogui
from playsound import playsound


# ---------------- MEMORY ----------------
MEMORY_FILE = "memory.json"

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f)

memory = load_memory()



# ---------------- VOICE ----------------
def speak(text):

    print("FRIDAY:", text)

    async def speak_async():

        filename = f"voice_{int(time.time())}.mp3"

        communicate = edge_tts.Communicate(
            text=text,
            voice="en-US-AriaNeural"
        )

        await communicate.save(filename)

        playsound(filename)

        os.remove(filename)

    asyncio.run(speak_async())


speak("FRIDAY is now Activated")




# ---------------- AI ----------------
def ai_response(command):
    try:
        response = ollama.chat(
           model="gemma2:2b",
            messages=[
                {
                    "role": "system",
                    "content": "You are FRIDAY, Anirudh's personal AI assistant. Keep answers short and helpful."
                },
                {
                    "role": "user",
                    "content": command
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        print("AI ERROR:", e)
        return "My AI brain is currently unavailable."
    
def get_weather(city="Delhi"):

    try:

        url = f"https://wttr.in/{city}?format=j1"

        data = requests.get(url).json()

        temp = data["current_condition"][0]["temp_C"]
        desc = data["current_condition"][0]["weatherDesc"][0]["value"]

        return f"The weather in {city} is {desc} with temperature {temp} degrees Celsius"

    except:
        return "Unable to get weather information"    
    
    

# ---------------- SPEECH ----------------
r = sr.Recognizer()
def handle_complex_command(command):

    command = command.lower()

    # Open YouTube and play a song
    if "open youtube and play" in command:

        song = command.split("play")[-1].strip()

        speak(f"Opening YouTube and playing {song}")

        pywhatkit.playonyt(song)

        return True
    
    # Open Chrome and search
    if "open chrome and search" in command:

        query = command.split("search")[-1].strip()

        speak(f"Opening Chrome and searching {query}")

        webbrowser.open(
            f"https://www.google.com/search?q={query}"
    )

        return True
    
    # Open Spotify and play song
    if "open spotify and play" in command:

        song = command.split("play")[-1].strip()

        speak(f"Opening Spotify and playing {song}")

        webbrowser.open(
            f"https://open.spotify.com/search/{song}"
    )

        return True

    return False

# ---------------- INTENT ENGINE ----------------
def detect_intent(command):
    command = command.lower()

    if any(x in command for x in ["exit", "stop", "bye"]):
        return "exit"

    if "time" in command:
        return "time"

    if "search" in command:
        return "search"

    if "open" in command:
        return "open"

    if any(x in command for x in ["volume up", "louder", "increase volume"]):
        return "volume_up"

    if any(x in command for x in ["volume down", "lower volume", "decrease volume"]):
        return "volume_down"

    if "mute" in command:
        return "mute"
    
    if "remember" in command:
        return "remember"

    if "who am i" in command:
        return "profile"

    if "what is my name" in command:
        return "my_name"
    if "play" in command:
        return "play_song"
    
    if "weather" in command:
        return "weather"
    
    

    return "ai"

# ---------------- MAIN LOOP ----------------
while True:
        # MEMORY SAVE
            
    try:

        with sr.Microphone() as source:
            print("\nListening...")
            r.adjust_for_ambient_noise(source, duration=0.5)

            audio = r.listen(
                source,
                timeout=5,
                phrase_time_limit=7
            )

        text = r.recognize_google(audio)
        command = text.lower()

        if handle_complex_command(command):
           continue

        print("You said:", text)

        intent = detect_intent(command)
        if intent in ["open", "search", "play_song"]:
           speak("Yes boss")
    

        # EXIT
        if intent == "exit":
            speak("Shutting down FRIDAY")
            break

        # TIME
        elif intent == "time":
            now = datetime.now().strftime("%I:%M %p")
            speak(f"It is {now}")

        # SEARCH
        elif intent == "search":
            query = command.replace("search", "")
            query = query.replace("for", "")
            query = query.strip()

            speak(f"Searching {query}")

            webbrowser.open(
                f"https://www.google.com/search?q={query}"
            )

        # OPEN APPS
        elif intent == "open":

            app = command.replace("open", "").strip()

            if "youtube" in app:
                webbrowser.open("https://youtube.com")
                speak("Opening YouTube")

            elif "google" in app:
                webbrowser.open("https://google.com")
                speak("Opening Google")

            elif "chrome" in app:
                os.system("start chrome")
                speak("Opening Chrome")

            elif "whatsapp" in app:
                os.system("start whatsapp:")
                speak("Opening WhatsApp")

            elif "spotify" in app:
                os.system("start spotify:")
                speak("Opening Spotify")

            elif "notepad" in app:
                os.system("notepad")
                speak("Opening Notepad")

            elif "calculator" in app:
                os.system("calc")
                speak("Opening Calculator")

            else:
                speak(f"I cannot open {app}")
        # MEMORY
        # MEMORY SAVE
        elif intent == "remember":
            if "name is" in command:
                name = command.split("name is")[-1].strip()
                memory["name"] = name
                save_memory(memory)
                speak(f"I will remember that your name is {name}")
            else:
                speak("Please tell me what to remember, for example: remember my name is Alex")

        elif intent == "profile":
            if "name" in memory:
                speak(f"You are {memory['name']}")
            else:
                speak("I don't know who you are yet")

        elif intent == "my_name":
            if "name" in memory:
                speak(f"Your name is {memory['name']}")
            else:
                speak("I don't know your name yet")

        elif intent == "play_song":

         song = command.replace("play", "").strip()

         speak(f"Playing {song}")

         pywhatkit.playonyt(song)

        elif intent == "weather":
            speak(get_weather())

         

        

        # VOLUME
        elif intent == "volume_up":
            pyautogui.press("volumeup")
            speak("Volume increased")

        elif intent == "volume_down":
            pyautogui.press("volumedown")
            speak("Volume decreased")

        elif intent == "mute":
            pyautogui.press("volumemute")
            speak("System muted")

        # AI
        else:
            reply = ai_response(command)
            speak(reply)

    except sr.UnknownValueError:
        pass

    except Exception as e:
        print("ERROR:", e)
        speak("Something went wrong")