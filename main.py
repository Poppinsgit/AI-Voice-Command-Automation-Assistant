from voice import listen, speak
from system_control import system_command
from web_control import web_command
from file_manager import file_command
from intent_model import predict_intent
import os
import datetime


def execute_command(command):

    intent, confidence = predict_intent(command)

    print("Detected Intent:", intent)
    print("Confidence:", round(confidence * 100, 2), "%")

    if confidence < 0.30:
        speak("Sorry, I am not confident enough to perform that command.")
        return

    if intent == "OPEN_CHROME":
        os.system("open -a 'Google Chrome'")
        speak("Opening Chrome")
        return


    elif intent == "OPEN_YOUTUBE":
        import webbrowser
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
        return


    elif intent == "OPEN_CALCULATOR":
        os.system("open -a Calculator")
        speak("Opening Calculator")
        return


    elif intent == "SCREENSHOT":
        os.system("screencapture screenshot.png")
        speak("Screenshot taken")
        return


    elif intent == "TIME":
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is " + time)
        return

    if intent == "OPEN_CHROME":
        speak("Opening Chrome")
        os.system("open -a 'Google Chrome'")
        return

    elif intent == "SCREENSHOT":
        speak("Taking screenshot")
        os.system("screencapture screenshot.png")
        return


    result = file_command(command)

    if result:
        speak(result)
        return
    
    result = web_command(command)

    if result:
        speak(result)
        return
    
    result = system_command(command)

    if result:
        speak(result)
        return


    if "chrome" in command:
        os.system("open -a 'Google Chrome'")
        speak("Opening Chrome")


    elif "calculator" in command:
        os.system("open -a Calculator")
        speak("Opening calculator")


    elif "vscode" in command:
        os.system("open -a 'Visual Studio Code'")
        speak("Opening Visual Studio Code")


    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is " + time)


    elif "exit" in command:
        speak("Goodbye")
        exit()


    else:
        speak("I don't know this command yet")


speak("Voice assistant started")


while True:

    command = listen()

    if command:
        execute_command(command)