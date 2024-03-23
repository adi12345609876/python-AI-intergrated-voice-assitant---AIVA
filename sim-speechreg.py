import speech_recognition as sr
import pyttsx3
import webbrowser
from functions import Aifunctions

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("You:", query)
        return query
    except Exception as e:
        print(e)
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def printandspeak(text):
    if isinstance(text,str):
        print(f'AIVA:{text}')
        speak(text)
        writemd(f"AIVA:{text}")
    elif isinstance(text,tuple):
        x,y,*z=text
        print(f'AIVA:{y}')
        speak(x)

def writemd(text):
     with open('text.md', 'a') as f:
        f.write(text)
        f.write("---")
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

    welcomeText="Hello! I'm your voice assistant Aiva. How can I help you?"
    printandspeak(welcomeText)
    printandspeak("Type 1 for VOICE mode\nType 2 for WRITE mode")
    input_mode=int(input("MODE (1 or 2):"))
    with open('text.md', 'w') as f:
        
        f.write("\n")
    while True:
        if input_mode == 1:
           query = listen().lower()
        elif input_mode == 2:
            query = input("Enter your prompt:").lower()
     
        if len(query)>0:
            if "hello" in query:
                printandspeak("Hello! How are you?")
            elif "how are you" in query:
                printandspeak("I'm fine, thank you!")
            elif "open" in query.split()[0]:
                linkName=query.split()[1].lower()
                printandspeak(f"Opening {linkName}...")
                
                if linkName in website_links:
                    genrated_web_link=website_links[linkName] 
                else:
                    genrated_web_link=Aifunctions.promtgen(f"Your are an assistant , you're asked to genrate link for {linkName} , genrate the link only",stop_sequences_prompt=None)
                webbrowser.open(genrated_web_link, new=2)
            elif "use ai" in query:
                printandspeak("AI engine started")
                Answer_mode="short"
                work_area="prompt"
                while True:
                    Max_Token=50 if Answer_mode == "short" else (1000 if "long" else 100)
                    query_prompt=modedQuery(input_mode)
                    
                    if "stop ai" in query_prompt:
                        printandspeak("stoping AI engine")
                        break
                    if "open aiva setting" in query_prompt:
                        printandspeak("opened settings...")
                        work_area="settings"
                    if work_area=="prompt":
                        Ai_response_text=Aifunctions.promtgen(query_prompt,stop_sequences_prompt=["."],max_output_tokens_prompt=Max_Token)
                        
                        printandspeak(Ai_response_text)

                    if work_area=="settings":
                        Answer_mode=input("*Change Answer mode*\nEnter(long/short):")
                        work_area="prompt"
            elif "stop program" in query:
                printandspeak("Goodbye!    ")
                printandspeak("Thank you for using Aiva")
                break
            else:
                printandspeak("I'm sorry, I didn't understand that.")
        else:
            printandspeak("I can't hear you")

if __name__ == "__main__":
    main()
