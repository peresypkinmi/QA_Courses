
def getCourse(VAL):
    import requests
    import json

    ACCESS_KEY = "1a9f381124042ca053ae4697e42340d4"
    url = "http://api.currencylayer.com/live"
    head = {"access_key": ACCESS_KEY}

    req = requests.get(url, params=head)
    s = req.text
    jsonD = json.loads(s)
    res = jsonD.get('quotes').get(VAL)

    return res



def convert(amount):
    import math
    num = getCourse("USDRUB")
    return round(amount/num, 1)

currency = "RUB"
amount = int(input())
print("Вы ввели {} {}".format(amount, currency))
print("Конвертированная сумма в USD = {}".format(convert(amount)))



