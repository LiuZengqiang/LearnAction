import os
import requests


def send_pushme_notification():
    url = "https://push.i-i.me"

    payload = {
        "push_key": os.environ["PUSH_KEY"],
        "title": "测试标题",
        "content": "测试内容",
        "type": "text",
        "date": "date",
    }

    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "user-agent": "GitHubActions",
    }

    response = requests.post(url, headers=headers, data=payload)
    print(response.status_code)
    print(response.text)


if __name__ == "__main__":
    send_pushme_notification()
