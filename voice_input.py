# voice_input.py
import speech_recognition as sr

def listen_for_command():
    """Captures audio and converts it to text using a speech recognizer."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a command...")
        # Helps the recognizer adapt to ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        # Listens for the first phrase and extract it into audio data
        audio = recognizer.listen(source)

    try:
        # Recognize speech using Google's free web speech API
        command = recognizer.recognize_google(audio)
        print(f"Recognized: '{command}'")
        return command
    except sr.UnknownValueError:
        # API was unable to understand the audio
        return None
    except sr.RequestError:
        # API is unreachable
        print("API unavailable. Please check your internet connection.")
        return None