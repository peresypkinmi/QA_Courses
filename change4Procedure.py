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
while True:
    lsChoise = ['', 'USD','EUR','CHF','GBP','CNY']
    choise = input('Выберите валюту из:\n 1-USD\n 2-EUR\n 3-CHF\n 4-GBP\n 5-CNY \n')
    if choise=='':
        print('Вы ввели пустое поле. Введите число от 1 до 5')
        continue

    try:
        choise = int(choise)
    except ValueError:
        print("Вы ввели не число. Введите число от 1 до 5")
        continue
    if int(choise)<1:
        print("Введите число от 1 до 5")
        continue
# print(res)
    amount = input("Введите сумму\n")
    if amount=='':
        print('Вы ввели пустое поле. Введите число.')
        continue

    try:
        amount = int(amount)
    except ValueError:
        print("Вы ввели не число. Введите число.")
        continue
    if int(amount)<0:
        print("Введите положительное число.")
        continue
# print("edem dalshe")
    if choise==1:
        num1 = (int(amount)/res["USDRUB"])
    else:
        num1 = (int(amount)/res["USDRUB"])*res["USD"+lsChoise[choise]]
    print("Вы ввели сумму {} {}".format(amount, currency))
    print("конвертированная сумма в {} = {}".format(lsChoise[choise], num1))
# for i in range(len(listCur)):
#     print("конвертированная сумма в {} = {}".format(listCur[i][3:], listRes[i]))

