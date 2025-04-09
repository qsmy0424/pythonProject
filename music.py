# _*_ coding: utf-8 _*_
# @Time: 2023/3/27 20:54
# @Author: 🎈
# @File: demo
import requests
import os
import re
from urllib import request
from urllib.parse import quote
import time
import random

"""
音频下载接口：
https://www.kuwo.cn/api/v1/www/music/playUrl?mid=440616&type=flac&httpsStatus=
https://www.kuwo.cn/api/v1/www/music/playUrl?mid={music_id}&type=flac&httpsStatus=1&reqId=80b33650-8a62-11ed-a069-8d99eba73f2a
"""

kw = input('请输入歌曲查询词: ')
base_url = f'https://kuwo.cn/search/list?key={quote(kw)}'
session = requests.Session()
resp = session.get(base_url).cookies
headers = {
    'Cookie': f"_ga=GA1.2.546227376.1683438650; _gid=GA1.2.1324843845.1684306466; SL_G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1684306502; _gat=1; kw_token={resp.get('kw_token')}",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Referer': base_url,
    'csrf': resp.get('kw_token'),
}


def get_ids(url):
    """获取搜索结果的歌曲id"""
    try:
        with session.get(url, headers=headers) as response:
            if response.status_code == 200:
                print(response.cookies.get('kw_token'))  # kw_token  cookie中携带的
                json_data = response.json()
            else:
                return 'code error!'
    except ConnectionError as e:
        print('error: ', e)
        raise e

    items = json_data['data']['list']
    for item in items:
        name = item['name']
        rid = item['rid']
        yield name, rid


def download(music_name, music_id):
    d_url = f'https://www.kuwo.cn/api/v1/www/music/playUrl?mid={music_id}&type=flac&httpsStatus=1&reqId=80b33650-8a62-11ed-a069-8d99eba73f2a'
    response = requests.get(d_url, headers=headers)
    result = response.json()
    play_url = result.get("data").get("url")

    # 获取当前路径并创建文件夹
    path = os.getcwd()
    folder_path = os.path.join(path, kw)
    os.path.exists(folder_path) or os.mkdir(folder_path)
    music_name = re.sub(r'[\\/:\*\?"<>\|]', '', music_name)  # 去除文件名可能出现的非法字符
    file_path = os.path.join(folder_path, music_name + '.mp3')

    # 下载音乐
    # request.urlretrieve(play_url, file_path)

    print(f'{music_name} >>> Download completed')
    music_content = requests.get(play_url).content
    with open(file_path, mode='wb') as f:
        f.write(music_content)


def scrape_index(page):
    url = f'https://kuwo.cn/api/www/search/searchMusicBykeyWord?key={quote(kw)}&pn={page}&rn=20&httpsStatus=1'
    return get_ids(url)


def main():
    # sleep_time = [random.uniform(1, 3) for i in range(10)]  # 在1-3之间随机返回一个数
    # for page in range(8, 18):
    #     print(f'开始下载第{page}页')
    #     # url = f'https://kuwo.cn/api/www/search/searchMusicBykeyWord?key={quote(kw)}&pn={page}&rn=20&httpsStatus=1'
    #     g_data = scrape_index(page)
    #     time.sleep(random.choice(sleep_time))
    #     for n, i in g_data:
    #         download(n, i)

    # 不考虑歌曲数量
    page = 1
    sleep_time = [random.uniform(1, 3) for i in range(10)]  # 在1-3之间随机返回一个数
    while True:
        print(f'开始下载第{page}页')
        g_data = scrape_index(page)
        time.sleep(random.choice(sleep_time))
        for n, i in g_data:
            download(n, i)
        page += 1


if __name__ == '__main__':
    main()
