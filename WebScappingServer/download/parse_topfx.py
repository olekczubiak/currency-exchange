from bs4 import BeautifulSoup

name = ['EUR', 'CHF', 'USD', 'GBP']
to_buy = ['buy_EUR','buy_CHF','buy_USD', 'buy_GBP']
to_sell = ['sell_EUR','sell_CHF', 'sell_USD', 'sell_GBP']


# Poprawić na odczytywanie pliku
FILE = 'html/html_topfx.html'

def open_file(filename):
    return open(filename, 'r', encoding='utf8').read()

def search(filename, name, buy_name, sell_name):
    soup = BeautifulSoup(open_file(filename), "html.parser")
    finder_to_buy = soup.body.find('span', attrs={'id': buy_name}).text
    finder_to_sell = soup.body.find('span', attrs={'id': sell_name}).text
    return {name: {'BUY': finder_to_buy,"SELL": finder_to_sell }}

def add_to_db():
    pass


def print_all_currency():
    for element1, element2, element3 in zip(name, to_buy, to_sell):
        # Tu bedzie dodanie do bazy danych
        print(search(FILE, element1, element2, element3))

if __name__ == "__main__":
    print_all_currency()