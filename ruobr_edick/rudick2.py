from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import time

N=5
def connect(url):
    driver = webdriver.Firefox()
    driver.get("https://www.ruobr.ru")
    assert "Электронная Школа" in driver.title
    driver.find_element_by_id("id_username").clear()
    elem = driver.find_element_by_id("id_username")
    elem.send_keys("alex3287")
    driver.find_element_by_id("id_password").clear()
    elem2 = driver.find_element_by_id("id_password")
    elem2.send_keys("winston")
    elem2.send_keys(Keys.RETURN)
    time.sleep(N)
    assert "ЭШ. Главная" in driver.title
    driver.find_element_by_link_text("Журнал").click()
    time.sleep(N)
    driver.find_element_by_link_text("КТП").click()
    time.sleep(N)
    driver.find_element_by_xpath("(//a[contains(text(),'Информатика и ИКТ')])[4]").click()
    time.sleep(N)
    #ТУТ БУДЕТ ДОБАВЛЕНИЕ ТЕМЫ, НУЖНО ВЫНЕСТИ В ФУНКЦИЮ
    driver.find_element_by_css_selector("span.dynatree-expander").click()
    time.sleep(N)
    #driver.find_element_by_xpath("//div[@id='tree']/ul/li/ul/li/span/span").click()
    s2=driver.find_element_by_class_name("contextMenu")
    a = driver.current_url
    print(a)
    a2=a+'#adddoc'


    """tre=driver.find_element_by_class_name("adddoc")
    time.sleep(N)
    p1=tre.find_element_by_link_text("Добавить тему")
    time.sleep(N)
    print(p1.text)"""


    #driver.find_element_by_link_text("Добавить тему").click()

    """time.sleep(3)
    driver.find_element_by_id("id_title").clear()
    driver.find_element_by_id("id_title").send_keys("Тут будет тема")
    driver.find_element_by_id("id_homework").clear()
    driver.find_element_by_id("id_homework").send_keys("тут домашка")
    driver.find_element_by_id("new_item_btn").click()
    link2 = driver.current_url
    return link2"""


def get_htm(url):
    response = urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    zag = soup.find_all('a')
    print(zag)

def main(s):
    print(s)
    parse(get_htm(s))

def scrap(url):
    """Эта лишнее пока"""
    session = requests.Session()
    params = {'username': 'alex3287', 'password': 'winston'}
    s = session.post(url, params)
    #print('обработка')
    s = session.get(url)
    print(s.text)

if __name__ == '__main__':
    print('SCRAP')
    print('*' * 50)
    connect('https://www.ruobr.ru')

    print('*'*50)
   #scrap(connect('https://www.ruobr.ru'))
    #driver.find_element_by_css_selector("button.login-btn").click()
    #wait = WebDriverWait(driver, 10)
    #element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))



    #print(link2)
    #main(link2)


#
