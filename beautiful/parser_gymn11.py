from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_htm(url):
    response = urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    zag = soup.find('div', class_ = "blog")

    spisok=[]

    for i in zag.find_all('div', class_ = "container row"):
        title = i.find_all('div')
        spisok.append({
            'title':title[0].h2.a.text,
            'text':title[0].p.text
        })


    return spisok


def parse2(html):
    """тут будут мои тесты"""
    soup = BeautifulSoup(html, "html.parser")
    zag = soup.find('div', class_="blog")

    for link in zag.find_all('a'):
        if 'href' in link.attrs:
            print(link.attrs['href'])



def last_page(s):
    s1=str(s)
    k1 = s1.find('page=') + 5
    k2 = s1.find('Последняя') - 2
    return int(s1[k1:k2])

def get_page_count(html):
    soup = BeautifulSoup(html, "html.parser")
    pagination = soup.find('div', id="pagination")
    s = pagination.div.ul.find_all('li')[-3].text
    number=int(s)
    return number


def main(s):

    page_count = get_page_count(get_htm(s))
    print('всего найдено страниц %d' % page_count)

    #projects = []
    #t1 = 6

    #for page in range(1, page_count):
       # print('Парсинг %d%%' % (page / page_count * 100))
        #projects.extend(parse(get_htm(s + '?start=%d' % t1)))
        #t1 = t1 + 6
    #вывод данных на экран
    #for project in projects:
      #  print(project)
#index.php?start=6
    print(parse2(get_htm(s)))



if __name__ == '__main__':
    #s = 'https://www.weblancer.net/jobs'
    s = 'http://gymn11.ru/index.php'
    main(s)
