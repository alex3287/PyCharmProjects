import requests

def connect(url):
    res = requests.get(url)
    t = res.text
    return t

def show(s, d):
    print(s[:d])

if __name__=='__main__':
    url = input('Введите адрес сайта >>>')

    print(len(connect(url)))
    d = int(input("Срез какой длины нужен??? >>>"))
    show(connect(url), d)