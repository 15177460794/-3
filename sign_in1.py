import requests
import time
from datetime import datetime

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
    
    # 判断当前日期是周几
    current_day = datetime.now().weekday()
    if current_day < 5:  # 周一到周五
        remark = "0"
    else:  # 周末
        remark = "14"
    
    payload = {
        "address": address,
        "province": province,
        "city": city,
        "latitude": latitude,
        "remark": remark,
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
    users =  [
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
        },{
            "account": "221020430147",
            "password": "$qaQ201030",
            "school_id": "267",
            "address": "广东省广州市天河区APM线",
            "province": "广东省",
            "city": "广州市",
            "latitude": "yjE7UWHPf3Rd21pPp8WKghp0LUgeKLGybPbgGerlX1/89RxeNLvpjLDzhdpUtbbrM0Rwj0GT4Err\nXNShWKQrJ8QoCp/dbnqStw62A2bFt9hPtD0myGHI6NaSfWeDdVHP5wKZRNdtGxtJTF4fSLVs42ie\nKkLYkz64P0ipTmiUBkE=\n",
            "longitude": "LF81jHnOPdqgrcvW8sSTfLRtxoaI5vcgsxhZ06IepCfDLkX5t36JwipHOOXmbUClZvhYM4feOcFw\nRVdflYbZGFkTqj5CwlzdhuXV2f6l9jKwUH3PgcBvdzVdD5LF6N6pr/+0tKvPkqqTabQZNKc2qNpn\n+BUXr4nNU1DJGzCGWzs=\n",
            "address_name": "黄埔大道(地铁站)",
            "pushplus_token": "d298beb43ca54592b7311eab59520d89"
            
        },{
            "account": "221020830124",
            "password": "asdDSA123@",
            "school_id": "267",
            "address": "广东省广州市天河区黄埔大道西33号(近地铁体育西站、公交天河站)",
            "province": "广东省",
            "city": "广州市",
            "latitude": "DqdC68NRG1bXwgOJ2+Kb2YDcw7Pu5GMbdIaQda7W92P/LFHK0aQxHfDum9qHDvKaE/8i2PanYumi\nmdv7REGg3TWhIP5s256kNZLSz68lNJQ7dhYIhrL8Sxyp0t+s04AIpKkFOVOkmt6g3mac34Y7Mdca\n/ep1PlRWc8djsVAQSA4=\n",
            "longitude": "dlkEcEcZAsVToGb1m01iHjhSP0q53MyZQg/M+hXairAdd2LFKHopLaUvk3cnomizgzjM2hQcUad1\nZTtOgYhMvSm//xWjVtcKCEMCSLglWc5hkJI00ohyu41FaR/oKV/PKamYHntNsstiPrDuPoea78vF\nQYQxCzCm6owCMwxEPfA=\n",
            "address_name": "三新大厦",
            "pushplus_token": "725f8c0c40f645fdb50c3ba3a4d306e7"
            
        },{
            "account": "221020830128",
            "password": "qQ2782363488.",
            "school_id": "267",
            "address": "广西壮族自治区玉林市北流市靠近广西北流华生瓷业有限责任公司",
            "province": "广西壮族自治区",
            "city": "玉林市",
            "latitude": "Nq+4e/CepdPvPDOe0CfdBEbqU0BRJJG3av6JGlRxV/WjFc/2XG1uTc2A6lgnrFYXz3X/SODMeH6eyrueixIz6LjBdhjeioZuK+a2WrrXsiLBVW8IU8J1kMsIcusyXgJOtzF41/JGwFPEu3Kcq2QaMWHDh5yj1S4lbmgeSU7TPBo=",
            "longitude": "XKCtKhu3cgW6RCrr9tVs/csm/KCIRhbTDsbdAmuMZEoJ5iEVoZSSZg39NJPpZAHJJzfJbR5KIdpMdT2SbopSs+ySeuDQKI7P4arQskAFUsObR5KVHx94bttKvVPGJYxfsES0RuTqJjN30gx2dBBWdXD5fgXf8ZFWK/9kzXIaNiA=",
            "address_name": "广西北流华生瓷业有限责任公司",
            "pushplus_token": "7861c1489c324e74b5fd7334e5a1b728"
        },{
            "account": "221050530111",
            "password": "Fanyijun1212@",
            "school_id": "267",
            "address": "广东省惠州市惠城区和畅六路37号靠近罗格朗智能电气(惠州)有限公司宿舍区",
            "province": "广东省",
            "city": "惠州市",
            "latitude": "Q77arll5f+6Fwz/aRVeMWRteMFdR+qhhcKE7nOEhxsCdx+aInj2IPnYA2tSCMWcVgoR1wK4lt0mnnfNG3moIgxqJowoFmOzxFe6CLtdtZKkXLdq3zZ3Fxnw896J96ZTh8tgvBCAGmzxfptdXUqHDmZk7A56IQwUGY5/9Komxgm8=",
            "longitude": "aKqdXsA6ceHzNQy05wfnnwKtwH7WAEPO/cVoBT3UNivHWyA4vsR4NQ/dGa65A0sudxoVS6WajRPxuVAfG/wJVakQLyXTV2mARJpJ7Oe/9X+31IAOaF6MOBEHvyUAQTTLWtrB9JixeIxCDQV/99uFfF1OTYv+VolLXdCSgD7lHp8=",
            "address_name": "罗格朗智能电气(惠州)有限公司宿舍区",
            "pushplus_token": "5deb739ac0a6468fb174ab61738eedf1"
        },{
            "account": "18776572683",
            "password": "asdZXC+123",
            "school_id": "267",
            "address": "广东省江门市台山市水步镇文华C区8号",
            "province": "广东省",
            "city": "江门市",
            "latitude": "Wth/QCi3syKu+pylKdDVdRTOgf5IY62GvhtK+O3c44bx7QesaoXRIiFy1FmjjP2DvrD+Omjz0+KF5OwIGSa6qKQ2fEry8jEWTgh2ohRuihwh2W/zGDPgTK7usLY+sYGfkM4yOGxoUyU+mhdyNVTg+AE+HepFX1BvtcEHavtPJDE=",
            "longitude": "b73GL+ysgsJAJihOa4roQERCrCRMckSxVuCN54p9LR68ic9UQmTGdkFuk9tnjTOxWoTGoSSakeCMXDYoZUZUQhFMHTmjiQEgXBXQEY2G0w5UBNTPgjVQZdEexY1pJs1dl8UoA/yrWpLRCCSTnJijuTXUbDOY0Cx1Sb6XsvWbSNk=",
            "address_name": "广东鸿特精密技术(台山)有限公司",
            "pushplus_token": "a099acd041d94dc896241b56c09d4161"
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
