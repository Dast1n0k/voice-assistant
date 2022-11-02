import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import time
import os # to remove created audio files
import requests
from docx import Document
from parser_news import parser_news

class person:
    name = ''
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

r = sr.Recognizer() # initialise a recogniser

# listen for audio and convert it to text:
def record_audio(ask=''):
    with sr.Microphone() as source: # microphone as source
        if ask:
            speak(ask)
        print("Done Listening")
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            speak('I did not get that')
        except sr.RequestError:
            speak('Sorry, the service is down') # error: recognizer is not connected
        print(f">> {voice_data.lower()}") # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    print(f"Lefty: {audio_string}") # print what app said
    playsound.playsound(audio_file) # play the audio file
    os.remove(audio_file) # remove audio file

def respond(voice_data):
    # 1: greeting
    if there_exists(['hey','hi','hello']):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)

    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
            speak("my name is Lefty")
        else:
            speak("my name is Lefty. what's your name?")

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        speak(f"okay, i will remember that {person_name}")
        person_obj.setName(person_name) # remember name in person object

    # 3: greeting
    if there_exists(["how are you","how are you doing"]):
        speak(f"I'm very well, thanks for asking {person_obj.name}")

    # 4: time
    if there_exists(["what's the time","tell me the time","what time is it"]):
        speak(ctime())

    # 5: search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        #search_term = record_audio('What do you want to find?')
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')

    # 6: search youtube
    if there_exists(["youtube"]):
        search_term = record_audio('What name of video?')
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube')

    # 8: toss a coin
    if there_exists(["flip coin"]):
        moves = ["head", "tails"]
        cmove = random.choice(moves)
        speak("The computer chose " + cmove)

    # 9: current location
    if there_exists(["what is my exact location"]):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        speak("You must be somewhere near here, as per Google maps")

    # 10: find location
    if there_exists(["find location"]):
        location = record_audio('What is the location?')
        if location == 'moscow':
            os.startfile(r'image\1.jpg')
        else:
            url = 'https://www.google.com.ua/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            speak('Here is the location of ' + location)

    # 11: weather
    if there_exists(["what weather", "what about weather", "weather"]):
        city = record_audio('Weather in which city?')
        try:
            params = {'q': city, 'units': 'metric', 'lang': 'en', 'appid': '208efe731338ff247c6843161cc807be'}
            response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
            if not response:
                raise
            w = response.json()
            speak(f"In city {city} {w['weather'][0]['description']} {round(w['main']['temp'])} degrees")

        except:
            speak('Error with API')

    # 12:schedule for group in kpi
    if there_exists(["show my schedule", "my schedule", "my timetable"]):
        ticket = ""
        group = record_audio('What a group').rsplit()
        group[0] = group[0]. replace(".", "")
        group = "".join(group)
        groups = {"po11": "744888e7-4f92-46ba-9330-ac56dfcfb65b", "pk11": "cdf72602-9bc3-46ee-b7f0-048b51def7c5",
                  "pg11": "b4f442dc-8641-4045-a740-b1fc038909a1", "pm11": "d41dad85-dff4-446b-965c-ca8f5547a014",
                  "pb11": "a6c846da-0241-48f3-92c8-44d5aeef7aea", "pb12": "60dffbed-e1ef-494d-a735-7a5e1cef3c52"}
        for key, value in groups.items():
            if key == group:
                ticket = value
        url = "https://schedule.kpi.ua/?groupId=" + ticket
        webbrowser.get().open(url)
        speak("Don't be late for the first lesson")

    # 13:create word file
    if there_exists(["build", "create"]):
        file_name = record_audio("What's the docx file name?")
        word_file = Document()
        word_file.save(file_name + ".docx")
        speak(f"File with name{file_name} created")

    # 14: translate word
    if there_exists(["translate", "translate word", "translator"]):
        word = record_audio('What word?')
        url = f'https://translate.google.com/?hl=en&sl=en&tl=uk&text={word}&op=translate'
        webbrowser.get().open(url)
        speak('Translate' + word + 'to ukrainian')
    # 15: instagram
    if there_exists(["open instagram", "instagram"]):
        url = "https://www.instagram.com/"
        webbrowser.get().open(url)
        speak("New photo of Maxim already posted")

    # 15.1: facebook
    if there_exists(["open facebook", "facebook"]):
        url = "https://www.facebook.com/"
        webbrowser.get().open(url)

    # exit
    if there_exists(["exit", "quit", "goodbye", "bye", "good bye", "close"]):
        byeings = [f"you destroyed me {person_obj.name}", f"you kill me {person_obj.name}",
                     f"going offline {person_obj.name}", f"have a nice day {person_obj.name}",
                     f"goodbye {person_obj.name}"]
        bye = byeings[random.randint(0, len(byeings) - 1)]
        speak(bye)
        exit()

time.sleep(1)

person_obj = person()
while(1):
    voice_data = record_audio() # get the voice input
    respond(voice_data) # respond

