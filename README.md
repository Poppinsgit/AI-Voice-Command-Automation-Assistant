# AI Voice Command Automation Assistant

A Python-based desktop automation assistant that accepts voice commands and performs system operations on macOS.

## Features

- Voice recognition (via Google's Web Speech API)
- Text-to-speech response
- Open applications (Chrome, Calculator, VS Code)
- File and folder management (create/delete files, create/open folders)
- Google search automation
- YouTube search automation
- Screenshot capture
- Battery status check

## Technologies Used

- Python
- SpeechRecognition
- pyttsx3
- SoundDevice / SoundFile
- OS Automation (macOS `open`, `screencapture`, `pmset`)
- Web Automation (`webbrowser`, URL-based search)

## Requirements

- **macOS only** — uses `open -a`, `screencapture`, and `pmset`, which are macOS-specific and won't run on Windows or Linux.
- **Internet connection required** — voice recognition uses Google's Web Speech API, not offline recognition.
- Each voice command is captured in a fixed 5-second recording window.

## How to Run

Install dependencies:
```
pip install -r requirements.txt
```

Run:
```
python main.py
```

## Example Commands

- "open google" / "open youtube"
- "search google [query]" / "search youtube [query]"
- "create folder [name]" / "create file [name]" / "delete file [name]" / "open folder [name]"
- "open downloads" / "open documents" / "open applications"
- "take screenshot"
- "battery"
- "chrome" / "calculator" / "vscode"
- "time"
- "exit"

## Project Evolution

V1.0.0 — Rule-Based Automation Assistant

The initial version uses command-based logic to map user inputs to automation tasks.

V2.0.0 — NLP Enhanced Assistant (Planned)

Future improvements:

NLP-based intent classification
Understanding multiple command variations
Machine learning based command interpretation
Improved scalability beyond fixed command matching

## Notes

Built as a self-directed learning project to practice voice recognition, text-to-speech, and system/web automation in Python. A planned V2 will replace the current if/elif command matching with NLP-based intent detection.