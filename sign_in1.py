import requests
import time
from datetime import datetime

def get_token(account, password, school_id):
    url = 'https://api.xixunyun.com/login/api'
    params = {"version": "5.0.8"}
    headers = {"User-Agent": "okhttp/3.8.0"}
    payload = {
        "account": account,
        "password": password,
        "request_source": "3",
        "school_id": school_id,
    }
    response = requests.post(url, params=params, headers=headers, data=payload)
    
    # 打印响应以进行调试
    print(f"获取令牌响应 (账号: {account}):", response.text)
    
    if response.status_code == 200 and 'data' in response.json():
        return response.json()['data']['token']
    else:
        print(f"获取令牌失败 (账号: {account}):", response.json().get('message', 'Unknown error'))
        return None

def sign_in(token, account, address, province, city, latitude, longitude, address_name, remark):
    url = 'https://api.xixunyun.com/signin_rsa'
    params = {"token": token}
    headers = {"User-Agent": "okhttp/3.8.0"}
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
    
    # 打印响应以进行调试
    print(f"签到响应 (账号: {account}):", response.text)
    
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
    users =  [
        {
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
            "password": "Qq2782363488..",
            "school_id": "267",
            "address": "广西壮族自治区玉林市北流市靠近广西北流华生瓷业有限责任公司",
            "province": "广西壮族自治区",
            "city": "玉林市",
            "latitude": "Nq+4e/CepdPvPDOe0CfdBEbqU0BRJJG3av6JGlRxV/WjFc/2XG1uTc2A6lgnrFYXz3X/SODMeH6eyrueixIz6LjBdhjeioZuK+a2WrrXsiLBVW8IU8J1kMsIcusyXgJOtzF41/JGwFPEu3Kcq2QaMWHDh5yj1S4lbmgeSU7TPBo=",
            "longitude": "XKCtKhu3cgW6RCrr9tVs/csm/KCIRhbTDsbdAmuMZEoJ5iEVoZSSZg39NJPpZAHJJzfJbR5KIdpMdT2SbopSs+ySeuDQKI7P4arQskAFUsObR5KVHx94bttKvVPGJYxfsES0RuTqJjN30gx2dBBWdXD5fgXf8ZFWK/9kzXIaNiA=",
            "address_name": "广西北流华生瓷业有限责任公司",
            "pushplus_token": "7861c1489c324e74b5fd7334e5a1b728"
        },{
            "account": "221050530103",
            "password": "Ws530103@",
            "school_id": "267",
            "address": "广东省东莞市东莞市富兴苑东门南210米",
            "province": "广东省",
            "city": "东莞市",
            "latitude": "SwKOHR6R1vjbKmgqkGqe4PwZfK2SJ6pUs6aMruq7w7Le8HfmOKJl/EHHJXAu3+LOOFSxJ6ZbVPCZ\n6DbVvMdIic5wCxQhp4zvnDDD29c3TdRZiKvtz6pm3MIld0L8Ma6gFff04rVCIZyjwNvaPafK2fDs\ndJeFaj5NSw4f9XlMqkI=\n",
            "longitude": "KRANUkebG7Y8wW9WtGOWHL+sbYdnfVvYjOZP3qE1E5sRWvNtLrED0b0bxSl8d/SehpIJpboL5ZWr\n2o5PGFnMn0XAxqEnTslF9kfMzDzjJxlDNBoU8KMHX6V7orwsWwHGj85/KM3YGnJ/4aA2NOfbVpdr\nluylgAcmPxr4DTgu9ac=\n",
            "address_name": "长安汽配广场",
            "pushplus_token": "5deb739ac0a6468fb174ab61738eedf1"
        },{
            "account": "19167045221",
            "password": "Houjiahui123.",
            "school_id": "1597h2",
            "address": "福建省福州市平潭县靠近虎尾楼",
            "province": "福建省",
            "city": "福州市",
            "latitude": "BO/KRLuawpnzat18Q66OyxHpRb6ss/A+mk3pHggHhnbps5gFtxsii7FukCQkBQqKOqazpJuim/8iuuZFqCWNOp0N9UyhF1hpZ2QNKx6WhPNX6UCKAqHFHk5rjV/UDUscJYyf7O6qqCL8YNDlG1CG+sGouKCXy0BR0OMSKgPtcfI=",
            "longitude": "xbUQYB9Pe8amDycAYgAxlYg8xyv3dFLdvmQrc1+0rRsV794XFchSpRrOCbqrQxJ1cqOKQMyvviAM8zG0jzfN1cG2zI+TTAPpI7D4dmaNYrYE4ticT+W5CFQKP7bN1xUy9cjwOWxOx0eap6n7c9IMeiBUhLwmsSY8HM6JcWwwRgA=",
            "address_name": "虎尾楼",
            "pushplus_token": "d1898b30fd0a4773834990c2e264a983"
        },{
            "account": "13706907925",
            "password": "Zqw2034959497.",
            "school_id": "1597h2",
            "address": "福建省漳州市龙海区角美镇东美村南园",
            "province": "福建省",
            "city": "漳州市",
            "latitude": "KDSRLv5qi8y3uUeRAeBW1/8K7zfe9CPnlQkcK5qLfQ/QoFq9yHUewwHP1snphJfbIriB/LnnrUjn66EBCc8JCfsYeota4Vmiqd8vHG+D8gst28mAaUEovrBRCxOk0fvPHAlPzzI6BsQSe4LZt0kVjZR2IC4k86AEWDbjIPUucXs=",
            "longitude": "0twkPSWx3kPqZJOBzW/4lUN5PuY65VWemTWhFGkPDuAbW+OWj2KKtsZ9F+wyovWAiE2Wb9PKaTCby9M+7DSja4SBL89DBtr4M2N2HWE4/plwp4H8EVdhSu4mBk7Hdlua1URR4zUc6MRKwDxcS7Kblph7j+/zkV8ytds08vnTIPs=",
            "address_name": "南园培新幼儿园",
            "pushplus_token": "d1898b30fd0a4773834990c2e264a983"
            }
        # 添加更多用户信息
    ]

    for user in users:
        current_time = datetime.now()
        current_weekday = current_time.weekday()
        current_hour = current_time.hour

        print(f"脚本触发时间: {current_time}")

        if current_weekday >= 5:
            remark = "14"
        else:
            remark = "0" if current_hour < 12 else "8"

        token = get_token(user["account"], user["password"], user["school_id"])
        if token:
            print('token:', token)
            time.sleep(5)
            data = sign_in(token, user["account"], user["address"], user["province"], user["city"], user["latitude"], user["longitude"], user["address_name"], remark)
            print('message:', data['message'])

            title = '签到结果'
            content = f"签到消息: {data['message']}"
            pushplus_response = send_pushplus_message(user["pushplus_token"], title, content)
            print('PushPlus response:', pushplus_response)
        else:
            print(f"获取令牌失败 (账号: {user['account']})")
