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
       "account": "221020830107",
        "password": "330577415@Ryj",
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
        "address": "广东省广州市天河区APM线",
        "province": "广东省",
        "city": "广州市",
        "latitude": "yjE7UWHPf3Rd21pPp8WKghp0LUgeKLGybPbgGerlX1/89RxeNLvpjLDzhdpUtbbrM0Rwj0GT4Err\nXNShWKQrJ8QoCp/dbnqStw62A2bFt9hPtD0myGHI6NaSfWeDdVHP5wKZRNdtGxtJTF4fSLVs42ie\nKkLYkz64P0ipTmiUBkE=\n",
        "remark": "0",
        "comment": "",
        "address_name": "黄埔大道(地铁站)",
        "change_sign_resource": "0",
        "longitude": "LF81jHnOPdqgrcvW8sSTfLRtxoaI5vcgsxhZ06IepCfDLkX5t36JwipHOOXmbUClZvhYM4feOcFw\nRVdflYbZGFkTqj5CwlzdhuXV2f6l9jKwUH3PgcBvdzVdD5LF6N6pr/+0tKvPkqqTabQZNKc2qNpn\n+BUXr4nNU1DJGzCGWzs=\n"
    }
    response = requests.post(url, params=params, data=payload, headers=headers)
    return response.json()

def send_pushplus_message(token, title, content):
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
    token = get_token()
    print('token:', token)
    time.sleep(5)
    data = sign_in(token)
    print('message:', data['message'])

    # 发送 PushPlus 消息
    pushplus_token = '725f8c0c40f645fdb50c3ba3a4d306e7'
    title = '签到结果'
    content = f"签到消息: {data['message']}"
    pushplus_response = send_pushplus_message(pushplus_token, title, content)
    print('PushPlus response:', pushplus_response)
