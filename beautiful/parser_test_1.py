from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

def get_htm(url):
    response = urlopen(url)
    return response.read()
'''
def categor_check(s):

    if s==False:
        s = 'Нет категории'
        return s
    else:
        return s
'''
def parse(html):
    soup = BeautifulSoup(html, "html.parser") #, "html.parser"
    table = soup.find('div', class_="container-fluid cols_table show_visited")

    projects =[]

    for row in table.find_all('div', class_="row"):
        cols = row.find_all('div')
        #print(cols)
        if cols[-1].a:
            categor=cols[-1].find('a', class_="text-muted").text
        else:
            categor='Нет категории'
        projects.append({
            'title': cols[0].h2.a.text,
            'categories': categor,
            'price': cols[1].text.strip(),
            'application': cols[2].text.strip()
        })
    return projects

    #for project in projects:
     #   print(project)
def last_page(s):
    s1=str(s)
    k1 = s1.find('page=') + 5
    k2 = s1.find('Последняя') - 2
    return int(s1[k1:k2])

def get_page_count(html):
    soup = BeautifulSoup(html, "html.parser")
    pagination = soup.find('ul', class_="pagination")
    s = pagination.find_all('li')[-1].a
    number=(last_page(s))
    return number

def save(projects, path):
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Проект','Категория','Цена','Заявки'))

        for project in projects:
            writer.writerow((project['title'], project['categories'], project['price'], project['application'],))

def main(s):
    #print(parse(get_htm(s)))
    page_count = get_page_count(get_htm(s))
    print('всего найдено страниц %d' % page_count )

    projects = []

    for page in range(1, page_count):
        print ('Парсинг %d%%' % (page / page_count * 100))
        projects.extend(parse(get_htm(s +'?page=%d' %page)))
    print('Парсинг 100%')

#вывод данных на экран
    #for project in projects:
      #  print(project)

    save(projects,'test.csv')

if __name__ == '__main__':
    s = 'https://www.weblancer.net/jobs'
    # s = 'http://gymn11.ru'
    main(s)
