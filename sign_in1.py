import requests

def pushplus_notification(token, title, content):
    url = 'http://www.pushplus.plus/send'
    headers = {
        "Content-Type": "application/json",
    }
    payload = {
        "token": token,  # 替换为你的 PushPlus Token
        "title": title,
        "content": content,
        "template": "json"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# 示例用法
if __name__ == "__main__":
    token = "725f8c0c40f645fdb50c3ba3a4d306e7"  # 替换为你的 PushPlus Token
    title = "测试推送"
    content = "这是一条测试消息"
    result = pushplus_notification(token, title, content)
    print(result)
