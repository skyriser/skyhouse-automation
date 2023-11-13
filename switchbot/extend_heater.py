import os
import json
import requests
import sb_sign

from dotenv import load_dotenv
load_dotenv()

token = os.getenv('SWITCHBOT_TOKEN')
secret = os.getenv('SWITCHBOT_SECRET')
device_id = os.getenv('HEATER_DEVICE_ID')

headers = sb_sign.signed_header(token, secret)
url = "https://api.switch-bot.com/v1.1/devices/" + device_id + "/commands"
params = {
    "commandType": "command",
    "command": "press"
}
response = requests.post(url, headers=headers, data=json.dumps(params))
print(response.text)
