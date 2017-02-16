from urllib.request import urlopen
from bs4 import BeautifulSoup


Adress = 'https://www.avito.ru/kemerovo/noutbuki?q=macbook&sgtd=2'

def get_htm(url):
    response = urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html, "html.parser") #, "html.parser"
    table = soup.find('div', class_="js-catalog_before-ads")
    #print(table)
    spisok =[]
    for i in table.find_all('div'):
        spisok.append(i.find_all('div'))

    print(spisok)
def main(A):
    parse(get_htm(Adress))


if __name__ == '__main__':
    main(Adress)