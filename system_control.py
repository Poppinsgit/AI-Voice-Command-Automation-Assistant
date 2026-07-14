import os
import subprocess


def system_command(command):

    if "take screenshot" in command:
        os.system("screencapture screenshot.png")
        return "Screenshot taken"


    elif "open downloads" in command:
        os.system("open ~/Downloads")
        return "Opening downloads folder"


    elif "open documents" in command:
        os.system("open ~/Documents")
        return "Opening documents folder"


    elif "battery" in command:
        result = subprocess.check_output(
            "pmset -g batt",
            shell=True
        ).decode()

        return result


    elif "open applications" in command:
        os.system("open /Applications")
        return "Opening applications"


    return None
