try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    import os
    import time
    from testapi import running
    from datetime import datetime
    import pytz
    tz = pytz.timezone('Asia/Bangkok')
    from dotenv import load_dotenv
    import requests
    # from send_tele_message import send_message
    load_dotenv()
except Exception as e:
    print(e)
    # os.system('nohup python3 immitest.py -u &')

import os 
from dotenv import load_dotenv
load_dotenv()
import requests

API_KEY = os.getenv('API_TELEGRAM')
chat_id = os.getenv("CHAT_ID_KEY")
baotinhtrang = os.getenv("baotinhtrang")
baomo = os.getenv("baomo")
message = "Hello, world!"

def send_message(message,chat_id):
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

try:
    username = os.getenv('USERNAME_IMMI')
    password = os.getenv('PASSWORD_IMMI')
    baotinhtrang = os.getenv('baotinhtrang')
    baomo = os.getenv('baomo')
    #username = 'changhapham9@gmail.com'
    data = {
        'username' :username,
        'password' :password,
    }
    send_message(f'Khởi chạy lại phần mềm',baotinhtrang)
except Exception as e:
    print(e)
    # os.system('nohup python3 immitest.py -u &')

def download_audio_banmai():
    time.sleep(4)
    options = Options()
    options.add_argument("headless")
    # options.add_experimental_option("detach", True)
    # web = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    # options = webdriver.ChromeOptions()
    # options.add_argument("--disable-dev-shm-usage")
    web = webdriver.Chrome(options=options)
    # web = webdriver.Chrome()
    web.get('https://online.immi.gov.au/')
    username = web.find_element('xpath','//*[@id="username"]')
    username.send_keys(data['username'])
    password = web.find_element('xpath','//*[@id="password"]')
    password.send_keys(data['password'])
    login = web.find_element('xpath','/html/body/form/div/div[2]/button[2]')
    login.click()
    continue_btn = web.find_element('xpath','/html/body/form/div/div/button')
    continue_btn.click()
    while True:
        try:
            application_edit = web.find_element('xpath','//*[@id="defaultActionPanel_0_1"]')
            application_edit.click()
        except:
            ...
        try:
            continue_btn_page1 = web.find_element('xpath','//button[@title="Go to next page"]')
            time.sleep(1)
            step = web.find_element('xpath',"//*[contains(text(), '/16')]")
            if step.text == '4/16':
                break
            continue_btn_page1.click()
        except:
            ...
        try:
            warning = web.find_element('xpath',"//*[contains(text(), 'An error has occurred')]")
            break
        except:
            ...
    warning = 'yes'
    while len(warning) > 2:
        try:
            print('enter checking mode')
            now = datetime.now()
            formatted_datetime = now.strftime('Ngày %d tháng %m năm %Y thời gian %H:%M:%S')
            continue_btn_page1 = web.find_element('xpath','//button[@title="Go to next page"]')
            continue_btn_page1.click()
            step = web.find_element('xpath',"//*[contains(text(), '/16')]")
            print('step: ', step.text)
            if step.text == '4/16':
                print('sending message')
                send_message(f'V1.2 \U0000274C Trang {step.text} : {formatted_datetime}',baotinhtrang)
                running(f'V1.2 Trang {step.text} : {formatted_datetime}','status')
                time.sleep(3)
            if step.text != '4/16':
                break
            try:
                warning = web.find_element('xpath',"//*[contains(text(), 'An error has occurred')]")
            except:
                break
            # print(warning.text)
            # print('****************')
            # print('not open')
            # print('****************')
            # print("Current Time =", formatted_datetime)
            time.sleep(30)
            warning = 'yes'
        except Exception as e:
            print(e)
            break
    if step.text == '5/16':
        print('step: ', step.text)
        for i in range(40):
            running('success','not status')
            send_message(f'\U00002705\U00002705\U00002705Trang 5 kìa vô mau vô mau : {formatted_datetime}\U00002705\U00002705\U00002705',baomo)
            time.sleep(3)
        time.sleep(60)
        return download_audio_banmai()
        # os.system('nohup python3 immitest.py -u &')
    else:
        send_message(f'\U00002705xảy ra sự cố chờ trong giây lát\U00002705',baotinhtrang)
        running(f'xảy ra sự cố chờ trong giây lát ','status')
        # running(f'xảy ra sự cố , gọi admin để fix gấp ','error')
        time.sleep(60)
        return download_audio_banmai()
        # os.system('nohup python3 immitest.py -u &')
try:
    download_audio_banmai()
except Exception as e:
    print(e)
    send_message(f'\U00002705xảy ra sự cố chờ trong giây lát\U00002705',baotinhtrang)
    running(f'xảy ra sự cố chờ trong giây lát ','status')
    # running(f'xảy ra sự cố , gọi admin để fix gấp ','error')
    time.sleep(10)
    download_audio_banmai()
    # os.system('nohup python3 immitest.py -u &')

