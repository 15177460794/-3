import requests
import time

def get_token(account, password, school_id):
    # 获取登录令牌
    url = 'https://api.xixunyun.com/login/api'
    params = {
        "version": "5.0.8",
    }
    headers = {
        "User-Agent": "okhttp/3.8.0",
    }
    payload = {
        "account": account,
        "password": password,
        "request_source": "3",
        "school_id": school_id,
    }
    response = requests.post(url, params=params, headers=headers, data=payload)
    return response.json()['data']['token']

def sign_in(token, address, province, city, latitude, longitude, address_name):
    # 签到
    url = 'https://api.xixunyun.com/signin_rsa'
    params = {
        "token": token,
    }
    headers = {
        "User-Agent": "okhttp/3.8.0",
    }
    payload = {
        "address": address,
        "province": province,
        "city": city,
        "latitude": latitude,
        "remark": "0",
        "comment": "",
        "address_name": address_name,
        "change_sign_resource": "0",
        "longitude": longitude
    }
    response = requests.post(url, params=params, data=payload, headers=headers)
    return response.json()

def send_pushplus_message(token, title, content):
    # 发送PushPlus消息
    url = 'http://www.pushplus.plus/send'
    data = {
        "token": token,
        "title": title,
        "content": content,
        "template": "html"
    }
    response = requests.post(url, json=data)
    return response.json()

if __name__ == "__main__":
    users = [
        {
            "account": "221020830107",
            "password": "330577415@Ryj",
            "school_id": "2376h2",
            "address": "广东省广州市番禺区惠众街21号靠近香港番禺工商联谊会大厦",
            "province": "广东省",
            "city": "广州市",
            "latitude": "UQWXgG/pTDNcEgohMJfyRftuOZQLTAVG3dMphr++87HDdYurNMwBfR0tugweEqFn0JEpTSomQRxwHxIAZRr9EWWt3wD8cj84efxL5Lnj4ywXfAw9DKdMPfdQ7XM1E3jtEoChUtcAY5gxZ5vt6qw6ZGE565QMHji17+fFFrlICDw=",
            "longitude": "lTDkAl8mMCIVT3njVRSmqVdcBrjGHF1NwKdJMJKAHdsw1GwKvzz2m4TvRk5VsTz66LOshlG/yx6nt7ZwTTZR5LABBOVBJcPILQ+DYsFJUFEMFgATQX2QJxUreW1dWFYLzfgdHVLh/PUmES4eYuLBWUKX5ZRL5D0kju7eiddXstQ=",
            "address_name": "香港番禺工商联谊会大厦",
            "pushplus_token": "725f8c0c40f645fdb50c3ba3a4d306e7"
        }
        # 添加更多用户信息
    ]

    for user in users:
        token = get_token(user["account"], user["password"], user["school_id"])
        print('token:', token)
        time.sleep(5)
        data = sign_in(token, user["address"], user["province"], user["city"], user["latitude"], user["longitude"], user["address_name"])
        print('message:', data['message'])

        # 发送 PushPlus 消息
        title = '签到结果'
        content = f"签到消息: {data['message']}"
        pushplus_response = send_pushplus_message(user["pushplus_token"], title, content)
        print('PushPlus response:', pushplus_response)
1
