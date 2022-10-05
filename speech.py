# Библиотеки распознавания и синтеза речи
import speech_recognition as sr
from gtts import gTTS

import pyowm
# Воспроизведение речи
import pygame
from pygame import mixer

mixer.init()
import datetime
import os
import sys
import time
import datetime
import logging
import webbrowser
import subprocess
print("Hello")

class Speech_AI:
    def __init__(self):
        self._recognizer = sr.Recognizer()
        self._microphone = sr.Microphone()

        now_time = datetime.datetime.now()
        self._mp3_name = now_time.strftime("Drop\\%d%m%Y%I%M%S") + ".mp3"
        self._mp3_nameold = '111'

    def work(self):
        print("Все закрыли пасточки...")

        with self._microphone as source:
            self._recognizer.adjust_for_ambient_noise(source)

        try:
            while True:

                print("Скажи что - нибудь!")
                with self._microphone as source:
                    audio = self._recognizer.listen(source)
                print("Понял, идет распознавание...")
                try:
                    statement = self._recognizer.recognize_google(audio, language="ru_RU")
                    statement = statement.lower()

                    # Weather

                    if ((statement.find("узнать") != -1) and (statement.find("погоду") != -1) or (
                            statement.find("что по погоде") != -1) or (statement.find("как там погода") != -1)):
                        self.openurl('http://t.me/Pogodasiri_bot', " Введите город на английском языке! ")

                    # Команды для открытия различных внешних приложений

                    if ((statement.find("калькулятор") != -1) or (statement.find("calculator") != -1)):
                        self.osrun('calc')

                    if ((statement.find("блокнот") != -1) or (statement.find("notepad") != -1)):
                        self.osrun('notepad')
                    if ((statement.find("paint") != -1) or (statement.find("паинт") != -1)):
                        self.osrun('mspaint')
                    if ((statement.find("browser") != -1) or (statement.find("браузер") != -1)):
                        self.openurl('http://google.ru', 'Открываю браузер')
                    if ((statement.find("steam") != -1) or (statement.find("стим") != -1)):
                        self.osrun('C:\\Program Files (x86)\\Steam\\Steam.exe')
                    if ((statement.find("discord") != -1) or (statement.find("дискорд") != -1)):
                        self.osrun('C:\\Users\\dimab\\AppData\\Local\\Discord\\app-0.0.305\\Discord.exe')

                    # Команды для открытия URL в браузере

                    if (((statement.find("youtube") != -1) or (statement.find("youtub") != -1) or (
                            statement.find("ютуб") != -1) or (statement.find("you tube") != -1)) and (
                            statement.find("смотреть") == -1)):
                        self.openurl('http://youtube.com', 'Открываю херню, куда все заливаю свои видосы')

                    if (((statement.find("новости") != -1) or (statement.find("новость") != -1) or (
                            statement.find("на усть") != -1)) and (
                            (statement.find("youtube") == -1) and (statement.find("youtub") != -1) and (
                            statement.find("ютуб") == -1) and (statement.find("you tube") == -1))):
                        self.openurl('https://www.rbc.ua/ukr', 'Посмотри новости!')

                    if ((statement.find("почту") != -1) or (statement.find("gmail") != -1)):
                        self.openurl('https://mail.google.com/mail/u/0/?tab=wm#inbox/', 'Открываю почту')

                    if ((statement.find("инстаграм") != -1) or (statement.find("инсту") != -1)):
                        self.openurl('https://www.instagram.com/p/B_5Pt5pHw8b/',
                                     'Люблю Лерочку, она самая красивая девушка!')

                    # Команды для поиска в сети интернет

                    if ((statement.find("найти") != -1) or (statement.find("поиск") != -1) or (
                            statement.find("найди") != -1) or (statement.find("дайте") != -1) or (
                            statement.find("mighty") != -1)):
                        statement = statement.replace('найди', '')
                        statement = statement.replace('найти', '')
                        statement = statement.strip()

                        self.openurl('https://www.google.com/search?q=' + statement, "Я нашла следующую информацию")

                    # Переделать
                    if ((statement.find("смотреть") != -1) and (
                            (statement.find("фильм") != -1) or (statement.find("сериал") != -1))):
                        statement = statement.replace('посмотреть', '')
                        statement = statement.replace('смотреть', '')
                        statement = statement.replace('хочу', '')
                        statement = statement.replace('фильм', '')
                        statement = statement.replace('сериал', '')
                        statement = statement.strip()
                        self.openurl('https://kinoprofi.vip/search/f:' + statement, "Приятного просмотра")

                    if (((statement.find("youtube") != -1) or (statement.find("ютуб") != -1) or (
                            statement.find("you tube") != -1)) and (statement.find("смотреть") != -1)):
                        statement = statement.replace('хочу', '')
                        statement = statement.replace('на ютубе', '')
                        statement = statement.replace('на ютуб', '')
                        statement = statement.replace('на youtube', '')
                        statement = statement.replace('на you tube', '')
                        statement = statement.replace('на youtub', '')
                        statement = statement.replace('youtube', '')
                        statement = statement.replace('ютуб', '')
                        statement = statement.replace('ютубе', '')
                        statement = statement.replace('посмотреть', '')
                        statement = statement.replace('смотреть', '')
                        statement = statement.strip()
                        self.openurl('http://www.youtube.com/results?search_query=' + statement,
                                     'Ищу в той херне, где много видосов')

                    # Music
                    if ((statement.find("слушать") != -1) and (statement.find("песн") != -1)):
                        statement = statement.replace('песню', '')

                        statement = statement.replace('песни', '')
                        statement = statement.replace('песня', '')
                        statement = statement.replace('песней', '')
                        statement = statement.replace('послушать', '')
                        statement = statement.replace('слушать', '')
                        statement = statement.replace('хочу', '')
                        statement = statement.strip()

                        self.openurl('https://soundcloud.com/search?q=' + statement, "Устрой дискотеку, братан")

                    # Поддержание диалога

                    if ((statement.find("закройся") != -1) or (statement.find("пока") != -1)):
                        answer = "Иди нахуй"
                        self.say(answer)

                        while pygame.mixer.music.get_busy():
                            time.sleep(0.1)
                        sys.exit()

                    print("Вы сказали: {}".format(statement))

                except sr.UnknownValueError:
                    print("Упс! Кажется, я тебя не поняла, повтори еще раз")
                except sr.RequestError as e:
                    print("Не могу получить данные от сервиса Google Speech Recognition; {0}".format(e))
        except KeyboardInterrupt:
            self._clean_up()
            print("Пока!")

    def osrun(self, cmd):
        PIPE = subprocess.PIPE
        p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT)

    def openurl(self, url, ans):
        webbrowser.open(url)
        self.say(str(ans))
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

    def say(self, phrase):
        tts = gTTS(text=phrase, lang="ru")
        tts.save(self._mp3_name)

        # Play answer
        mixer.music.load(self._mp3_name)
        mixer.music.play()
        if (os.path.exists(self._mp3_nameold)):
            os.remove(self._mp3_nameold)

        now_time = datetime.datetime.now()
        self._mp3_nameold = self._mp3_name
        self._mp3_name = now_time.strftime("Drop\\%d%m%Y%I%M%S") + ".mp3"

    def _clean_up(self):
        def clean_up():
            os.remove(self._mp3_name)


def main():
    ai = Speech_AI()
    ai.work()


main()
input()
