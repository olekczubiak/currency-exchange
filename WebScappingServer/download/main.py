from time import sleep, ctime
import sqlite3
from bs4 import BeautifulSoup
import requests
import os
import datetime
# to delete errors
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# ----------------------------------------------------------------------

# Olek PC
DB_PATH = '/Users/olek/Documents/CurrencyExchange/BackendServer/CurrencyExchange/db.sqlite3'

# JAN OP PC
# DB_PATH = 'C:\\Users\\jkopr\\Desktop\\CurrencyExchange\\currency-exchange\\BackendServer\\CurrencyExchange\\db.sqlite3'


class OpenFile:
    def open_file(self):
        return open(self, 'r', encoding='utf8').read()

class ToJson:
    def return_json_msg(name, buy_price, sell_price):
        return {name: {'BUY': buy_price, 'SELL': sell_price}}


class AddToDB:
    def __init__(self, my_id = None ,
                    name = 'ERROR NAME', 
                    date = 'ERROR DATE',
                    buy_price = 0.00, 
                    sell_price = 0.00, 
                    currency = 'ERROR', 
                    website='www.error.com', 
                    rating:int = 10):
        self.id: int = my_id
        self.name: str = name
        self.date: str = date
        self.buy_price: float = buy_price
        self.sell_price: float = sell_price
        self.currency: str = currency
        self.website: str = website
        self.rating: int = rating
    def main(self):
        try:
            # ADD REAL PATH TO DB
            sqliteConnection = sqlite3.connect(os.path.realpath(DB_PATH))
            cursor = sqliteConnection.cursor()
            sqlite_insert_query = """
                            INSERT INTO api_basic_cantor
                            (ID, name, date, 
                            buy, sell, 
                            currency, 
                            website, rating) 
                            VALUES 
                            (?,?,?,?,?,?,?,?);"""
            count = cursor.execute(sqlite_insert_query, (self.id,self.name,self.date , 
                                                        self.buy_price, self.sell_price, 
                                                        self.currency, self.website, self.rating))
            sqliteConnection.commit()
            print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
            cursor.close()
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")


class Parse:
    def __init__(self):
        self.CURRENCIES: list = ['EUR', 'GBP', 'CHF', 'USD']
        self.CANTOR_NAMES: list = ['internetowykantor', 'liderwalut', 'topfx']
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
    def __init__(self):
        self.PATH:str = 'html/html_liderwalut.html'
        self.name:str = 'Lider walut'
        self.date:str = datetime.datetime.now()
        self.website: str = 'www.liderwalut.pl'
        self.rating: int = 1
    
    def search(self, filename, name = 'EUR',to_return:int = 1, table_to_find = 'tr', cell_to_find = 'td'):
        soup = BeautifulSoup(OpenFile.open_file(filename), "html.parser")
        finder_to_buy_sell = soup.body.find(table_to_find, attrs={'class': name})
        fake_list = finder_to_buy_sell.find_all(cell_to_find)
        return fake_list[to_return].text


    # def print_to_debug(self):
    #     print("Lider Walut")
    #     for element in Parse().CURRENCIES:
    #         print(ToJson.return_json_msg(element, self.search(self.PATH, element), self.search(self.PATH, element, 2)))

    def add_to_db(self):
        for num in range(4):
            AddToDB(None,
            self.name, 
            self.date, 
            float(self.search(self.PATH, Parse().CURRENCIES[num])), 
            float(self.search(self.PATH, Parse().CURRENCIES[num], 2)),
            Parse().CURRENCIES[num],
            self.website, self.rating).main()

class TopFx(Parse):
    PATH: str
    NAMES_TO_BUY: list
    NAMES_TO_SELL: list
    def __init__(self):
        self.PATH = 'html/html_topfx.html'
        self.name:str = 'TopFx'
        self.date:str = datetime.datetime.now()
        self.website: str = 'www.topfx.pl'
        self.rating: int = 2
                                #['EUR', 'GBP', 'CHF', 'USD']
        self.NAMES_TO_BUY = ['buy_EUR','buy_GBP', 'buy_CHF','buy_USD']
        self.NAMES_TO_SELL = ['sell_EUR','sell_GBP', 'sell_CHF', 'sell_USD']

    def search(self, filename, name ,element_to_buy, element_to_sell, container = 'span', element_name = 'id'):
        soup = BeautifulSoup(OpenFile.open_file(filename), "html.parser")
        finder_to_buy = soup.body.find(container, attrs={element_name: element_to_buy}).text
        finder_to_sell = soup.body.find(container, attrs={element_name: element_to_sell}).text
        return finder_to_buy, finder_to_sell

    def add_to_db(self):
        for element1, element2, element3 in zip(Parse().CURRENCIES, self.NAMES_TO_BUY, self.NAMES_TO_SELL):
            AddToDB(None,
                    self.name, 
                    self.date,
                    float(self.search('html/html_topfx.html', element1, element2, element3)[0].replace(',', '.')),
                    float(self.search('html/html_topfx.html', element1, element2, element3)[1].replace(',', '.')),
                    element1,
                    self.website,
                    self.rating).main()

class InternetowyKantor(Parse):
    PATH: str
    class_name_to_buy: str
    class_name_to_sell: str
    def __init__(self):
        self.PATH = 'html/html_internetowykantor.html'
        self.CURRENCIES = ['eur', 'gbp', 'chf', 'usd']
        self.class_name_to_buy = 'currency_table_buy bem-rate-table__rate'
        self.class_name_to_sell = "currency_table_sell bem-rate-table__rate"
        self.name: str = 'InternetowyKantor'
        self.date: str = datetime.datetime.now()
        self.website: str = 'www.internetowykantor.pl'
        self.rating: int = 3


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
        return buy_list[i], sell_list[i]

    def print_to_debug(self):
        print('Internetowy Kantor')
        print(self.search(self.PATH, 0)[0])
        print(self.search(self.PATH, 0)[1])



    def add_to_db(self):
        for element in range(4):
            AddToDB(None,
                    self.name,
                    self.date,
                    float(self.search(self.PATH, element)[0].replace(',', '.')),
                    float(self.search(self.PATH, element)[1].replace(',', '.')),
                    self.CURRENCIES[element].upper(),
                    self.website,
                    self.rating).main()


if __name__ == "__main__":

    # Test db connection
    # AddToDB().main()

    # Add to db
    # LiderWalut().add_to_db()
    # TopFx().add_to_db()
    # InternetowyKantor().add_to_db()

    # Loop
    for x in range(3):
        Parse()
        LiderWalut().add_to_db()
        TopFx().add_to_db()
        InternetowyKantor().add_to_db()
        sleep(30)