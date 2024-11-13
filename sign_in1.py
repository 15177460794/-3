import requests
import time


def get_token():
    url = 'https://api.xixunyun.com/login/api'
    params = {
        "version": "5.0.8",
    }
    headers = {
        "User-Agent": "okhttp/3.8.0",
    }
    payload = {
        "account": "学号",
        "password": "密码",
        "request_source": "3",
        "school_id": "267",
    }
    response = requests.post(url, params=params, headers=headers, data=payload)
    return response.json()['data']['token']


def sign_in(token):
    url = 'https://api.xixunyun.com/signin_rsa'
    params = {
        "token": token,
    }
    headers = {
        "User-Agent": "okhttp/3.8.0",
    }
    payload = {
        "address": "广东省惠州市惠城区滨河东路15号靠近展创大厦",
        "province": "广东省",
        "city": "惠州市",
        "latitude": "JlCkFWfvW+5k2bpJMfjUo6cqz361GjTSSifzxR8Zz4nnQOFsNCh8yp6l4Imw5gMcqa2Zg46EXk24XfJiNq23tmajmP6bf84PRbCLR8wVDX9s1lUI4fvfzxPG/Vv02OO74Q1nnlw1Otn57FWYAfC4cpLFmfBauX3JZ1sGp5firpQ=",
        "remark": "0",
        "comment": "",
        "address_name": "展创大厦",
        "change_sign_resource": "0",
        "longitude": "qoRSdAcfSydE7VHFdw2ozgxRAq2LJuV4xecaGiQw1YjOdOjGTloM+BVwlp4+uvj59hmQdIAHtlGAW+rX14E5ld6Rwo51OQ30LsCA+GL85nU1PjCwI9kkvbwqCsG+VISIvoHlXyJZU5AXRgdPY//WvTId/nWALNrkwyl2PNKLZdc="
    }
    response = requests.post(url, params=params, data=payload, headers=headers)
    return response.json()


if __name__ == "__main__":
    token = get_token()
    print('token:', token)
    time.sleep(5)
    data = sign_in(token)
    print('message:', data['message'])
