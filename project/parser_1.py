# Парсер для сбора внешних ссылок с сайта

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


url = 'http://gymn11.ru'


def get_html(url):
    '''Считывает страницу в html'''
    try:
        html = urlopen(url)
    except:
        print('нет сайта такого')
        return None
    else:
        return html.read()

def all_links(html):
    """Находит все ссылки на страницы
       и помещает их в список"""
    suop = BeautifulSoup(html, "html.parser")
    links = suop.body.find_all("a")
    mas = []
    for link in links:
        if 'href' in link.attrs:
            mas.append(link.attrs['href'])
    return mas

def print_l(links):
    '''вывод каждой ссылки в отдельную строчку'''
    k=0
    for i in links:
        k+=1
        print(k, i)

def type_links(mas):
    global url
    """Делит список ссылок на 2 категории:
        1. внешнии
        2. внутренние"""
    input2 = []
    output2 = []
    for i in mas:
        if ('http:' in i) or ('https:' in i):
            if url not in i:
                output2.append(i)
        elif (len(i)>2) and ('java' not in i):
            input2.append(i)
    return output2, input2

def sort2(mas):
    """Отбрасывает одинаковые ссылки"""
    b=[]
    for i in mas:
        if i[-1]!='/':
            k=i+'/'
            b.append(k)
        else: b.append(i)
    links1 = set(b)
    links=list(links1)
    return links

def out_link(links):
    """Создает настаящую ссылку из внутренней ссылки"""
    global url
    out_li = []
    for i in links:
        link = url+i
        out_li.append(link)
    return out_li

def seach_links(links):
    links_list = []
    n = 0
    for i in links:
        htm = get_html(i)
        if htm:
            n += 1
            print('сделано', n)
            links5 = all_links(htm)
            links6 = type_links(links5)
            links7 = sort2(links6[0])
            for k in links7:
                # print(k)
                links_list.append(k)
    return sort2(links_list)

if __name__ == "__main__":
    # url = input("Введите сайт для парсенга \n>>>")
    html = get_html(url)
    links = all_links(html)
    links2 = type_links(links)
    links3 = out_link(sort2(links2[1]))
    print_l(links3)
    print('*'*150)
    print_l(seach_links(links3))
    print('used')