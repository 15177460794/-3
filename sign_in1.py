import requests
import time
# 获取 token 的函数
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
    return response.json()['data']['token']  # 返回从响应中提取的 token

# 签到的函数
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
    return response.json()  # 返回签到响应的 JSON 数据

# PushPlus 推送通知的函数
async def pushplus_notification(message):
    url = 'http://www.pushplus.plus/send'
    headers = {
        "Content-Type": "application/json",
    }
    payload = {
        "token": "725f8c0c40f645fdb50c3ba3a4d306e7",  # 替换为你的 PushPlus Token
        "title": "签到通知",
        "content": message,
        "template": "json"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# 主函数，异步执行
async def main():
    token = get_token()  # 获取 token
    print('token:', token)
    await push(f'获取到 token: {token}')  # 推送获取到的 token
    await pushplus_notification(f'获取到 token: {token}')  # PushPlus 推送获取到的 token
    time.sleep(5)  # 等待 5 秒
    data = sign_in(token)  # 签到
    print('message:', data['message'])
    await push(f'签到结果: {data["message"]}')  # 推送签到结果
    await pushplus_notification(f'签到结果: {data["message"]}')  # PushPlus 推送签到结果

# 程序入口
if __name__ == "__main__":
    asyncio.run(main())  # 运行主函数
