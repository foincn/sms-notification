#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: email-code.py
# discription: Email Notification Third Part Server


from wxpy import *

bot = Bot(console_qr=2, cache_path=False)

bot.self.send('000000')

def send_msg(name, message, sex=None, city=None):
    search = bot.friends(update=False).search(name, sex=sex, city=city)
    friend = ensure_one(search)
    result = friend.send(message)
    return result



embed()
