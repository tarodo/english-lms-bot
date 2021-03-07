import requests
from data.config import API_ADDRESS
from .auth import API_TOKEN

WORDSET_URL = API_ADDRESS + 'trainer/wordsets/'


class WordSet:
    def __init__(self, name, set_id):
        self.name = name
        self.id = set_id


class WordSetList:
    def __init__(self, wordset_db: list = None):
        self.sets = []
        self.page_step = 3
        if wordset_db:
            for wset in wordset_db:
                self.sets.append(WordSet(name=wset['name'], set_id=wset['id']))

    def pages(self):
        """Return count of pages"""
        return (len(self.sets) - 1) // self.page_step + 1

    def page(self, page_number: int) -> tuple['WordSetList', int, int]:
        """Return one page and bool is previous and next pages exist"""
        first_set = self.page_step * (page_number - 1)
        last_set = self.page_step * (page_number - 1) + self.page_step
        prev_page = 0
        if page_number > 1:
            prev_page = page_number - 1
        next_page = 0
        if page_number < self.pages():
            next_page = page_number + 1
        one_page = WordSetList()
        one_page.sets = self.sets[first_set:last_set]
        return one_page, prev_page, next_page


def auth_head():
    """Create headers part about authorization"""
    return {
        'Authorization': 'Token ' + API_TOKEN
    }


def wordset_create(wordset_name, student_id, **kwargs):
    payload = {
        'name': wordset_name,
        'student': student_id
    }
    payload.update(kwargs)
    res = requests.post(WORDSET_URL, data=payload, headers=auth_head())
    return res.status_code


def wordsets(student_id, **kwargs):
    params = {
        'student': student_id
    }
    params.update(kwargs)
    res = requests.get(WORDSET_URL, params=params, headers=auth_head())
    return WordSetList(res.json())
