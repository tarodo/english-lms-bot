import requests
from data.config import API_ADDRESS
from .auth import API_TOKEN

WORDSET_URL = API_ADDRESS + 'trainer/wordsets/'


def auth_head():
    """Create headers part about authorization"""
    return {
        'Authorization': 'Token ' + API_TOKEN
    }


def wordset_create(wordset_name, **kwargs):
    payload = {
        'name': wordset_name,
        'student': 4
    }
    payload.update(kwargs)
    headers = auth_head()
    res = requests.post(WORDSET_URL, data=payload, headers=headers)
    return res.status_code
