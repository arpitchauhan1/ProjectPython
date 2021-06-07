import speech_recognition as sr
import pyttsx3


listner = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
     try:
         with sr.Microphone() as source:
             print('listening....')
             voice = listner.listen(source)
             command = listner.recognize_google(voice)
             command = command.lower()
             if 'alexa' in command:
                 command = command.replace('alexa', '')
                 print(command)
                 except:
                     pass
                    return command
                    
                    def run_alexa():
                        command = take_command()
                        print(command)
                        if 'play' in command:
                            talk('playing')
                            print('playing')
                            run_alexa()