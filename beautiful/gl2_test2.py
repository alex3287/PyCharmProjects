from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://gymn11.ru/index.php/osnovnye-svedeniya/")
bsObj = BeautifulSoup(html, "html.parser")

#for sibling in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
#    print(sibling)

#allText = bsObj.findAll(id="text")
#print(allText[0].get_text())
for i in bsObj.find("div", {"id":"header"}):
    print(i)

print(bsObj.a)