#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: price-notification/goradar.py
# discription: 旅行雷达BUG短信提醒

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pytz import timezone
import sms
import time

s = requests.session()
s.keep_alive = False

def search_bug():
    url = 'http://www.goradar.cn/portal.php?mod=list&catid=4'
    r = s.get(url)
    source = soup.select('dl.bbda.cl')
    for i in source:
        title = i.dt.text
        if 'BUG' or 'bug' in title:
            date = source[0].span.text.strip().split(' ')[0]
            agency = source[0].span.text.strip().split(' ')[1]
            today = datetime.now(timezone('Asia/Shanghai')).strftime('%y-%m-%d')
            if date == today:
                text = '旅行雷达找到BUG\r%s\r%s' % (title, agency)
                print(text)
                sms.send_sms(16267318573, text)

def start():
    c = 0
    while True:
        c += 1
        search_bug()
        print('第%s次扫描完成。' % c)
        time.sleep(600)

def help():
    print'''
help'''


if __name__ != '__main__'
    start()
else:
    help()


