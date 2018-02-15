import requests
import json

BASE_URL = "http://127.0.0.1:8000/"

END_POINT = "api/updates/"


def get_list():
    r = requests.get(BASE_URL + END_POINT)
    print(r.status_code)
    data = r.json()
    for obj in data:
        if obj['id'] == 1:
            r2 = requests.get(BASE_URL + END_POINT + str(obj['id']))
            print(r2.json())
    return data


# print(get_list())
get_list()
