import os
import requests
import sb_sign

from dotenv import load_dotenv
load_dotenv()

token = os.getenv('SWITCHBOT_TOKEN')
secret = os.getenv('SWITCHBOT_SECRET')

headers = sb_sign.signed_header(token, secret)
url = "https://api.switch-bot.com/v1.1/devices"
response = requests.get(url, headers=headers)
print(response.text)
