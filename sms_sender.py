#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename: nexmo_sender.py
# version: 0.0.1
# description:


import nexmo
import queue
import threading
import time


api_key = 'd1258708'
api_secret = 'Nosecret'


def auto_login(alive=6000):
    now_time = time.time()
    time_past = int(now_time - last_login_time)
    if time_past < alive:
        message = '上次登录%d秒前，无需登录' % time_past
        print(message)
    else:
        message = '上次登录%d秒前，重新登录' % time_past
        print(message)

def login():
    global last_login_time
    global client
    client = nexmo.Client(key=api_key, secret=api_secret)
    last_login_time = time.time()


def send_message(receiver, text):
    auto_login()
    result = client.send_message(
        {'from': 13658000403,
        'to': receiver,
        'text': text,
        'type': 'unicode'})
    return result


def send(receiver, text):
    message = [receiver, text]
    q.put(message)


def sender():
    global q
    global sender_status
    sender_status = True
    q = queue.Queue()
    while sender_status == True:
        receiver, text = q.get()
        if type(receiver) == type(1):
            r = send_message(receiver, text)
            print(r)
            status = r['messages'][0]['status']
            if status != '0':
                print(status)
            time.sleep(3)
    print('发件人停止')


def sender_start():
    login()
    a = threading.Thread(target=sender, args=())
    a.start()

def sender_stop():
    global sender_status
    sender_status = False
    send('stop','')

sender_start()

if '__main__' == '__main__':
    import code
    code.interact(banner = "", local = locals())
