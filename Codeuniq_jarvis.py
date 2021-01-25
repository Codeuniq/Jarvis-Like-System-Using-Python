import speech_recognition as sr
from translate import Translator
from gtts import gTTS
from playsound import playsound

def take_commands():
    listner=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        listner.adjust_for_ambient_noise(source)
        voice=listner.listen(source)
        try:
            Text=listner.recognize_google(voice)
            text=Text.lower()
            print(text)
        except Exception as e:
            print(e)
            print("Can you please repeat it")
            return "None"
    return text

def Speak(txt):
    ob = gTTS(txt,lang='en')
    ob.save("bot.mp3")
    playsound("bot.mp3")

while True:
        command = take_commands()
        if "exit" in command:
            txt="Sure! Thanks for using Codeuniq bot, Bye"
            Speak(txt)
            break
        if "insta" in command:
            txt="You can find out in instagram as Codeuniq_"
            Speak(txt)
        if "instagran" in command:
            txt="You can find out in instagram as Codeuniq_"
            Speak(txt)
        if "fb" in command:
            txt="You can find out in facebook as Codeuniq projects"
            Speak(txt)
        if "facebook" in command:
            txt="You can find out in facebook as Codeuniq projects"
            Speak(txt)
        if "name" in command:
            txt="My name is Codeuniq."
            Speak(txt)
        if "thank" in command:
            txt="It's My pleasure"
            Speak(txt)
        if "help" in command:
            txt="Sure.. How can i help you"
            Speak(txt)
        else:
            print("Can't recogonise")
