import requests
import json

url_tokens = 'https://api.zks.app/1/tokens'
url_price = 'https://api.zks.app/1/tokens/price'


def get_token():
    data = requests.get(url_tokens)
    return json.loads(data.text)['data']


def get_price(result):
    # id_symbols = {}
    # # id 对应 symbol
    # for r in result:
    #     id_symbols[r['id']] = r['symbol']
    id = 1
    for r in result:
        if r['symbol'] == "ZKS":
            id = r['id']
    data = json.loads(requests.get(url_price).text)['data']
    for d in data:
        if d['id'] == id:
            return d['price']


def saveText(path, price):
    with open(path, 'w', encoding="utf-8") as f:
        f.writelines(price)


if __name__ == '__main__':
    result = get_token()
    price = get_price(result)
    email_path = "email.txt"
    saveText(email_path, price)
