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
        },{
            "account": "221020430147",
            "password": "$qaQ201030",
            "school_id": "267",
            "address": "广东省珠海市斗门区珠海冠宇集团南园区(北门)附近",
            "province": "广东省",
            "city": "珠海市",
            "latitude": "IgLOdsjHzVhklQlwdLJ558PkEOmNu73PDGn1uH8lONt1J+OrOI5qmgs7tNa3Gj+GTaYX+D8lJilF\n5HiW4YoCt9DWWz8h6SryfYreUInYD5Oa9+0a0ln6dOaXSewY9rq28voiKDldsqfy+k1RgGOb7y1M\nQbXdlVb/MKGhdNQbSFU=\n",
            "longitude": "hZDbVFV2/AcRj3FpU/VIPZSAWQu653Gh+qBNcdQLmBemnf72rbC5Q+nl/yWElbYaSBDXRkBkZZm/\nBTTS4L9oL7WteG3BomuYkdxIDp4EJInh1MQn0fcdP99EXgZgsu7HCmDCjmY2vfIj+KvNYr4PaPnn\nRpLpqgIlNl9DqEuTmes=\n",
            "address_name": "珠海冠宇七厂一期北丰巢柜",
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
            "latitude": "Nq+4e/CepdPvPDOe0CfdBEbqU0BRJJG3av6JGlRxV/WjFc/2XG1uTc2A6lgnrFYXz3X/SODMeH6e
yrueixIz6LjBdhjeioZuK+a2WrrXsiLBVW8IU8J1kMsIcusyXgJOtzF41/JGwFPEu3Kcq2QaMWHD
h5yj1S4lbmgeSU7TPBo=",
            "longitude": "XKCtKhu3cgW6RCrr9tVs/csm/KCIRhbTDsbdAmuMZEoJ5iEVoZSSZg39NJPpZAHJJzfJbR5KIdpM
dT2SbopSs+ySeuDQKI7P4arQskAFUsObR5KVHx94bttKvVPGJYxfsES0RuTqJjN30gx2dBBWdXD5
fgXf8ZFWK/9kzXIaNiA=",
            "address_name": "广西北流华生瓷业有限责任公司",
            "pushplus_token": "7861c1489c324e74b5fd7334e5a1b728"
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
