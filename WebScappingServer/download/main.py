from time import sleep
from bs4 import BeautifulSoup
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# ----------------------------------------------------------------------


class OpenFile:
    def open_file(self):
        return open(self, 'r', encoding='utf8').read()

class ToJson:
    def return_json_msg(name, buy_price, sell_price):
        return {name: {'BUY': buy_price, 'SELL': sell_price}}

class Parse:
    def __init__(self):
        self.CURRENCIES: list = ['EUR', 'CHF', 'USD', 'GBP']
        self.CANTOR_NAMES: list =  ['internetowykantor', 'liderwalut', 'topfx']
    def download_file(self,url):
        r = requests.get(url, verify=False)
        return r.content
    def write_file(self, n, content):
        file_name = f'html/html_{self.CANTOR_NAMES[n]}.html'
        with open(file_name, 'wb') as f:
            f.write(content)
    def scrape_tasks(self, n ,url):
        content = self.download_file(url)
        self.write_file(n, content)
    def main(self):
        for n, url in enumerate(open('urls.txt').readlines()):
            self.scrape_tasks(n, url)


class LiderWalut(Parse):
    PATH: str
    def __init__(self):
        self.PATH = 'html/html_liderwalut.html'
    
    def search(self, filename, name = 'EUR', table_to_find = 'tr', cell_to_find = 'td'):
        soup = BeautifulSoup(OpenFile.open_file(filename), "html.parser")
        finder_to_buy_sell = soup.body.find(table_to_find, attrs={'class': name})
        fake_list = finder_to_buy_sell.find_all(cell_to_find)
        return ToJson.return_json_msg(fake_list[0].text, fake_list[1].text, fake_list[2].text)

    def print_to_debug(self):
        print("Lider Walut")
        for element in Parse().CURRENCIES:
            print(self.search(self.PATH, element))

class TopFx(Parse):
    PATH: str
    NAMES_TO_BUY: list
    NAMES_TO_SELL: list
    def __init__(self):
        self.PATH = 'html/html_topfx.html'
        self.NAMES_TO_BUY = ['buy_EUR','buy_CHF','buy_USD', 'buy_GBP']
        self.NAMES_TO_SELL = ['sell_EUR','sell_CHF', 'sell_USD', 'sell_GBP']

    def search(self, filename, name, element_to_buy, element_to_sell, container = 'span', element_name = 'id'):
        soup = BeautifulSoup(OpenFile.open_file(filename), "html.parser")
        finder_to_buy = soup.body.find(container, attrs={element_name: element_to_buy}).text
        finder_to_sell = soup.body.find(container, attrs={element_name: element_to_sell}).text
        return ToJson.return_json_msg(name, finder_to_buy, finder_to_sell)

    def print_to_debug(self):
        print('TopFx')
        for element1, element2, element3 in zip(Parse().CURRENCIES, self.NAMES_TO_BUY, self.NAMES_TO_SELL):
            print(self.search(self.PATH ,element1, element2, element3 ))

class InternetowyKantor(Parse):
    PATH: str
    class_name_to_buy: str
    class_name_to_sell: str
    def __init__(self):
        self.PATH = 'html/html_internetowykantor.html'
        self.CURRENCIES = ['eur', 'chf', 'usd', 'gbp']
        self.class_name_to_buy = 'currency_table_buy bem-rate-table__rate'
        self.class_name_to_sell = "currency_table_sell bem-rate-table__rate"
    
    def search(self, filename, i = 0):
        soup = BeautifulSoup(OpenFile.open_file(filename), "html.parser")
        def finder_to_buy(CURRENCIES):
            to_buy_list = []
            for j in CURRENCIES:
                to_buy_list.append(soup.body.find('tr', attrs={'data-currency-id': j}).find('td', attrs={'class': self.class_name_to_buy}).text)
            return to_buy_list
        def finder_to_sell(CURRENCIES):
            to_sell_list = []
            for j in CURRENCIES:
                to_sell_list.append(soup.body.find('tr', attrs={'data-currency-id': j}).find('td', attrs={'class': self.class_name_to_sell}).text)
            return to_sell_list
        buy_list = finder_to_buy(self.CURRENCIES)
        sell_list = finder_to_sell(self.CURRENCIES)
        return {self.CURRENCIES[i].upper(): {'BUY': buy_list[i], "SELL": sell_list[i]}}

    def print_to_debug(self):
        print('Internetowy Kantor')
        for element in range(4):
            print(self.search(self.PATH,element))





if __name__ == "__main__":
    for x in range(3):
        # Pobieranie i zapisywanie do pliku
        Parse().main()
        # Wyciagacze html 
        LiderWalut().print_to_debug()
        TopFx().print_to_debug()
        InternetowyKantor().print_to_debug()
        print('----------------------------------------')
        sleep(30)
