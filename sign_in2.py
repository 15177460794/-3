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
            "school_id": "267",
            "address": "广东省广州市天河区APM线",
            "province": "广东省",
            "city": "广州市",
            "latitude": "yjE7UWHPf3Rd21pPp8WKghp0LUgeKLGybPbgGerlX1/89RxeNLvpjLDzhdpUtbbrM0Rwj0GT4Err\nXNShWKQrJ8QoCp/dbnqStw62A2bFt9hPtD0myGHI6NaSfWeDdVHP5wKZRNdtGxtJTF4fSLVs42ie\nKkLYkz64P0ipTmiUBkE=\n",
            "longitude": "LF81jHnOPdqgrcvW8sSTfLRtxoaI5vcgsxhZ06IepCfDLkX5t36JwipHOOXmbUClZvhYM4feOcFw\nRVdflYbZGFkTqj5CwlzdhuXV2f6l9jKwUH3PgcBvdzVdD5LF6N6pr/+0tKvPkqqTabQZNKc2qNpn\n+BUXr4nNU1DJGzCGWzs=\n",
            "address_name": "黄埔大道(地铁站)",
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
