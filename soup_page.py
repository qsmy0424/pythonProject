import requests
import json
import time
from bs4 import BeautifulSoup


def scrape_data(url):

    headers = {
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "priority": "u=0, i",
        "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
    }
    data = {'Submit': '%E7%A2%BA%E8%AA%8D'}
    json_data = json.dumps(data)
    response = requests.post(url, data=json_data, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    for item in soup.find_all(class_='item'):
        print(item.a.attrs.get("href") + "，" + item.img.attrs.get("title") + "，" + item.img.attrs.get("src") + "，" + item.date.text)


if __name__ == "__main__":
    i = 101
    while i <= 200:
        time.sleep(1)
        scrape_data(url="https://www.javsee.lol/page/" + str(i))
        i = i + 1
