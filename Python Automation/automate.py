# Send good morning message to a mobile number every day or every morning
# For this, we need to install a library called "schedule" and another library called "requests".
# Also, check out the textbelt.com website

import requests
from credentials import mobile_number
import schedule
import time


def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': mobile_number,
        'message': 'Hola, Good evening. Me: Python',
        'key': 'textbelt'
    })
    print(resp.json())


# schedule.every().day.at('18:00').do(send_message)

schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
