from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_htm(url):
    response = urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    zag = soup.find_all('a')
    print(zag)



def main(s):
    parse(get_htm(s))

if __name__ == '__main__':
    s = 'https://www.ruobr.ru'
    main(s)