import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():

    duration = 5
    filename = "voice.wav"

    print("Listening...")

    recording = sd.rec(
        int(duration * 16000),
        samplerate=16000,
        channels=1
    )

    sd.wait()

    sf.write(filename, recording, 16000)

    recognizer = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except Exception:
        print("Could not understand")
        return ""