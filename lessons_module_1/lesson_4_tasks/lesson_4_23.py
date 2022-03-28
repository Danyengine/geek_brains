
from calendar import day_abbr
from shutil import ExecError
from unicodedata import decimal
from urllib import response
from urllib.error import HTTPError
import requests as req
#from decimal import getcontext, Decimal
from decimal import*
from datetime import datetime

# Устанавливаем число десятичных цифр
#getcontext().prec = 4


"""
Task_2,3
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp. 
Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа. 
Можно ли, используя только методы класса str, решить поставленную задачу? 
Функция должна возвращать результат числового типа, например float. 
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal? 
Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, 
которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, 
в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.

Доработать функцию currency_rates(): 
теперь она должна возвращать кроме курса дату, которая передаётся в ответе сервера. 
Дата должна быть в виде объекта date. Подумайте, 
как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
"""

# Устанавливаем число десятичных цифр
getcontext().prec = 6

def currency_rates(code_cur):
    code_cur = code_cur.upper()

    try:
        response = req.get('http://www.cbr.ru/scripts/XML_daily.asp')

    except HTTPError as http_error:
        print('http error occured: {}'.format(http_error))
    except ExecError as err:
        print('other error occurred: {}'.format(err))
    else:
        response = response.text

        if code_cur not in response:
            return None
        
        # string.find(str, [start],[end])
        rub = response[response.find('<Value>', response.find(code_cur)) + 7: response.find('</Value>', response.find(code_cur))]
        data_cur = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.') # Date="26.03.2022"
        day_cur, month_cur, year_cur = [int(x) for x in data_cur]

    #return ('Перевод {:3f} в рубли: {:3f}'.format(code_cur, Decimal(rub.replace(',', '.'))))
    return f"Перевод {code_cur} в рубли: {Decimal(rub.replace(',', '.'))},\
        \n\nДата последнего обновления: {datetime(day = day_cur, month = month_cur, year = year_cur)}"

        
def main():
    print(currency_rates('GBP'))
    print(currency_rates('USD'))
    print(currency_rates('EUR'))

if __name__=="__main__":
    main()


    

"""
Task_4
"""

