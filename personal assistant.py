import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import re
import subprocess
import json
import requests
""" import openai """



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
""" openai.api_key = os.getenv("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")

def generateResponse(statement):
    response = openai.Completion.create(
    engine="davinci",
    prompt="",
    temperature=0.7,
    max_tokens=64,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    ) """
class AI :
    name = " ana "
    state = True

region="es-AR"
def recognizer(audio):
    try:
        statement=" "+r.recognize_google(audio,language=region)
        print(f"mic: {statement}\n")
        return statement
    except Exception as e:
        return "None"
def speak(text):
    print(f"{AI.name}: {text}")
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()
m = sr.Microphone()

def takeCommand(): #take a command
    with m as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        statement = recognizer(audio)
        return statement

def hello():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,  Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,  Good Afternoon")
    else:
        speak("Hello,  Good Evening")
        
""" def sendWhatMsg():
    user_name = {
        'Jarvis': '+91 95299 16394'
    }
    try:
        output("To whom you want to send the message?")
        name = inputCommand()
        output("What is the message")
        we.open("https://web.whatsapp.com/send?phone=" +
                user_name[name]+'&text='+inputCommand())
        sleep(6)
        pyautogui.press('enter')
        output("Message sent")
    except Exception as e:
        print(e)
        output("Unable to send the Message")
 """
statement = "None"
program_state: bool = True
if __name__=='__main__':
    while program_state:
        if not AI.state:
            statement = takeCommand().lower()
        if (AI.name in statement and "préndete" in statement) or AI.state:
            AI.state = True
            print("load")
            while AI.state:
                statement = takeCommand().lower()

                if " apaga te " in statement and AI.name in statement:
                    speak("Ok, good bye")
                    program_state = False
                    AI.state = False
                
                elif AI.name in statement and " cállate " in statement and " minutos " in statement:
                    waitfor= int(re.search(r'por ', statement)[0])*60
                    speak("i will be later for {waitfor}")
                    print(waitfor)
                    time.sleep(statement.isdigit()*60)
                    speak("i am back")
                
                elif AI.name in statement and " cállate " in statement:
                    speak("i will be later")
                    AI.state = False
                    break

                elif AI.name in statement and " quesos " in statement:
                    speak("i am an artificial inteligence made by dante alfonso, only because he was bored")

                    
                elif "quien es tu creador" in statement or "quien te creo" in statement:
                    speak("I was built by Dante D. Alfonso")
                
                elif " decí " in statement and AI.name in statement:
                    statement: statement =statement.replace(AI.name, " ",1)
                    if " decí " in statement: statement =statement.replace(" decí ", " ",1)
                    speak(statement)

                elif AI.name in statement and "hola" in statement:
                    hello()
                
                elif ' hora es ' in statement and  AI.name in statement:
                            strTime=datetime.datetime.now().strftime("%H:%M")
                            speak(f"the time is {strTime}")
                
                elif ' wikipedia ' in statement and AI.name in statement:
                            speak('Searching Wikipedia...')
                            statement =statement.replace(AI.name, " ",1)
                            statement =statement.replace(" wikipedia ", " ",1)
                            if statement != "" :
                                try: 
                                    results = wikipedia.summary(statement, sentences=3)
                                    speak("According to Wikipedia")
                                    speak(results)
                                except Exception as e:
                                    speak("Sorry, I can't find any result")
                                break
                            else:
                                speak("what")

                elif AI.name in statement:
                    speak("what")
                    while True:
                        statement = takeCommand().lower()
                        if "no" in statement and "gracias" in statement:
                            speak('ok')
                            break

                        elif 'open youtube' in statement:
                            webbrowser.open_new_tab("https://www.youtube.com")
                            speak("youtube is open now")
                            time.sleep(5)
                            break

                        elif 'open google' in statement:
                            webbrowser.open_new_tab("https://www.google.com")
                            speak("Google chrome is open now")
                            time.sleep(5)
                            break

                        elif 'open gmail' in statement:
                            webbrowser.open_new_tab("gmail.com")
                            speak("Google Mail open now")
                            time.sleep(5)
                            break

                        elif "log off" in statement or "sign out" in statement:
                            speak("Ok , the PC will log off")
                            subprocess.call(["shutdown", "/l"])
                            break

                            """ elif statement!="error":
                            speak("I cant do that") """
                        elif "error" in statement:
                            speak("repeat")
                            break