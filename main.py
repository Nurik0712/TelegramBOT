import requests
import random
import telebot
from bs4 import BeautifulSoup as b
URL = "https://www.anekdot.ru/random/anekdot/"
API_KEY = '5243818570:AAETX2_VS-wuSwcyvp0jf8320QxFXg5bdFw'
def parser(url):
    r = requests.get(url)
    soup = b(r.text, "html.parser")
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]

list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['начать'])

def hello(message):
    bot.send_message(message.chat.id, "Здарова. Что бы здохнуть от кринжа введи цифру от 1 до 10:")

@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'Далбаеб введи цифры')
bot.polling()