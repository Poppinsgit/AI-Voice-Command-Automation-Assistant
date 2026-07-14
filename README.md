# AI Voice Command Automation Assistant

A Python-based desktop automation assistant that accepts voice commands and performs system operations on macOS.

## Version 2.0.0 — NLP Intent Detection

V2 replaces V1's keyword/if-else command matching with a trained NLP intent classifier (TF-IDF + Naive Bayes) for a core set of commands, falling back to rule-based matching for everything else.
User command
|
NLP Intent Classifier (TF-IDF + Naive Bayes)
|
Confidence >= 0.30?
|-- Yes -> Execute matched intent
|-- No  -> Fall back to rule-based command matching
## Features

**NLP-classified intents (V2):**
- Open Chrome
- Open YouTube
- Open Calculator
- Take screenshot
- Tell the time

**Rule-based fallback (inherited from V1, still active for everything else):**
- File and folder management (create/delete files, create/open folders)
- Google and YouTube search with a query
- Open Downloads / Documents / Applications folders
- Battery status check
- Open VS Code
- Exit

- Voice recognition (Google Web Speech API)
- Text-to-speech response

## Technologies Used

- Python
- scikit-learn (TF-IDF vectorizer, Multinomial Naive Bayes)
- SpeechRecognition
- pyttsx3
- SoundDevice / SoundFile
- OS Automation (macOS `open`, `screencapture`, `pmset`)
- Web Automation (`webbrowser`, URL-based search)

## Requirements

- **macOS only** — uses macOS-specific commands (`open`, `screencapture`, `pmset`).
- **Internet connection required** — voice recognition uses Google's Web Speech API.
- Voice input uses a fixed 5-second recording window per command.

## How to Run

Install dependencies:
```bash
pip install -r requirements.txt
```

Run:
```bash
python main.py
```

## Example Commands

**NLP-classified:** "open chrome" / "launch chrome" · "open youtube" · "open calculator" · "take screenshot" · "what time is it"

**Rule-based fallback:** "create folder [name]" / "create file [name]" / "delete file [name]" / "open folder [name]" · "search google [query]" / "search youtube [query]" · "open downloads" / "open documents" / "open applications" · "battery" · "vscode" · "exit"

## Known Limitations

- The NLP classifier is trained on only 5 intents and always predicts one of those 5 — it has no "none of the above" category. Commands clearly outside those 5 may occasionally still get a confident-but-wrong match rather than correctly falling through to the rule-based handlers.
- **Planned next step (V3):** add a negative/"OTHER" training class so out-of-scope commands reliably fall through, and expand NLP-classified coverage over time.

## Notes

Built as a self-directed learning project to practice NLP-based intent classification, voice recognition, and system/web automation in Python.
