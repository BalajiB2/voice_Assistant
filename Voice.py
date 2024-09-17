import speech_recognition as sr
import pyttsx3
import webbrowser
import os

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice commands from the user
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            print("Recognizing...")
            command = recognizer.recognize_google(audio, language='en-US')
            print(f"User said: {command}\n")
    except Exception as e:
        print("Sorry, I couldn't understand. Could you repeat that?")
        return None
    return command.lower()

# Function to perform tasks based on voice commands
def perform_task(command):
    if 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    
    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif 'open notepad' in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif 'play music' in command:
        music_dir = 'C:\\path\\to\\your\\music\\folder'  # Change this path to your local music folder
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
    
    elif 'exit' in command or 'quit' in command:
        speak("Goodbye!")
        exit()

    else:
        speak("I didn't get that. Can you please repeat?")

# Main function to run the voice assistant
def voice_assistant():
    speak("Hello, how can I assist you?")
    while True:
        command = take_command()
        if command:
            perform_task(command)

# Run the assistant
if __name__ == "__main__":
    voice_assistant()
