import requests
import json

listRes = []
listCur = ["USDEUR", "USDCHF", "USDGBP", "USDCNY"]
currency = "RUB"
ACCESS_KEY = "1a9f381124042ca053ae4697e42340d4"
url = "http://api.currencylayer.com/live"
head = {"access_key": ACCESS_KEY}

req = requests.get(url, params=head)
s = req.text
jsonD = json.loads(s)
res = jsonD.get('quotes')
# print(res)
amount = input()
if amount=='':
    print('Вы ввели пустое поле. Введите число.')
    exit()

try:
    amount = int(amount)
except ValueError:
    print("Вы ввели не число. Введите число.")
    exit()
if int(amount)<0:
    print("Введите положительное число.")
    exit()
# print("edem dalshe")
for i in listCur:
    listRes.append(round((int(amount)/res["USDRUB"])*res[i], 1))
listRes.append(round((int(amount)/res["USDRUB"]), 1))
listCur.append("RUBUSD")
print("Вы ввели {} {}".format(amount, currency))

for i in range(len(listCur)):
    print("конвертированная сумма в {} = {}".format(listCur[i][3:], listRes[i]))

