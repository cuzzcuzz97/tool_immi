import os 
import telebot
from dotenv import load_dotenv
load_dotenv()
import requests

API_KEY = os.getenv('API_TELEGRAM')
CHAT_ID_KEY = os.getenv('CHAT_ID_KEY')
bot = telebot.TeleBot(API_KEY)

user = bot.get_me()

# print(user)
chat_id = CHAT_ID_KEY
url = f"https://api.telegram.org/bot{API_KEY}/getChat?chat_id={chat_id}"
response = requests.get(url)


@bot.message_handler(commands=['hello'])
def greet(message):
    bot.reply_to(message,'Fuck you bitch, what are you looking at')

bot.polling()