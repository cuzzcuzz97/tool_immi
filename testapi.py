try:
    import requests
    from datetime import datetime
    from dotenv import load_dotenv
    import os
    load_dotenv()
    API_KEY_MAIN_CHANNEL = os.getenv('API_MAIN_KEY')
    API_KEY_STATUS_CHANNEL = os.getenv('API_STATUS_KEY')
except:
    os.system('pip3 install -r requirements.txt')

URL_SET_WEBHOOK = "https://chatapi.viber.com/pa/set_webhook"
def running(message,channel_selection):
    if channel_selection == 'status':
        api_key = API_KEY_STATUS_CHANNEL
    elif channel_selection == 'error':
        api_key = API_KEY_MAIN_CHANNEL
    else:
        api_key = API_KEY_MAIN_CHANNEL
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {
        "auth_token": api_key,
        "url":"https://chatapi.viber.com/pa/set_webhook",
    }

    response = requests.post(URL_SET_WEBHOOK, headers=headers, json=params)
    # print(response.json())
    # info 
    URL_INFO = 'https://chatapi.viber.com/pa/get_account_info'

    params_get_info = {
        "auth_token": api_key,
    }
    get_response = requests.post(URL_INFO, headers=headers, json=params_get_info)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    # send messages 
    URL_SEND_MESSAGE = 'https://chatapi.viber.com/pa/post'
    if message == 'success':
        message_send = f"IMMI mở kìa anh em , thoi gian : {current_time}"
        id_room = 'fu3sTymjh0Vkt6cqCSXQEg=='
    elif channel_selection =='error':
        message_send = message
        id_room = 'fu3sTymjh0Vkt6cqCSXQEg=='
    else:
        message_send = message
        id_room = 'OteXpRI/MBq7x8DYm1rmjA=='

    params_sendmessage = {  
        "auth_token": api_key,
        "from": id_room, 
        "type": "text", 
        "text": message_send
    }
    get_response_message = requests.post(URL_SEND_MESSAGE, headers=headers, json=params_sendmessage)


    