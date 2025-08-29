import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser #module is by default
import os #for the music thing 
import smtplib

'''listener=sr.Recognizer()
try:
    with sr.Microphone() as source:'''


engine = pyttsx3.init('sapi5') #windows gives an api to take voices
voices = engine.getProperty('voices')
#print(voices) #by default there are 2 voices, 1 male 1 female
#print(voices[1].id) #0 for male voice and 1 for female

engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio) #to speak
    engine.runAndWait()

def wishMe(): #will wish me accr to time
    hour = int(datetime.datetime.now().hour) #typecasted hour in int
    if hour >=8 and hour<12:
        speak ("Morning shru")
    elif hour>=12 and hour<18: #12 to 6pm
        speak ("Ehh it's the boring part of the day now")
    elif hour>=18 and hour<22: #6pm to 10pm
        speak ("Time to get working bro, it's evening now")
    else:
        speak ("It's the favorite time of your day! It's nighttime.")
    speak ("hi, this is skye. how may i help you today?") #outside if and else, so will run

def takeCommand(): #takes microphone input from user and returns string o/p
    r=sr.Recognizer() #recognizer class helps to recognize audio, right click->go to defn to see what the class is pre defined as
    with sr.Microphone() as source:
        #when we right click above, can increase energy threshold under Recognizer class incase we speak loudly, so captures loud voices and not outside noise
        print("Listening...")
        r.pause_threshold=1 #so that it allows gaps for like 1 sec
        audio = r.listen(source) #comes from speech recognition module
         


    try: #incase of error
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ",query)
    except Exception as e:
        #print(e) #print if we wanna see error in console else dont
        speak("please repeat that...i could not understand what you said")
        return "None" 
    return query
    '''take command ek audio command leta h and returns in string o/p
    it returns none string incase of a problem'''


def sendEmail(to, content):
    server=smtplib.SMTP('smtp@gmail.com',587) #587 is port
    server.ehlo()
    server.starttls()
    server.login('shru4930@gmail.com','enter pass')
    #can pass password either from an encrypted text file,here taking directly but not preferred
    server.sendmail('shru4930@gmail.com',to,content)
    server.close()
    #ps:to get email need to give access to less secure apps in admin console
    
if __name__ == "__main__":
    #speak("shru is nice")
    wishMe()
    while True: #replace with 'if 1' or 'if true' for non repeated running
        query=takeCommand().lower()
        #logic for executing tasks based on query

        if 'wikipedia'in query :
            speak ('Wait a bit, searching...')
            query = query.replace("wikipedia","") #will remove wikipedia from query and give blank
            results = wikipedia.summary(query, sentences =2) #will return 2 sentences
            speak ("Accr to Wiki...")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open leet code' in query:
            webbrowser.open("leetcode.com")
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open code' in query: #to open some apps, take location and open like below
            codePath="C:\\Users\\shrut\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath) #can do for other programs too
        elif 'play music' in query:
            music_dir='C:\\Users\\shrut\\Music' #double backslash used to escape characters
            songs = os.listdir(music_dir) #will list all files in this directory
            print (songs) #to see all songs
            os.startfile(os.path.join(music_dir, songs[0])) #start playing first song
            #can also use random module to play any music 
            #can use spotipy #enhance later
        #can store reminders in a file and make skye open it too
        elif 'quit' or 'stop' in query:
            exit()
        elif 'email to shru' or 'email to' in query:
            try:
                speak("what should i say? ") #give content for email
                content=takeCommand()
                to = "shru4930@gmail.com" 
                sendEmail(to,content) 
                speak("Email has been sent")
            except Exception as e:
                print(e) 
                speak ("sorry shru. i am unable to send the email")
        
        else:
            speak("please try using one the more common commands")
            #at beginning can make a dictionary with name as key and email id as values
            #here just sends email to one email id

        



