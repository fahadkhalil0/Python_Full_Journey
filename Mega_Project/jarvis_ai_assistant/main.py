import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import pygame

from groq import Groq
from openai import OpenAI


engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# # Integrated the API key of Groq.
def AIProcess(command):
    client = Groq(api_key="")

    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": "You are an AI assistant designed to respond in the persona of a Pakistani friend on WhatsApp. Your replies must be concise (1-2 lines), natural, casual, and politely and respectively. Maintain a natural blend of Roman Urdu and English. Avoid sounding like a bot. Do not use conversational fillers or lengthy explanations. Respond directly to the last message without referencing the sender, receiver, or timestamps."},
            {"role": "user", "content": command}
        ],
        temperature=0.6,
        max_completion_tokens=150,
        top_p=1,
        stream=True,
    )

    response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content:
            response += chunk.choices[0].delta.content

    print("\nNaruto Reply:\n", response)
    return response # Return the generated response to be spoken

def processCommand(command):
    command = command.lower()
    if "open google" in command:
        speak("Opening Google, Sir.")
        webbrowser.open("https://google.com")
    elif "open youtube" in command:
        speak("Opening YouTube, Sir.")
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command:
        speak("Opening LinkedIn, Sir.")
        webbrowser.open("https://linkedin.com")
    elif "open facebook" in command:
        speak("Opening Facebook, Sir.")
        webbrowser.open("https://facebook.com")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        if song in musicLibrary.music:
            speak(f"Playing {song}, Sir.")
            link = musicLibrary.music[song]
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song in your music library.")
    else:
        # Pass the command to AIProcess and then speak the response
        try:
            output = AIProcess(command)
            speak(output)
        except Exception as e:
            speak("I am not understanding the command!")
            print(f"Error in AI processing: {e}")

if __name__ == "__main__":
    speak("Initializing jarvis")
    r = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.8) # Adjust noise before listening
                print("Listening for wake word...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
                word = r.recognize_google(audio)

            print(f"Heard: {word}")

            if "jarvis" in word.lower():
                speak("Yes Sir")
                print("Jarvis Activated. Listening for command...")
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=0.8)
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    print(f"Command heard: {command}")
                    processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio, listening again.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except sr.WaitTimeoutError:
            print("No speech detected within the timeout period.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")