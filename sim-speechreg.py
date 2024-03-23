import speech_recognition as sr
import pyttsx3
import webbrowser
from functions import Aifunctions
from functions import Commfn
from PyDictionary import PyDictionary
from functions import Autopyfn 
import time
import pyautogui
import pywhatkit
dictionary=PyDictionary()

def listen():
    recognizer = sr.Recognizer()
             
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
       
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        # listen()
        print("You:", query)
        return query
        
        
    except Exception as e:
        print(e)
        return ""
        

def speak(text):
    engine = pyttsx3.init()
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

def printandspeak(text):
    if isinstance(text,str):
        speak(text)
        print(f'AIVA:{text}')
        writemd(f"AIVA:{text}")
        with open('text.md', 'a') as f:
                f.write("---\n")
    elif isinstance(text,tuple):
        speak(x)
        x,y,*z=text
        print(f'AIVA:{y}')
        writemd(f"AIVA:{text}")
        with open('text.md', 'a') as f:
                f.write("---\n")

def writemd(text,fileName='text.md'):
     with open('text.md', 'a') as f:
        f.write(text)
        f.write("\n")
        
def modedQuery(Mode,inputText="Enter your prompt:"):
    if Mode == 1:
        query = listen().lower()
    elif Mode == 2:
        query= input(inputText).lower()
    return query

def main():
    website_links = {
    "google": "https://www.google.com",
    "chrome": "https://www.google.com", 
    "facebook": "https://www.facebook.com",
    "twitter": "https://twitter.com",
    "instagram": "https://www.instagram.com",
    "youtube": "https://www.youtube.com",
    "linkedin": "https://www.linkedin.com",
    "reddit": "https://www.reddit.com",
    "amazon": "https://www.amazon.com",
    "ebay": "https://www.ebay.com",
    "stackoverflow": "https://stackoverflow.com"
    }
    welcomeText="Hello! I'm Aiva."
    printandspeak(welcomeText)
    work_area="home"
    song_spotify_playlist="https://open.spotify.com/playlist/4f8pDIL1Sjb7jBr04ssx9I?si=e59929325a324ba2"
    # printandspeak("Type 1 for VOICE mode\nType 2 for WRITE mode")
    input_mode=int(input("MODE (1 or 2):"))
    # input_mode=1
    with open('text.md') as f:
        writemd(f.readline(),fileName='History.md')
    with open('text.md', 'w') as f:
        f.close()
        # f.write("\n")
    while True:
        query=modedQuery(input_mode)
        writemd(f"User:{query}")
        # print(query.split())
        if len(query)>0:
            #HOME workspace
            if "stop program" in query:
                printandspeak("Goodbye!    ")
                printandspeak("Thank you for using Aiva")
                break
            elif "hello" in query or "hi" in query or "hey aiva" in query:
                printandspeak("Hello! How are you?")
            elif "how are you" in query:
                printandspeak("I'm fine,thank you!")
            elif "i am fine" in query:
                printandspeak("I'm fine too")
            elif "play my song" in query or "play my playlist" in query:
                Autopyfn.clickButtonInWeb('c:/Users/radin/Documents/Adi light/Code/AIVA beta/images/spotifyPlayButton.png',song_spotify_playlist) 
            elif "play" in query.split()[0] and "song" in query.split()[-1]:
                search_par=Commfn.listToString(query.split()[1:-1])
                spotify_artist_search=f"https://open.spotify.com/search/{search_par}"
                pyautogui.moveTo(494,433)
                webbrowser.open(spotify_artist_search, new=2) 
                Autopyfn.clickSpotifyPlayButton(spotify_artist_search,0.7)
            elif "play the song".split() == query.split()[:3]:
                if Commfn.listToString(query.split()[3:]) == None:
                    search_par=Commfn.listToString(query.split()[3:])
                else:
                    printandspeak("what song sir")
                    search_par=modedQuery(input_mode)
                    
                spotify_artist_search=f"https://open.spotify.com/search/{search_par}"
                pyautogui.moveTo(494,433)
                webbrowser.open(spotify_artist_search, new=2) 
                Autopyfn.clickSpotifyPlayButton(spotify_artist_search,0.7)
            elif "play video".split() == query.split()[:2] or "play a video".split() == query.split()[:3]:
                if input_mode==1:
                    printandspeak("tell the video title or channel")
                video_query=modedQuery(input_mode,inputText="Enter Video name or channel title:")
                pywhatkit.playonyt(video_query)

            elif "stop song" in query:
                printandspeak("stopping song...")
                pyautogui.press('space',interval=1) 
            elif "unstop song" in query:
                printandspeak("stopping song...")
                pyautogui.press('space',interval=1) 
                
            elif ['find', 'meaning', 'for'] == query.split()[0:3]:
                word_tofind_meaning=" ".join(query.split()[3:])
                meaning_pair=dictionary.meaning(word_tofind_meaning)
                meaning=(list(meaning_pair.values())[0][0])
                printandspeak(f"meaning of {word_tofind_meaning} is {meaning}")

            elif "open" in query.split()[0]:
                linkName=query.split()[1].lower()
                printandspeak(f"Opening {linkName}...")
                
                if linkName in website_links:
                    genrated_web_link=website_links[linkName] 
                else:
                    genrated_web_link=Aifunctions.promtgen(f"Your are an assistant , you're asked to genrate link for {linkName} , genrate the link only",stop_sequences_prompt=None)
                webbrowser.open(genrated_web_link, new=2)
            #SETTINGS workspace
            elif "get to aiva setting" in query:
                printandspeak("opened settings...")
                work_area="settings"
                
            #AI workspace
            elif "use ai" in query:
                printandspeak("AI engine started")
                Answer_mode="long"
                work_area="ai"
            else:
                printandspeak("Sorry ! i can't understand that")
            #WORKSPACES
            ##settings
            while work_area=="settings":
                    Answer_mode=input("*Change Answer mode*\nEnter(long/short):") or Answer_mode
                    work_area="home"
            ##ai
            while work_area=="ai":
                Max_words=100 if Answer_mode == "short" else (10000 if "long" else "as many")
                query_prompt=modedQuery(input_mode)
                writemd(f"User:{query_prompt}")
                if "stop ai" in query_prompt:
                    printandspeak("stoping AI engine")
                    work_area=="home"
                    break
                else:
                    Ai_response_text=Aifunctions.promtgen(query_prompt,max_words_prompts=Max_words)
                    printandspeak(Ai_response_text)
            with open('text.md', 'a') as f:
                f.write("---\n")
        else:
            print("I can't hear you")

if __name__ == "__main__":
    main()
