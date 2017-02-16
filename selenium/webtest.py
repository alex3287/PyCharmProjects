from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_htm(url):
    response = urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    zag = soup.find_all('h1')
    print(zag)

def stop(x):
    i = 1
    for j in range(1, x):
        i *= j
    print(i)

def main(s):
    print(s)
    parse(get_htm(s))

if __name__ == '__main__':


    driver  = webdriver.Firefox()
    driver.get("https://www.ruobr.ru")

    assert "Электронная Школа" in driver.title

    driver.find_element_by_id("id_username").clear()
    elem = driver.find_element_by_id("id_username")
    elem.send_keys("alex3287")
    driver.find_element_by_id("id_password").clear()
    elem2 = driver.find_element_by_id("id_password")
    elem2.send_keys("winston")
    elem2.send_keys(Keys.RETURN)
    #driver.find_element_by_css_selector("button.login-btn").click()
    #wait = WebDriverWait(driver, 10)
    #element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))


    stop(80000)
    assert "ЭШ. Главная" in driver.title
    driver.find_element_by_link_text("Журнал").click()
    stop(80000)
    driver.find_element_by_link_text("КТП").click()
    stop(80000)
    driver.find_element_by_link_text("Информатика и ИКТ").click()
    link2 = driver.current_url
    #print(link2)
    main(link2)


#driver.find_element_by_link_text("Журнал").click()
#driver.find_element_by_link_text("КТП").click()
#elem2.send_keys(Keys.RETURN)
'''
assert "No results found." not in driver.page_source
driver.close()
driver = self.driver
        driver.get(self.base_url + "/accounts/login/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("alex3287")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("winston")
        driver.find_element_by_css_selector("button.login-btn").click()
        driver.find_element_by_link_text(u"Журнал").click()
        driver.find_element_by_link_text(u"КТП").click()
        driver.find_element_by_id("disp_param").click()
'''
