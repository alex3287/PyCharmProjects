#Парсер для сбора ссылок с сайта

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

def get_html(url):
    try:
        html = urlopen(url)
    except:
        print('нет сайта такого')
        return None
    else:
        return html.read()

def getTitle(html):
    try:
        suop = BeautifulSoup(html, "html.parser")
        title2 = suop.body.find('div',class_="blog").find_all('h2')
        title=[]
        for i in title2:
#ИНТЕРЕСНЫЙ МОМЕНТ НУЖНО ОБРАТИТЬ ВНИМАНИЕ
            title.append(i.a.attrs['href'])

    except AttributeError as e:
        return None
    return title

def all_links(html):
    suop = BeautifulSoup(html, "html.parser")
    links = suop.body.find_all("a")
    mas=[]
    for link in links:
        if 'href' in link.attrs:
            mas.append(link.attrs['href'])
    return mas

def type_links(mas):
    input2=[]
    output2=[]
    for i in mas:
        if 'http:' in i:
            output2.append(i)
        else:
            input2.append(i)
    return output2, input2
if __name__=="__main__":
    #url = input("Введите сайт для парсенга \n>>>")
    t=get_html('http://gymn11.ru')
    #print(all_links(t))
    print(type_links(all_links(t))[0])
    print(type_links(all_links(t))[1])

    #if t!=None:
        #print(t)
        #title = getTitle(t)
        #if title == None:
           # print("Title could not be found")
       # else:
            #print(title)
