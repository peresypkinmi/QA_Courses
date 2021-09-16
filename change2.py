
def getCourse():
    import requests
    import json

    ACCESS_KEY = "1a9f381124042ca053ae4697e42340d4"
    url = "http://api.currencylayer.com/live"
    head = {"access_key": ACCESS_KEY}

    req = requests.get(url, params=head)
    s = req.text
    jsonD = json.loads(s)
    res = jsonD.get('quotes')
    # print(res)
    return res

def printCourse(list, amount):
    num = getCourse()
    listRes = []

    for i in list:
        listRes.append(round((amount/num["USDRUB"])*num[i], 3))
    listRes.append(round(amount / num["USDRUB"], 3))


    return listRes
def checks(amount):
    if amount == '':
        print("Вы ввели пустое поле. Введите число.")
        exit()
    try:
        amount = int(amount)
    except ValueError:
        print("Вы ввели не число. Введите число.")
        exit()
    if int(amount) < 0:
        print("Введите положительное число.")
        exit()
    elif int(amount)>=0:
        return int(amount)





listCur = ["USDEUR", "USDCHF", "USDGBP", "USDCNY"]
currency = "RUB"
amount = int(input())
# amount = checks(amount)

s = printCourse(listCur, amount)
print("Вы ввели {} {}".format(amount, currency))
print("Конвертированная сумма в USD = {}".format(s[len(s)-1]))
for i in range(len(listCur)):
    print("Конвертированная сумма в {} = {}".format(listCur[i][3:], s[i]))










