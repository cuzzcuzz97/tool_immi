import os 
import telebot
from dotenv import load_dotenv
load_dotenv()
import requests

API_KEY = os.getenv('API_TELEGRAM')
chat_id = os.getenv("CHAT_ID_KEY")
message = "Hello, world!"
def send_message(message,chat_id=chat_id):
    url = f"https://api.telegram.org/bot{API_KEY}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Error sending message:", response.status_code)


send_message("\U0000274C fuck you")