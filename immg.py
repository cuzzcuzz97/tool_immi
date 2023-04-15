try:
    from selenium import webdriver
    import os
    import time
    from testapi import running
    from datetime import datetime
    import pytz
    tz = pytz.timezone('Asia/Bangkok')
    from dotenv import load_dotenv
    load_dotenv()
except:
    os.system('pip3 install -r requirements.txt')

username = os.getenv('USERNAME_IMMI')
password = os.getenv('PASSWORD_IMMI')
#username = 'changhapham9@gmail.com'
data = {
    'username' :username,
    'password' :password,
}

def download_audio_banmai():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    web = webdriver.Chrome(options=options)
    # web = webdriver.Chrome()    
    web.get('https://online.immi.gov.au/lusc/login')
    username = web.find_element('xpath','//*[@id="username"]')
    username.send_keys(data['username'])
    password = web.find_element('xpath','//*[@id="password"]')
    password.send_keys(data['password'])
    login = web.find_element('xpath','/html/body/form/div/div[2]/button[2]')
    login.click()
    time.sleep(4)
    continue_btn = web.find_element('xpath','/html/body/form/div/div/button')
    continue_btn.click()
    time.sleep(4)
    application_edit = web.find_element('xpath','//*[@id="defaultActionPanel_0_1"]')
    application_edit.click()
    time.sleep(5)
    # page 1
    continue_btn_page1 = web.find_element('xpath','//button[@title="Go to next page"]')
    continue_btn_page1.click()
    time.sleep(4)
    # page 2
    continue_btn_page1 = web.find_element('xpath','//button[@title="Go to next page"]')
    continue_btn_page1.click()
    time.sleep(4)
    # page 3
    continue_btn_page1 = web.find_element('xpath','//button[@title="Go to next page"]')
    continue_btn_page1.click()
    time.sleep(4)
    # page 4
    continue_btn_page1 = web.find_element('xpath','//button[@title="Go to next page"]')
    continue_btn_page1.click()
    time.sleep(4)
    warning = 'yes'
        
    while len(warning) > 2:
        try:
            now = datetime.now()
            formatted_datetime = now.strftime('Ngày %d tháng %m năm %Y thời gian %H:%M:%S')
            step = web.find_element('xpath',"//*[contains(text(), '/16')]")
            print('step: ', step.text)
            if step.text == '4/16':
                print('sending message')
                running(f'Trang {step.text} : {formatted_datetime}','status')
            warning = web.find_element('xpath',"//*[contains(text(), 'An error has occurred')]")
            print(warning.text)
            print('****************')
            print('not open')
            print('****************')
            print("Current Time =", formatted_datetime)
            time.sleep(50)
            continue_btn_page1 = web.find_element('xpath','//button[@title="Go to next page"]')
            continue_btn_page1.click()
            time.sleep(4)
            warning = 'yes'
        except:
            break
    if step.text == '5/16':
        print('step: ', step.text)
        running('success','not status')
        os.system('nohub python3 immg.py -u &')
    else:
        running(f'xảy ra sự cố , gọi admin để fix gấp ','status')
        running(f'xảy ra sự cố , gọi admin để fix gấp ','error')
        os.system('nohub python3 immg.py -u &')
    # output = web.find_element('xpath','//*[@id="tts-audio"]')
    # URL = output.get_attribute('src')
    # return URL
try:
    download_audio_banmai()
except:
    running(f'xảy ra sự cố , gọi admin để fix gấp ','status')
    running(f'xảy ra sự cố , gọi admin để fix gấp ','error')
    os.system('nohub python3 immg.py -u &')
print('openning')
