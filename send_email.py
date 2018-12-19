import smtplib
import csv
from email.message import EmailMessage

import getpass
password = getpass.getpass('비밀번호 머니')

f = open('pygj.csv', 'r', encoding='utf-8')
read_csv = csv.reader(f)

smtp_url = 'smtp.naver.com'
smtp_port = 465

s = smtplib.SMTP_SSL(smtp_url, smtp_port)
s.login('chlwlsgh78', password)


for line in read_csv:
     msg = EmailMessage()
     msg['subject'] = line[0] + "은(는) 배고프다" #대괄호 리스트 접근,스트링일때 딕셔너리 접근
     msg['From'] = "chlwlsgh78@naver.com"
     msg['To'] = line[1]
 
     msg.set_content(line[0] + '님 배고파요')
     s.send_message(msg)