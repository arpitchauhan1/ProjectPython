from pyttsx3 import engine
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def speakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def Takecommand():
    try:
        with sr.Microphone() as source2:
            # wait for the recognizer to adjust the energy threshold
            r.adjust_for_ambient_noise(source2,duration=0.3)  

            #listen to the imput from user
            print('i am jarvis and listening you...')

            audio2 = r.listen(source2)

            mytext = r.recognize_google(audio2)
            mytext = mytext.lower()

            print("Did you say"+ mytext)
            speakText(mytext)

    except sr.RequestError as e:
        print("Could Not request Result; {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown Error occured")