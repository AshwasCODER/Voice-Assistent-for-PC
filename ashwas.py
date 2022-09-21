import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import pyautogui
import keyboard







engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir !")

    elif hour>12 and hour<18:
        speak("good afternoon sir !")

    else:
        speak("good evening sir !")



    speak(" I am ZIRA 11.0 ,  speed 1 tera harz memory one terabyte ,  your personal voice assistent. plese tell me sir how may i help you")




def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Lisining.......")
        r.pause_thresshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")


    except Exception as e:
        print("Please say that again sir .....")
        return "None"
    return query



def Music():
    speak("Tell me the name of the song ! sir ")
    musicName = takeCommand()
    pywhatkit.playonyt(musicName)

    
 


if __name__ == "__main__":

    wishme()



    while True:
        
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('searching wikipedia.... please wait sir')
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query, sentences=3)
            speak("Accoding to wikipedia")
            print(results)
            speak(results)

        elif' how are you ' in query:
            speak(" i am fine sir ")


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("done sir")

          
        elif'stop' in query:
            keyboard.press('space bar')
        elif 'restart' in query:
            keyboard.press('0')
        elif 'mute' in query:
            keyboard.press('m')
        elif 'skip' in query:
            keyboard.press('l')
        elif 'back' in query:
            keyboard.press('j')
        elif 'full screen' in query:
            keyboard.press('f')    
        elif 'flim ' in query:
            keyboard.press('t') 
       

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("done sir")

        
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("done sir")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak("done sir")

        elif 'open telegram' in query:
            webbrowser.open("https://web.telegram.org")
            speak("done sir")

        elif 'play music' in query:
             Music() 


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak (f"sir the time is {strTime}")
            
        elif 'vs studio' in query:
            vsstudiopath = "C:\\Users\\91736\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vsstudiopath)
            speak("done sir")

        elif 'open pro' in query:
            cpath = "C:\Program Files (x86)\Dev-Cpp\devcpp.exe"
            os.startfile(cpath)
            speak("done sir")


        elif 'open master' in query:
            pathTM = "C:\\Program Files (x86)\\TypingMaster\\tmaster.exe"
            os.startfile(pathTM)
            speak("done sir ")

        elif 'open amazon' in query:
            apath = "https://www.amazon.in/ref=as_li_ss_tl?ie=UTF8&linkCode=ll2&tag=enin-edge-topsites-curate-ana-21&linkId=fbedcb44d04a4bae8eae32722a2f41c2&language=en_IN"
            os.startfile(apath)
            speak("done sir")

        elif 'open flipkart' in query:
            fpath = "https://www.flipkart.com"
            os.startfile(fpath)
            speak("done sir ")

       
        elif 'youtube search' in query:
            speak(" ok sir , that is what i found for your search")
            query = query.replace("Zira","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("done sir")
    
        elif 'google search' in query:
            speak(" ok sir , that is what i found for your search")
            query = query.replace("google search","")
            pywhatkit.search(query)
            speak("done sir")

        elif 'thank you' in query:
            speak("Welcome sir")
 
        elif 'screenshot' in query:
            speak(" ok sir")
            sc =pyautogui.screenshot()
            path = "C:\\Users\91736\Pictures\Saved Pictures\\ +" ".png"
            sc.save(path)
            speak("done sir")
 
        elif 'my location' in query:
            speak("searching.....")
            webbrowser.open('https://www.google.co.in/maps/place/Burdwan,+West+Bengal/@23.2462592,87.8487396,14z/data=!3m1!4b1!4m5!3m4!1s0x39f849d1ea7e5efd:0x4ce71a0a521f8b0e!8m2!3d23.2324214!4d87.8614793')

        elif 'you need a break' in query:
            speak( " ok sir ,  you can call me any time ")
            break
        
        
       

        
            
            