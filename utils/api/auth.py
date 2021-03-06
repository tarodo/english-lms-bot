import requests
from utils.misc.logging import logging

from data.config import AUTH_NAME, AUTH_PASS, API_AUTH_ADDRESS


def give_token():
    payload = {
        'email': AUTH_NAME,
        'password': AUTH_PASS
    }
    logging.info('request token')
    res = requests.post(API_AUTH_ADDRESS, payload)
    if res.status_code == 200:
        return res.json()['token']
    else:
        logging.info(res.text)


API_TOKEN = give_token()
logging.info(API_TOKEN)