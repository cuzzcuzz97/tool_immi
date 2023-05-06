try:
    from selenium import webdriver
    import os
    import time
    from testapi import running
    from datetime import datetime
    import pytz
    tz = pytz.timezone('Asia/Bangkok')
    from dotenv import load_dotenv
    import telebot
    import requests
    from send_tele_message import send_message
    load_dotenv()
except:
    os.system('nohup python3 immg.py -u &')
    os.system('pip3 install -r requirements.txt')

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
    os.system('nohup python3 immg.py -u &')

def download_audio_banmai():
    time.sleep(4)
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.addArguments("--disable-dev-shm-usage")
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
    application_edit = web.find_element('xpath','//*[@id="defaultActionPanel_0_1"]')
    application_edit.click()
    # page 1
    print('step step')
    continue_btn_page1 = web.find_element('xpath','//button[@title="Go to next page"]')
    continue_btn_page1.click()
    # page 2
    continue_btn_page1 = web.find_element('xpath','//button[@title="Go to next page"]')
    continue_btn_page1.click()
    # page 3
    continue_btn_page1 = web.find_element('xpath','//button[@title="Go to next page"]')
    continue_btn_page1.click()
    # page 4
    continue_btn_page1 = web.find_element('xpath','//button[@title="Go to next page"]')
    continue_btn_page1.click()
    warning = 'yes'
        
    while len(warning) > 2:
        try:
            now = datetime.now()
            formatted_datetime = now.strftime('Ngày %d tháng %m năm %Y thời gian %H:%M:%S')
            step = web.find_element('xpath',"//*[contains(text(), '/16')]")
            # print('step: ', step.text)
            if step.text == '4/16':
                print('sending message')
                send_message(f'\U0000274C Trang {step.text} : {formatted_datetime}',baotinhtrang)
                running(f'Trang {step.text} : {formatted_datetime}','status')
            warning = web.find_element('xpath',"//*[contains(text(), 'An error has occurred')]")
            # print(warning.text)
            # print('****************')
            # print('not open')
            # print('****************')
            # print("Current Time =", formatted_datetime)
            time.sleep(20)
            continue_btn_page1 = web.find_element('xpath','//button[@title="Go to next page"]')
            continue_btn_page1.click()
            time.sleep(4)
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
        os.system('nohup python3 immg.py -u &')
    else:
        send_message(f'\U00002705xảy ra sự cố chờ trong giây lát\U00002705',baotinhtrang)
        running(f'xảy ra sự cố chờ trong giây lát ','status')
        # running(f'xảy ra sự cố , gọi admin để fix gấp ','error')
        time.sleep(60)
        os.system('nohup python3 immg.py -u &')
try:
    download_audio_banmai()
except Exception as e:
    print(e)
    send_message(f'\U00002705xảy ra sự cố chờ trong giây lát\U00002705',baotinhtrang)
    running(f'xảy ra sự cố chờ trong giây lát ','status')
    # running(f'xảy ra sự cố , gọi admin để fix gấp ','error')
    time.sleep(60)
    os.system('nohup python3 immg.py -u &')

