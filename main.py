import json
import smtplib
import sys
from email.mime.text import MIMEText

import requests

url_tokens = 'https://api.zks.app/1/tokens'
url_price = 'https://api.zks.app/1/tokens/price'

From = sys.argv[1]
PW = sys.argv[2]
To = sys.argv[3]
s_price = float(sys.argv[4])
b_price = float(sys.argv[5])


def get_token():
    data = requests.get(url_tokens)
    return json.loads(data.text)['data']


def get_price(result):
    id = 1
    for r in result:
        if r['symbol'] == "ZKS":
            id = r['id']
    data = json.loads(requests.get(url_price).text)['data']
    for d in data:
        if d['id'] == id:
            return d['price']


def sendEmail(price):
    if float(price) < s_price or float(price) > b_price:
        smtpObj = smtplib.SMTP_SSL('smtp.163.com', 465)
        # 登录 SMTP 服务器
        smtpObj.login(From, PW)
        # 发送邮件
        message = MIMEText(price, 'plain', 'utf-8')
        message['From'] = From
        message['To'] = To
        message['Subject'] = "zks 价格"
        smtpObj.sendmail(From, To, message.as_string())


if __name__ == '__main__':
    result = get_token()
    price = get_price(result)
    sendEmail(price)
