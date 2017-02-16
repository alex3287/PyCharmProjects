from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


def get_htm(url):
    response = urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    zag = soup.find_all('a')
    print(zag)

def stop(x):
    i = 1
    for j in range(1, x):
        i *= j
    print(i)

def main(s):
    parse(get_htm(s))



if __name__ == '__main__':
    link2="https://www.ruobr.ru"
    main(link2)
    session = requests.Session()
    params = {'username': 'alex3287', 'password': 'winston'}
    s = session.post("https://ruobr.ru/accounts/login/", params)
    print('обработка')
    print(s.text)