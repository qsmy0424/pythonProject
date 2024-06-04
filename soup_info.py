import urllib

import requests
import json
from urllib.request import urlretrieve
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
    # print(soup)

    container = soup.find('div', {'class': 'container'})
    h3 = container.find('h3').text
    href = container.find('a', {'class': 'bigImage'}).get('href')
    title = container.img.attrs.get("title")
    # print(h3)
    # print(href)
    # print(title)

    code = ''
    date = ''
    time = ''
    author = []
    category = []

    for a in container.find_all('span', {'class': 'genre'}):
        if a.get('onmouseout'):
            author.append(a.a.text)

    for item in container.find('div', {'class': 'col-md-3 info'}).find_all(name='p'):
        # print(item)
        if str(item).__contains__("識別碼"):
            code = item.find_all(name='span')[1].text

        if str(item).__contains__("發行日期"):
            date = item.text

        if str(item).__contains__("長度"):
            time = item.text

        if str(item).__contains__("類別"):
            for sub_item in container.find_all('input', {'name': 'gr_sel'}):
                category.append(sub_item.next_element.text)

    print(code + "，" + h3 + "，" + href + "，" + date + "，" + time + "，" + ','.join(str(item) for item in author) + "，" + ','.join(
        str(item) for item in category))
    # for sub_item in item.find_all(name='span'):
    #     print(sub_item.text)

    # for item in soup.find_all(class_='container'):
    #     print(item)
    #     print(item.a.attrs.get("href") + "，" + item.img.attrs.get("title") + "，" + item.img.attrs.get("src"))
    # urllib.request.Request(url="https://www.javsee.lol" + href, headers=headers)
    # urllib.request.urlretrieve("https://www.javsee.lol" + href, '/Users/qsmy/Pictures/qsmy/' + code + "_cover.jpg")
    if 'http' in href:
        r = requests.get(href)
    else:
        r = requests.get("https://www.javsee.lol" + href)
    with open('/Users/qsmy/Pictures/qsmy/' + code + "_cover.jpg", 'wb') as f:
        f.write(r.content)


if __name__ == "__main__":

    with open('url.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        scrape_data(url=line.strip())
    # scrape_data(url='https://www.javsee.lol/AARM-223')
