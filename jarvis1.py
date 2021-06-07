from pyttsx3 import speak
import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
import os
import datetime
import requests
import wolframalpha

#initializing the recognizer
r = sr.Recognizer()

def SpeakText(command):   #bolna
    #initialize the engine
    e = pyttsx3.init()
    e.say(command)
    e.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning")

    elif hour>=12 and hour<=18:
        speak("Good afternoon")

    else:
        speak("Good evening")

    speak("I am Jarvis sir Please tell me how may i help you")

app = wolframalpha.Client("YH7T4U-XWUUY3HWEG")



if __name__=="__main__":
    wishme()

# Loopz
def takecom():  #sunnna
    try:
        #use the microphone for input
        with sr.Microphone() as source2:
            # wait for the recognizer to adjust the energy threshold
            r.adjust_for_ambient_noise(source2)

            #listen to the input from user
            print("Listening ...")
            audio2 = r.listen(source2)

            # using google to recognize audio
            MyText = r.recognize_google(audio2)
            
            MyText = MyText.lower()
            print(MyText)
        
    except sr.RequestError as e:
        print("Could Not request Result; {0}".format(e))
    except Exception: #For Error handling
        speak("error...")
        print("Network connection error") 
        return "none"
    return MyText
#SpeakText('hello, hello sir')
def TaskExe():
    def music():
        speak('tell me the name of the song..')
        MusicName = takecom()
        if 'my song' in MusicName:
            os.startfile('sidhu.mp3')
        #elif 'new song' in MusicName:
            #os.startfile('music/we.mp3')
        else:
            pywhatkit.playonyt(MusicName)
        speak('your song has been started.. enjoy')
    
    while True:
        query =takecom()

        if 'hello' in query:
            speak("Hello sir , I am Jarvis")
            speak("your Personal AI Assistant!")
            speak("How May I help you")
        elif 'how are you' in query:
            speak("I am fine Arpit!")
            speak("what about you?") 
        elif 'thank you' in query:
            speak("welcome sir")    
        elif 'bye' in query:
            speak("bye sir")
        elif 'youtube search' in query:
            speak('ok sir, this is what i found for you in search')
            query = query.replace('jarvis',"")
            query = query.replace('youtube search',"")
            web = "https://www.youtube.com/results?search_query="+ query
            webbrowser.open(web)
            #speak("done sir")
            pywhatkit.search(query)
            speak("Done sir")
        elif "google search" in query:
            query = query.replace('google search', " ")
            pywhatkit.search(query)
            speak("done sir")
        elif 'open website' in query:
            speak('Tell me the name of the website..')
            name = takecom()
            web ='https://www.' + name + '.com'
            webbrowser.open(web)
            speak("Done sir")
        elif 'facebook' in query:
            #speak("Done sir")
            webbrowser.open('https://www.facebook.com/')
            speak("Done sir")
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)
        elif 'temperature' in query:
            res = app.query(query)
            speak(next(res.results).text)
        elif 'calculate' in query:
            speak("what should i calculate?")
            gh = takecom().lower()
            res = app.query(gh)
            speak(next(res.results).text)
        elif 'open chrome' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
        elif 'music' in query:
            music()
TaskExe()
