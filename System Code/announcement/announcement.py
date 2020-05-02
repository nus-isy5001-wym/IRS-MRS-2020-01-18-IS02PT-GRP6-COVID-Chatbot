import sys
import django
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

os.environ.setdefault('DJANGO_SETTING_MODULE', 'ChatBot_Main.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ChatBot_Main.settings'
django.setup()

from chatbot_app.models import userList
import requests
import json
from bs4 import BeautifulSoup
import time

user_list = list(userList.objects.all().values())
print(user_list)

with open('message.txt',encoding="utf8") as file:  
    msg = file.read()

with open('bot_token.txt',encoding="utf8") as file:  
    token = file.read()

counter = 0
for item in user_list:
    if item['subscribe'] == True:
        user_name = item['first_name']
        chat_id = item['chat_ID']
        announcement_text = ""
        announcement_text += f"Hello, {user_name}\n\n" + msg
        a = requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={announcement_text}')
        counter += 1
        print(f'{counter} message sent. Response: {a}')
