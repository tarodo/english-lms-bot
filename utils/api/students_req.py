import requests
from data.config import API_ADDRESS
from .auth import API_TOKEN

STUDENTS_URL = API_ADDRESS + 'trainer/students/'


def auth_head():
    """Creates headers part about authorization"""
    return {
        'Authorization': 'Token ' + API_TOKEN
    }


def student_id(tg_id):
    """Checks api for student existing. Returns id if it exists"""
    params = {
        'tg_id': tg_id
    }
    headers = auth_head()
    res = requests.get(STUDENTS_URL, params=params, headers=headers)
    if res.status_code == 200:
        if len(res.json()) == 0:
            return None
        else:
            return int(res.json()[0]['id'])
    return None


def student_registration(tg_id, **kwargs):
    """Registers new student. Returns status of a request, or -1 if student exists"""
    if not student_id(tg_id):
        payload = {
            'tg_id': tg_id
        }
        payload.update(kwargs)
        headers = auth_head()
        res = requests.post(STUDENTS_URL, data=payload, headers=headers)
        return res.status_code
    else:
        return -1

