import requests
from data.config import API_ADDRESS
from .auth import API_TOKEN

STUDENTS_URL = API_ADDRESS + 'trainer/students/'


def auth_head():
    """Create headers part about authorization"""
    return {
        'Authorization': 'Token ' + API_TOKEN
    }


def is_student_exists(tg_id):
    """Check api for student existing"""
    params = {
        'tg_id': tg_id
    }
    headers = auth_head()
    res = requests.get(STUDENTS_URL, params=params, headers=headers)
    if res.status_code == 200 and len(res.json()) == 0:
        return False
    return True


def student_registration(tg_id, **kwargs):
    """Register new student. Return status of a request, or -1 if student exists"""
    if not is_student_exists(tg_id):
        payload = {
            'tg_id': tg_id
        }
        payload.update(kwargs)
        headers = auth_head()
        res = requests.post(STUDENTS_URL, data=payload, headers=headers)
        return res.status_code
    else:
        return -1

