import speech_recognition as sr
import pyttsx3


def speak(words):
    engine = pyttsx3.init('sapi5')

    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)

    engine.say(words)
    engine.runAndWait()
    engine.stop()


r = sr.Recognizer()
r.pause_threshold = 1


with sr.Microphone() as source:
    print("Calibrating...")
    r.adjust_for_ambient_noise(source)

print("Ciel is ready.")


while True:

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        model_output = r.recognize_google(audio)
        model_output = model_output.lower()

        print("You:", model_output)

        if model_output == "hello" or model_output == "hi":
            speak("Hello, how can I help you?")

        elif model_output == "who are you":
            speak("I am Ciel, an AI assistant.")

        elif model_output == "what is your name":
            speak("My name is Ciel.")

        elif model_output in ["bye", "bye-bye", "goodbye"]:
            speak("Goodbye.")
            break

    except sr.UnknownValueError:
        print("Sorry, I did not get that.")

    except sr.RequestError:
        print("Could not connect to Google Speech Recognition.")
