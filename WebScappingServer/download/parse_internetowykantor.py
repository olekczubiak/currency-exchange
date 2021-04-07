from bs4 import BeautifulSoup


CURRENCIES = ['eur', 'chf', 'usd', 'gbp']
to_buy = "currency_table_buy bem-rate-table__rate"
to_sell = "currency_table_sell bem-rate-table__rate"

# Poprawić na odczytywanie pliku
FILE = 'html/html_internetowykantor.html'

def open_file(filename):
    return open(filename, 'r', encoding='utf8').read()


def search(filename, i = 0):

    soup = BeautifulSoup(open_file(filename, ), "html.parser")

    def finder_to_buy(CURRENCIES):
        to_buy_list = []
        for j in CURRENCIES:
            to_buy_list.append(soup.body.find('tr', attrs={'data-currency-id': j}).find('td', attrs={'class': to_buy}).text)
        return to_buy_list

    def finder_to_sell(CURRENCIES):
        to_sell_list = []
        for j in CURRENCIES:
            to_sell_list.append(soup.body.find('tr', attrs={'data-currency-id': j}).find('td', attrs={'class': to_sell}).text)
        return to_sell_list

    buy_list = finder_to_buy(CURRENCIES)
    sell_list = finder_to_sell(CURRENCIES)

    return {CURRENCIES[i].upper(): {'BUY': buy_list[i], "SELL": sell_list[i]}}

def add_to_db():
    pass

def print_all_currency():
    for j in range(4):
        print(search(FILE, j))

if __name__ == "__main__":
    print_all_currency()
