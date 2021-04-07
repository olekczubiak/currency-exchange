from bs4 import BeautifulSoup
class OpenFile:
    def open_file(self):
        return open(self, 'r', encoding='utf8').read()

class ToJson:
    def return_json_msg(name, buy_price, sell_price):
        return {name: {'BUY': buy_price, 'SELL': sell_price}}



class Parse:
    def __init__(self):
        self.CURRENCIES: list = ['EUR', 'CHF', 'USD', 'GBP']


    def search_in_list(filename, name = 'EUR', table_to_find = 'tr', cell_to_find = 'td'):
        soup = BeautifulSoup(OpenFile.open_file(filename), "html.parser")
        finder_to_buy_sell = soup.body.find(table_to_find, attrs={'class': name})
        fake_list = finder_to_buy_sell.find_all(cell_to_find)
        return ToJson.return_json_msg(fake_list[0].text, fake_list[1].text, fake_list[2].text)


    def search_by_names(filename, name, element_to_buy, element_to_sell, container = 'span', element_name = 'id'):
        soup = BeautifulSoup(OpenFile.open_file(filename), "html.parser")
        finder_to_buy = soup.body.find(container, attrs={element_name: element_to_buy}).text
        finder_to_sell = soup.body.find(container, attrs={element_name: element_to_sell}).text
        return ToJson.return_json_msg(name, finder_to_buy, finder_to_sell)

class LiderWalut(Parse):
    PATH: str
    def __init__(self):
        self.PATH = 'html/html_liderwalut.html'
    
    def print_to_debug(self):
        print("Lider Walut")
        for element in Parse().CURRENCIES:
            print(Parse.search_in_list(self.PATH, element))

class TopFx(Parse):
    PATH: str
    NAMES_TO_BUY: list
    NAMES_TO_SELL: list
    def __init__(self):
        self.PATH = 'html/html_topfx.html'
        self.NAMES_TO_BUY = ['buy_EUR','buy_CHF','buy_USD', 'buy_GBP']
        self.NAMES_TO_SELL = ['sell_EUR','sell_CHF', 'sell_USD', 'sell_GBP']

    def print_to_debug(self):
        print('TopFx')
        for element1, element2, element3 in zip(Parse().CURRENCIES, self.NAMES_TO_BUY, self.NAMES_TO_SELL):
            print(Parse.search_by_names(self.PATH ,element1, element2, element3 ))

class InternetowyKantor(Parse):
    PATH: str
    def __init__(self):
        self.PATH = 'html/html_internetowykantor.html'
    
    def print_to_debug(self):
        print('Internetowy Kantor')
        for element in Parse().CURRENCIES:
            print(Parse.search_in_list(self.PATH, element))





if __name__ == "__main__":
    LiderWalut().print_to_debug()
    TopFx().print_to_debug()
    # InternetowyKantor().print_to_debug()











# y = Parse.search_by_names('html/html_topfx.html', 'EUR', 'buy_EUR', 'sell_EUR')

# print(x)
# print(y)