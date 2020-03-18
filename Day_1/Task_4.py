import requests
import json


def convert_to_dollars(uah, rate):
    return uah / rate


def get_dollar_rate(resp):
    return json.loads(json.dumps(resp))[0]['buy']


resp = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5").json()
uah = int(input("Enter uah: "))
print(convert_to_dollars(uah, float(get_dollar_rate(resp))))

