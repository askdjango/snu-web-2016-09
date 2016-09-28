# -*- coding: utf-8 -*-
import smtplib
import sys
from getpass import getpass

sender = input('네이버 이메일 주소 : ')
receiver = input('수신자 이메일 주소 : ')
password = getpass('Enter Password : ')
subject = '저에게 쓰는 편지'
message = '''blah blah blah
blah blah blah ~~~
blah blah blah ~~~
blah blah blah ~~~한글 메세지

파이썬 버전 : {}'''.format(sys.version_info[:3])

server = smtplib.SMTP_SSL('smtp.naver.com', 465)
server.login(sender, password)

body = '''To: {}
From: {}
Subject: {}

{}'''.format(receiver, sender, subject, message)

server.sendmail(sender, [receiver], body.encode('utf8'))
server.quit()

print('sended!')
