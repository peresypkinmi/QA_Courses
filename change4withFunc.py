
def getCourse():
    import requests
    import json
    ACCESS_KEY = "1a9f381124042ca053ae4697e42340d4"
    url = "http://api.currencylayer.com/live"
    head = {"access_key": ACCESS_KEY} # прикручиваем хедер для авторизации
    req = requests.get(url, params=head)
    s = req.text
    jsonD = json.loads(s)
    res = jsonD.get('quotes')

    return res

def printCourse(list, choice, amount):
    num = getCourse()
    if amount==0:
        return 0
    if choice==1:
        res = amount/num["USDRUB"]
    else:
        res = (amount/num["USDRUB"])*num["USD"+list[choice]]
    return res
def checks(amount):
    if amount == '':
        print("Вы ввели пустое поле. Введите число.")
        return amount, False
    try:
        amount = int(amount)
    except ValueError:
        print("Вы ввели не число. Введите число.")
        return amount, False

    if int(amount) < 0:
        print("Введите положительное число.")
        return amount, False
    elif int(amount)>=0:
        return int(amount), True
def checksChoice(amount):
    if amount == '':
        print("Вы ввели пустое поле. Введите число от 1 до 5")
        return amount, False
    try:
        amount = int(amount)
    except ValueError:
        print("Вы ввели не число. Введите число от 1 до 5")
        return amount, False

    if int(amount) < 1:
        print("Введите число от 1 до 5")
        return amount, False
    elif int(amount)>=1 and int(amount)<=5:
        return int(amount), True





listCur = ["USDEUR", "USDCHF", "USDGBP", "USDCNY"]
currency = "RUB"
ls = ['','USD','EUR','CHF','GBP','CNY']
while True:
    choice = input("Выберите валюту из: \n1 - 'USD'\n2 - 'EUR'\n3 - 'CHF'\n4 - 'GBP'\n5 - 'CNY'\n")
    choice, b = checksChoice(choice)
    if b==False:
        continue
    amount = input("Введите сумму\n")
    amount, b = checks(amount)
    if b == False:
        continue

    s = printCourse(ls, choice, amount)
    print("Вы ввели {} {}".format(amount, currency))
    print("Конвертированная сумма в {} = {}".format(ls[choice], s))












