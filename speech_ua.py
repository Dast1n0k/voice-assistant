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
        print("Слухаю тебе")
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="uk")  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            speak('Не зрозумів тебе')
        except sr.RequestError:
            speak('Вибач, сервер впав') # error: recognizer is not connected
        print(f">> {voice_data.lower()}") # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='uk') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(f"Лівобережний: {audio_string}") # print what app said
    os.remove(audio_file) # remove audio file

def respond(voice_data):
    # 1: greeting
    if there_exists(['привіт','прив','добрий день', 'добрий вечір', 'добрий ранок']):
        greetings = [f"привіт, як я можу допомогти тобі {person_obj.name}", f"привіт, як ти чувак {person_obj.name}", f"Я слухаю {person_obj.name}", f"як я можу допомогти тобі {person_obj.name}", f"привіт {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)

    # 2: name
    if there_exists(["як тебе звати","як тебе називати","який в тебе всевдонім"]):
        if person_obj.name:
            speak("Мене звати Лівобережний")
        else:
            speak("Мене звати Лівобережний. Як тебе звати?")

    if there_exists(["мене звати"]):
        person_name = voice_data.split("звати")[-1].strip()
        speak(f"добре, я запам'ятав твоє ім'я {person_name}")
        person_obj.setName(person_name) # remember name in person object

    # 3: greeting
    if there_exists(["як ти","що робиш"]):
        speak(f"В мене все добре, дякую що спитав {person_obj.name}")

    # 4: time
    if there_exists(["котра година","скажи мені годину","че по времені"]):
        speak(ctime())

    # 5: search google
    if there_exists(["знайти", "найди", "пошукай", "окей google", "okey google"]) and 'youtube' not in voice_data:
        search_term = record_audio('Що ти хочешь знайти?')
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Вот що я знайщов в інтернеті за запитом {search_term} в google')

    # 6: search youtube
    if there_exists(["youtube"]):
        search_term = record_audio('What name of video?')
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Вот що я знайшов за запитом {search_term} в youtube')

    # 8: toss a coin
    if there_exists(["кинь монетку"]):
        moves = ["тризуб", "дядько"]
        cmove = random.choice(moves)
        speak("Комп'ютер вибрав " + cmove)

    # 9: current location
    if there_exists(["де я знаходжуся", "моє місцезнаходження"]):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        speak("ти знаходишся десь поблизу цього місця")

    # 10: find location
    if there_exists(["знайди місце", "відкрий карту"]):
        location = record_audio('яке місце ви бажаєте знайти?')
        url = 'https://www.google.com.ua/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('місцезнаходження ' + location + 'знайдено')

    # 11: weather
    if there_exists(["яка погода", "що за вікном", "погода"]):
        city = record_audio('погода в якому місті?')
        try:
            params = {'q': city, 'units': 'metric', 'lang': 'uk', 'appid': '208efe731338ff247c6843161cc807be'}
            response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
            if not response:
                raise
            w = response.json()
            speak(f"В місті {city} {w['weather'][0]['description']} {round(w['main']['temp'])} градусів")

        except:
            speak('помилка API')

    # 12:schedule for group in kpi
    if there_exists(["покажи мій розклад", "мій розклад", "покажи розклад"]):
        ticket = ''
        group = record_audio('Яка група?')
        time.sleep(2)
        group = "".join(group.rsplit())
        groups = {"po11": "744888e7-4f92-46ba-9330-ac56dfcfb65b", "pk11": "cdf72602-9bc3-46ee-b7f0-048b51def7c5",
                  "pg11": "b4f442dc-8641-4045-a740-b1fc038909a1", "pm11": "d41dad85-dff4-446b-965c-ca8f5547a014",
                  "pb11": "a6c846da-0241-48f3-92c8-44d5aeef7aea", "pb12": "60dffbed-e1ef-494d-a735-7a5e1cef3c52",
                  "по11": "744888e7-4f92-46ba-9330-ac56dfcfb65b", "пг11": "b4f442dc-8641-4045-a740-b1fc038909a1",
                  "пб11": "a6c846da-0241-48f3-92c8-44d5aeef7aea", "пк11": "cdf72602-9bc3-46ee-b7f0-048b51def7c5",
                  "пм11": "d41dad85-dff4-446b-965c-ca8f5547a014", "пб12": "60dffbed-e1ef-494d-a735-7a5e1cef3c52",
                  "п11": "a6c846da-0241-48f3-92c8-44d5aeef7aea"}
        for key, value in groups.items():
            if key == group:
                ticket = value
        url = "https://schedule.kpi.ua/?groupId=" + ticket
        webbrowser.get().open(url)
        speak("Не спізнюйся на першу пару!")

    # 13:create word file
    if there_exists(["створи файл", "створи ворд файл", "файл", "створи"]):
        file_name = record_audio("Як ви хочете назвати файл?")
        word_file = Document()
        word_file.save(file_name + ".docx")
        speak(f"Файл під назвою {file_name} був створений")

    # 14: translate word
    if there_exists(["переклади слово", "переклади слова"]):
        word = record_audio('Яке слово ви хочете перекласти?')
        url = f'https://translate.google.com/?hl=ru&sl=uk&tl=en&text={word}&op=translate'
        webbrowser.get().open(url)
        speak('Перекладено' + word + 'на англійську мову')
    # exit
    if there_exists(["вихід", "закрийся", "бувай", "щасливо"]):
        byeings = [f"ти мене знищуєш {person_obj.name}", f"ти мене вбиваєш {person_obj.name}",
                   f"перехожу в оффлайн {person_obj.name}", f"Вдалого дня {person_obj.name}",
                   f"бувай {person_obj.name}"]
        bye = byeings[random.randint(0, len(byeings) - 1)]
        speak(bye)
        exit()


time.sleep(1)

person_obj = person()
while (1):
    voice_data = record_audio()  # get the voice input
    respond(voice_data)  # respond

