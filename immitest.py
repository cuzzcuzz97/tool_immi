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

username = os.getenv('USERNAME_IMMI')
password = os.getenv('PASSWORD_IMMI')
baotinhtrang = os.getenv('baotinhtrang')
baomo = os.getenv('baomo')
# username = 'changhapham9@gmail.com'
data = {
    'username' :username,
    'password' :password,
}

def download_audio_banmai():
    os.system('pkill chrome')
    send_message(f'Khởi chạy lại phần mềm',baotinhtrang)
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument("--disable-gpu")
    options.add_argument('--disable-dev-shm-usage')
    # options.add_argument("headless")
    # options.add_experimental_option("detach", True)
    # web = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    # options = webdriver.ChromeOptions()
    # options.add_argument("--disable-dev-shm-usage")
    web = webdriver.Chrome(options=options)
    # web = webdriver.Chrome()
    web.get('https://online.immi.gov.au/')
    try:
        username = web.find_element('xpath','//*[@id="username"]')
        username.send_keys(data['username'])
        password = web.find_element('xpath','//*[@id="password"]')
        password.send_keys(data['password'])
        login = web.find_element('xpath','/html/body/form/div/div[2]/button[2]')
        login.click()
        continue_btn = web.find_element('xpath','/html/body/form/div/div/button')
        continue_btn.click()
    except:
        web.close()
        os.system('pkill chrome')
        return download_audio_banmai()
    try:
        step_2 = False
        while True:
            time.sleep(4)
            if not step_2:
                try:
                    time.sleep(4)
                    application_edit = web.find_element('xpath','//*[@id="defaultActionPanel_0_1"]')
                    application_edit.click()
                except:
                    web.get('https://online.immi.gov.au/')
                    myapplicant_btn = web.find_element('xpath','/html/body/form/div[1]/button[1]')
                    myapplicant_btn.click()
                    time.sleep(4)
                    try:
                        application_edit = web.find_element('xpath','//*[@id="defaultActionPanel_0_1"]')
                        application_edit.click()
                    except:
                        ...
            try:
                time.sleep(2)
                now = datetime.now()
                formatted_datetime = now.strftime('Ngày %d tháng %m năm %Y thời gian %H:%M:%S')
                continue_btn_page1 = web.find_element('xpath','//button[@title="Go to next page"]')
                step = web.find_element('xpath',"//*[contains(text(), '/16')]")
                print(f'trang : {step.text}')
                time.sleep(1)
                if step.text == '4/16':
                    send_message(f'v1.3 \U0000274C Trang {step.text} : {formatted_datetime}',baotinhtrang)
                elif step.text == '5/16':
                    for i in range(40):
                        now = datetime.now()
                        formatted_datetime = now.strftime('Ngày %d tháng %m năm %Y thời gian %H:%M:%S')
                        # running('success','not status')
                        send_message(f'\U00002705\U00002705\U00002705Trang 5 kìa vô mau vô mau : {formatted_datetime}\U00002705\U00002705\U00002705',baomo)
                        send_message(f'\U00002705\U00002705\U00002705Trang 5 kìa vô mau vô mau : {formatted_datetime}\U00002705\U00002705\U00002705',baotinhtrang)
                        # send_message(f'test app mn thong cam {formatted_datetime}',baotinhtrang)
                        time.sleep(1)
                continue_btn_page1.click()
                step_2 = True
            except Exception as e:
                print(e)
                web.get('https://online.immi.gov.au/')
                step_2 = False
                time.sleep(4)
    except Exception as e2:
        print(e2)
        time.sleep(2)
        web.close()
        os.system('pkill chrome')
        return download_audio_banmai()
    # if step.text == '5/16':
    #     print('step: ', step.text)
        # for i in range(40):
        #     running('success','not status')
        #     # send_message(f'\U00002705\U00002705\U00002705Trang 5 kìa vô mau vô mau : {formatted_datetime}\U00002705\U00002705\U00002705',baomo)
        #     send_message(f'test app mn thong cam',baotinhtrang)
        #     time.sleep(1)
    #     time.sleep(10)
    #     return download_audio_banmai()
    # else:
    #     send_message(f'\U00002705xảy ra sự cố chờ trong giây lát\U00002705',baotinhtrang)
    #     running(f'xảy ra sự cố chờ trong giây lát ','status')
    #     time.sleep(10)
    #     return download_audio_banmai()
while True:
    try:
        download_audio_banmai()
    except Exception as open_f_error:
        os.system('pkill chrome')
        print(open_f_error)
        time.sleep(5)
        os.system('killall python3')
        os.system('nohup python3 immitest.py -u &')
        break