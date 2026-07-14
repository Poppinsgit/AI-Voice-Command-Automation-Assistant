from voice import listen, speak
from system_control import system_command
from web_control import web_command
from file_manager import file_command
import os
import datetime


def execute_command(command):

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