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

def create_update():
    new_data = {
        'user': 1,
        'content': 'Another new cool update'
    }
    r = requests.post(BASE_URL + END_POINT, data=new_data)
    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text

# print(get_list())
print(create_update())
