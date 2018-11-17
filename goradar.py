#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: price-notification/goradar.py
# discription: 旅行雷达BUG短信提醒

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pytz import timezone
import time

from sms_sender import send


receiver = [16267318573, 8615606296615]

last_title = None



def pull_goradar():
    url = 'http://www.goradar.cn/portal.php?mod=list&catid=4'
    s = requests.session()
    s.headers = {'Accept': '*/*',
                 'Accept-Encoding': 'gzip, deflate',
                 'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,en-US;q=0.7',
                 'Connection': 'close',
                 'Host': 'www.goradar.cn',
                 'Referer': 'http://www.goradar.cn/portal.php?mod=list&catid=4',
                 'Upgrade-Insecure-Requests': '1',
                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
                 }
    r = s.get(url)
    if r.status_code == 200:
        return r
    else:
        print(r.status_code)
        return None


def process_data():
    global last_title
    r = pull_goradar()
    html = r.content
    soup = BeautifulSoup(html, "html.parser")
    items = soup.select('dl.bbda.cl')
    for i in items:
        title = i.dt.text
        link = i.dt.a.get('href')
        date = i.span.text.split(' ')[1]
        source = i.span.text.split(' ')[2]
        today = datetime.now(timezone('Asia/Shanghai')).strftime('%Y-%m-%d')
        li = [title, link, date, source]
        if 'BUG' in title:
            if title != last_title and date == today:
                result = send_to_receiver(li)
                last_title = title
                # log(result)
            break


def send_to_receiver(li, debug=0):
    msg = generate_msg(li)
    for phone in receiver:
        send(phone, msg)
    if debug != 0:
        print(msg)
        print(len(msg))


def generate_msg(li):
    title = li[0]
    link = li[1]
    date = li[2]
    source = li[3]
    msg = '【BUG提醒】{}\n{}\n来源: {}\n({})'.format(title, date, source, link)
    return msg


def start():
    c = 0
    while True:
        c += 1
        process_data()
        print('第%s次扫描完成。' % c)
        time.sleep(300)




if __name__ == '__main__'
    start()



