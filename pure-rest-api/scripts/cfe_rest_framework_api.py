import json
import requests
import os

import time

import sys

ENDPOINT = "http://127.0.0.1:8000/api/status/"
AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"
REGISTER_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"
REFRESH_ENDPOINT = 'http://127.0.0.1:8000/api/auth/refresh/'


headers = {
    "Content-Type": "application/json",
    # "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkZWwiLCJleHAiOjE1MTkyMjYyMTEsImVtYWlsIjoiYWRlbEBnbWFpbC5jb20iLCJvcmlnX2lhdCI6MTUxOTIyNTkxMX0.PmPDvDeSUHEdr0ngjoeL4Vxo_YY0dvLO7o1gI_Z6Lo0",
}

image_path = os.path.join(os.getcwd(), 'logo.jpg')


data = {
    'username': 'adel8',
    'email': 'adel8@gmail.com',
    'password': 'adeladel',
    'password2': 'adeladel',
}


r = requests.post(REGISTER_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()
#['token']

print(token)
#
# headers = {
#     # "Content-Type": "application/json",
#     "Authorization": "JWT " + token,
# }
#
# print(headers)
# post_data = {"content": "updated"}
#
# # sys.exit()
# with open(image_path, 'rb') as img:
#     file_data = {
#         'image': img
#     }
#     # posted_response = requests.post(ENDPOINT, data=post_data, headers=headers, files=file_data)
#     posted_response = requests.put(ENDPOINT + "37/", data=post_data, headers=headers, files=file_data)
#     print(posted_response.text)

# refresh_data = {
#     'token': token
# }
#
# # should wait otherwise we'll get the same token
# time.sleep(1.05)
#
# new_r = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
# new_token = new_r.json()['token']
#
# print("###########################")
#
# print(new_token)





# get_endpoint = ENDPOINT + str(32)
# data = json.dumps({'id': 1234})
# post_data = json.dumps({'content': 'Some random content'})
#
#
# r = requests.get(get_endpoint)
# print(r.text)
# r2 = requests.get(ENDPOINT)
# print(r2.status_code)
#
# post_headers = {
#     'content-type': 'application/json'
# }
# post_response = requests.post(ENDPOINT, data=post_data, headers=post_headers)
# print(post_response.text)



# def do_img(method='get', data={}, is_json=True, img_path=None):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     if img_path is not None:
#         with open(image_path, 'rb') as img:
#             file_data = {
#                 'image': img
#             }
#             r = requests.request(method, ENDPOINT, data=data, files=file_data)
#     else:
#         r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r


# do_img(method='post', data={'user': 1, 'content': ''}, is_json=False, img_path=image_path)
# do_img(method='put',
#        data={'id': 31, 'user': 1, 'content': ''},
#        is_json=False,
#        img_path=image_path)


# def do(method='get', data={}, is_json=True):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r


# do(data={'id': 500})
# do(method='delete', data={'id': 12})
# do(method='post', data={'content': 'new content', 'user': 1})
# do(method='put', data={'id': 20, 'content': '9demet', 'user': 1})
# do(data={'id': 20})

