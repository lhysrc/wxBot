#!/usr/bin/env python
# coding: utf-8

from wxbot import *


class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
            self.send_msg_by_uid(u'[自动回复]', msg['user']['id'])
'''
    def schedule(self):
        self.send_msg(u'张三', u'测试')
        time.sleep(1)
'''


def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()

    for g in bot.group_list:
        print g['UserName'],g['NickName'] ## 所有群


if __name__ == '__main__':
    main()
