import webbrowser
import urllib.parse
import os


def web_command(command):

    if "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google"


    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"


    elif "search google" in command:
        query = command.replace("search google", "").strip()

        url = "https://www.google.com/search?q=" + urllib.parse.quote(query)

        webbrowser.open(url)

        return "Searching Google"


    elif "search youtube" in command:
        query = command.replace("search youtube", "").strip()

        url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(query)

        webbrowser.open(url)

        return "Searching YouTube"


    return None