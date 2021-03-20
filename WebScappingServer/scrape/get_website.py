import time
import requests


MY_TIME = str(time.ctime()).replace(' ', '-')
NAMES = ['internetowykantor', 'liderwalut', 'trejdoo']

def download_file(url):
    r = requests.get(url, verify=False)
    return r.content


def write_file(n, content):
    file_name = f'html/html_{n}_{NAMES[n]}_{MY_TIME}.html'
    with open(file_name, 'wb') as f:
        f.write(content)

def scrape_tasks(n ,url):
    content = download_file(url)
    write_file(n, content)

def main():
    tasks = []
    for n, url in enumerate(open('urls.txt').readlines()):
        tasks.append(scrape_tasks(n, url))

main()
