import json
import time
import hashlib
import hmac
import base64
import uuid

def signed_header(token, secret):
    nonce = uuid.uuid4()
    t = int(round(time.time() * 1000))
    string_to_sign = '{}{}{}'.format(token, t, nonce)

    string_to_sign = bytes(string_to_sign, 'utf-8')
    secret = bytes(secret, 'utf-8')

    sign = base64.b64encode(hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())

    header = {}
    header['Authorization']=token
    header['Content-Type']='application/json'
    header['charset']='utf8'
    header['t']=str(t)
    header['sign']=str(sign, 'utf-8')
    header['nonce']=str(nonce)

    return header
