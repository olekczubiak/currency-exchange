from bs4 import BeautifulSoup

name = ['EUR', 'CHF', 'USD', 'GBP']



# Poprawić na odczytywanie pliku
FILE = 'html/html_liderwalut.html'

def open_file(filename):
    return open(filename, 'r', encoding='utf8').read()

def search(filename, name = 'EUR'):
    soup = BeautifulSoup(open_file(filename, ), "html.parser")
    finder_to_buy_sell = soup.body.find('tr', attrs={'class': name})
    fake_list = finder_to_buy_sell.find_all('td')
    return {fake_list[0].text: {'BUY': fake_list[1].text,"SELL": fake_list[2].text }}

def add_to_db():
    pass


def print_all_currency():
    for element in name:
        # tu bedzie polaczenie do bazy danych (add_to_db)
        print(search(FILE, element))



if __name__ == "__main__":
    print_all_currency()
