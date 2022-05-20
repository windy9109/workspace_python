from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://127.0.0.1:5000/list")  

bsObject = BeautifulSoup(html, "html.parser") 
txt = bsObject.find_all("td", {"id":"e_name"})
#txt += bsObject.find_all("td", {"id":"sex"})
txt += bsObject.find_all("td", {"id":"addr"})
for i in txt:
    print (i.text)
#print(bsObject)