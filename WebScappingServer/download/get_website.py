import time
import requests

# Delete Adding certificate verification is strongly advised.
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# ----------------------------------------------------------------------





MY_TIME = str(time.ctime()).replace(' ', '-')
NAMES = ['internetowykantor', 'liderwalut', 'topfx']

def download_file(url):
    r = requests.get(url, verify=False)
    return r.content


def write_file(n, content):
    file_name = f'html/html_{NAMES[n]}.html'
    with open(file_name, 'wb') as f:
        f.write(content)

def scrape_tasks(n ,url):
    content = download_file(url)
    write_file(n, content)

def main():
    tasks = []
    for n, url in enumerate(open('urls.txt').readlines()):
        tasks.append(scrape_tasks(n, url))

if __name__ == "__main__":
    main()
